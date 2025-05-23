import os
import time
import requests
from urllib.parse import urljoin, urlparse
import re
from docling.document_converter import DocumentConverter

# --- Configuration ---
BASE_URL = "https://cloud.google.com/sdk/gcloud/reference"
START_PAGE = BASE_URL + "/"
OUTPUT_DIR = "gcloud_online_docs_markdown"
REQUEST_DELAY = 0
# Seconds to wait between requests
USER_AGENT = "GCloudDocsToMarkdownFetcher/1.0"
GCLOUD_WIDE_FLAGS_PAGE_URL = "https://cloud.google.com/sdk/gcloud/reference/"
SKIP_URL_PREFIXES = [
    "https://cloud.google.com/sdk/gcloud/reference/alpha/",
    "https://cloud.google.com/sdk/gcloud/reference/beta/"
]
# --- End Configuration ---

def fetch_page(url):
    """Fetches the content of a given URL."""
    print(f"Fetching: {url}")
    headers = {'User-Agent': USER_AGENT}
    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_markdown_with_docling(html_content: str, page_url: str) -> str:
    """
    Converts HTML content to Markdown using Docling.
    """
    if not html_content:
        # Construct a minimal Markdown indicating failure, including the source URL
        return f"# Content Error for {page_url}\\n\\n*Source: [{page_url}]({page_url})*\\n\\nContent extraction failed: No HTML content provided."

    try:
        converter = DocumentConverter()
        # Docling's convert method can take 'document_bytes'.
        # We have html_content as a string, so we encode it.
        result = converter.convert(document_bytes=html_content.encode('utf-8')) # Docling should infer HTML
        markdown_content = result.document.export_to_markdown()
        
        # Prepend the source URL, similar to the old logic's intent
        final_markdown = f"*Source: [{page_url}]({page_url})*\\n\\n{markdown_content}"
        
        # Clean up excessive newlines, similar to old logic
        final_markdown = re.sub(r'\\n{3,}', '\\n\\n', final_markdown).strip()
        return final_markdown
    except Exception as e:
        print(f"Error converting HTML from {page_url} with Docling: {e}")
        # Construct Markdown indicating conversion error
        return f"# Conversion Error for {page_url}\\n\\n*Source: [{page_url}]({page_url})*\\n\\nDocling conversion failed: {e}"

def save_markdown(markdown_content, url, base_url_for_paths, output_dir):
    """Saves the Markdown content to a file, mirroring the URL structure."""
    parsed_url = urlparse(url)
    
    if not base_url_for_paths.endswith('/'):
        base_url_for_paths += '/'
    
    relative_path = url.replace(base_url_for_paths, "")
    if not relative_path:
        relative_path = "index.html" 

    path_parts = [part for part in relative_path.split('/') if part and part != '.']
    
    filename_html = "index.html"
    dir_path_parts = path_parts

    if path_parts and '.' in path_parts[-1]:
        filename_html = path_parts[-1]
        dir_path_parts = path_parts[:-1]
    elif path_parts :
        dir_path_parts = path_parts
        filename_html = "index.html"
    
    sanitized_dir_parts = [re.sub(r'[^\\w\\-_\\.]', '_', part) for part in dir_path_parts]
    base_filename, file_extension = os.path.splitext(filename_html)
    sanitized_base_filename = re.sub(r'[^\\w\\-_\\.]', '_', base_filename)

    current_output_path = output_dir
    for part in sanitized_dir_parts:
        if part:
            current_output_path = os.path.join(current_output_path, part)
    
    os.makedirs(current_output_path, exist_ok=True)

    markdown_filename = sanitized_base_filename + ".md"
    file_path = os.path.join(current_output_path, markdown_filename)
    
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(markdown_content)
        print(f"Saved Markdown: {file_path}")
    except IOError as e:
        print(f"Error saving file {file_path}: {e}")


def crawl_and_convert():
    """Main crawling and conversion function."""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    queue = [START_PAGE]
    visited_urls = set()
    normalized_skip_prefixes = [prefix.rstrip('/') + '/' for prefix in SKIP_URL_PREFIXES]

    while queue:
        current_url = queue.pop(0)
        normalized_url_for_visit_check = current_url.rstrip('/') if current_url != BASE_URL.rstrip('/') else current_url

        # Skip any URL that starts with any of the skip prefixes
        if any(normalized_url_for_visit_check.startswith(prefix.rstrip('/')) for prefix in normalized_skip_prefixes):
            print(f"Skipping configured URL prefix: {current_url}")
            continue

        if normalized_url_for_visit_check in visited_urls:
            continue
        
        parsed_current_url = urlparse(current_url)
        base_parsed_url = urlparse(BASE_URL)
        if parsed_current_url.hostname != base_parsed_url.hostname or \
           not parsed_current_url.path.startswith(base_parsed_url.path):
            print(f"Skipping irrelevant URL (domain/path mismatch): {current_url}")
            continue

        visited_urls.add(normalized_url_for_visit_check)
        
        html_content = fetch_page(current_url)
        if not html_content:
            time.sleep(REQUEST_DELAY)
            continue

        markdown_content = extract_markdown_with_docling(html_content, current_url)
        save_markdown(markdown_content, current_url, BASE_URL, OUTPUT_DIR)

        soup = BeautifulSoup(html_content, "html.parser")
        for link_tag in soup.find_all("a", href=True):
            href = link_tag['href']
            next_url_absolute = urljoin(current_url, href)
            
            next_url_parsed = urlparse(next_url_absolute)
            next_url_clean = next_url_parsed._replace(query="", fragment="").geturl()
            
            normalized_next_clean = next_url_clean.rstrip('/') if next_url_clean != BASE_URL.rstrip('/') else next_url_clean

            if normalized_next_clean not in visited_urls and \
               next_url_parsed.hostname == base_parsed_url.hostname and \
               next_url_parsed.path.startswith(base_parsed_url.path):
                queue.append(normalized_next_clean)
        
        time.sleep(REQUEST_DELAY)

    print("Crawling and Markdown conversion finished.")

if __name__ == "__main__":
    crawl_and_convert()
    print(f"All fetched gcloud CLI documentation saved as Markdown in ./{OUTPUT_DIR}/")