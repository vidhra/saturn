import os
import time
import requests
from urllib.parse import urljoin, urlparse
import re
from bs4 import BeautifulSoup, NavigableString, Tag # Ensure BeautifulSoup and related classes are imported


BASE_URL = "https://awscli.amazonaws.com/v2/documentation/api/latest/reference"
START_PAGE = BASE_URL + "/index.html"
OUTPUT_DIR = "aws_cli_docs_markdown"
REQUEST_DELAY = 0 
USER_AGENT = "AWSCLI-DocsToMarkdownFetcher/1.0"
SKIP_URL_PREFIXES = [] 

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


def to_markdown_recursive(element, page_url):
    """
    Recursively converts an HTML element and its children to Markdown.
    page_url is the URL of the current page, used for resolving relative links.
    """
    if isinstance(element, NavigableString):
        s = str(element)
        if element.parent and element.parent.name in ['script', 'style']:
            return ""
        return s

    if element.name is None: 
        return ""
    needs_surrounding_newlines = element.name in [
        'p', 'div', 'section', 'article', 'aside', 'header', 'footer',
        'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ul', 'ol', 'li', 'dl', 'dt', 'dd',
        'pre', 'blockquote', 'table', 'hr', 'form', 'fieldset', 'figure'
    ]
    
    children_md_parts = []
    for child in element.contents:
        children_md_parts.append(to_markdown_recursive(child, page_url))
    children_md_concat = "".join(children_md_parts)


    if element.name == 'ul':
        list_items_md = ""
        for li_tag in element.find_all('li', recursive=False):
            li_content_md = "".join(to_markdown_recursive(child, page_url) for child in li_tag.contents).strip()
            list_items_md += f"- {li_content_md}\n"
        return f"\n{list_items_md.strip()}\n\n" if list_items_md.strip() else ""

    if element.name == 'ol':
        list_items_md = ""
        for i, li_tag in enumerate(element.find_all('li', recursive=False)):
            li_content_md = "".join(to_markdown_recursive(child, page_url) for child in li_tag.contents).strip()
            list_items_md += f"{i+1}. {li_content_md}\n"
        return f"\n{list_items_md.strip()}\n\n" if list_items_md.strip() else ""


    if element.name == 'dl':
        markdown_for_dl = ""
        processed_children = [c for c in element.children if isinstance(c, Tag)]
        idx = 0
        while idx < len(processed_children):
            current_child_element = processed_children[idx]
            
            if current_child_element.name == 'dt':
                dt_inner_md = "".join(to_markdown_recursive(c, page_url) for c in current_child_element.contents).strip()
                term_to_display = dt_inner_md # Simplified for AWS

                markdown_for_dl += f"\n**{term_to_display}**"
                idx += 1 
                
                if idx < len(processed_children) and processed_children[idx].name == 'dd':
                    dd_element = processed_children[idx]
                    dd_inner_md = "".join(to_markdown_recursive(c, page_url) for c in dd_element.contents).strip()
                    if dd_inner_md:
                        markdown_for_dl += f":\n{dd_inner_md}\n" 
                    else: 
                        markdown_for_dl += "\n" 
                    idx += 1 
                else: 
                    markdown_for_dl += "\n\n" 
            elif current_child_element.name == 'dd':
                dd_inner_md = "".join(to_markdown_recursive(c, page_url) for c in current_child_element.contents).strip()
                if dd_inner_md:
                     markdown_for_dl += f"\n: {dd_inner_md}\n\n"
                idx += 1
            else:
                markdown_for_dl += to_markdown_recursive(current_child_element, page_url)
                idx += 1
        
        return f"\n{markdown_for_dl.strip()}\n\n" if markdown_for_dl.strip() else ""

    if element.name == 'table':
        table_md = "\n"
        header_processed = False
        for row_idx, row_tag in enumerate(element.find_all('tr', recursive=False)):
            cells_md_list = []
            for cell_tag in row_tag.find_all(['th', 'td'], recursive=False):
                cell_content = "".join(to_markdown_recursive(child, page_url) for child in cell_tag.contents)
                cells_md_list.append(cell_content.strip().replace('\n', ' ')) 
            
            if not cells_md_list and not any(c.strip() for c in cells_md_list):
                continue

            table_md += "| " + " | ".join(cells_md_list) + " |\n"
            if (row_tag.find('th') or row_idx == 0) and not header_processed and cells_md_list :
                 table_md += "| " + " | ".join(['---'] * len(cells_md_list)) + " |\n"
                 header_processed = True # Ensure header markdown is added only once
        return table_md + "\n" if table_md.strip() else ""


    if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
        level = int(element.name[1])
        return '\n' + '#' * level + ' ' + children_md_concat.strip() + '\n\n'
    
    if element.name == 'p':
        stripped_children = children_md_concat.strip()
        if not stripped_children: 
            return "" 
        return stripped_children + '\n\n'

    if element.name == 'code':
        if element.parent and element.parent.name == 'pre':
            return children_md_concat 
        else:
            return f"`{children_md_concat.strip()}`" 

    if element.name == 'pre':

        code_text = element.get_text() 
        lang_hint = ""
        if 'class' in element.attrs:
            for cls in element['class']:
                if cls.startswith('language-'):
                    lang_hint = cls.replace('language-', '')
                    break
        return f"\n```{lang_hint}\n{code_text.strip()}\n```\n\n"

    if element.name == 'strong' or element.name == 'b':
        return f"**{children_md_concat.strip()}**"
    if element.name == 'em' or element.name == 'i':
        return f"*{children_md_concat.strip()}*"

    if element.name == 'dt': 
        stripped_content = children_md_concat.strip()
        if stripped_content: return f"\n**{stripped_content}**\n"
        return ""
    if element.name == 'dd': 
        stripped_content = children_md_concat.strip()
        if stripped_content: return f": {stripped_content}\n\n"
        return ""

    if element.name == 'a':
        if 'headerlink' in element.get('class', []):
            return ""
            
        href = element.get('href', '')
        text = children_md_concat.strip()
        
        if not text and 'title' in element.attrs:
             text = element['title']
        if not text and href: 
            text = href
        elif not text and not href: 
            return "" 
        
        if href:
            abs_href = urljoin(page_url, href)
            return f"[{text}]({abs_href})"
        else: 
            return text

    if element.name == 'br':
        return "  \n" 

    if element.name == 'hr':
        return "\n---\n\n"


    if element.name in ['div', 'section', 'article', 'main', 'aside', 'header', 'footer', 
                        'figure', 'figcaption', 'details', 'summary', 'blockquote',
                        'span', 'body', 'html']: # span is inline, but often used for grouping
        stripped_content = children_md_concat.strip()
        if not stripped_content:
            return ""
        
       
        if element.name in ['div', 'section', 'article', 'main', 'aside', 'header', 'footer', 
                            'figure', 'figcaption', 'details', 'summary', 'blockquote']:
            return f"\n{stripped_content}\n\n"
        return stripped_content 

    return children_md_concat.strip()


def extract_markdown_content(html_content, page_url):
    """Extracts the main documentation content and converts it to Markdown."""
    soup = BeautifulSoup(html_content, "html.parser")
    
    doc_title = "Untitled Document"
    title_tag = soup.find("title")
    if title_tag:
        doc_title = title_tag.get_text(strip=True)

    # Try to find the main content area in AWS CLI (Sphinx-based) docs
    content_area = soup.find("section", attrs={"role": "main"})
    if not content_area:
        # Fallback: try to find a div with a common Sphinx main content class/id
        content_area = soup.find("div", class_="body") # Common in Sphinx
    if not content_area:
        content_area = soup.find("div", attrs={"role": "main"})
    if not content_area: 
        # Last resort fallback
        h1 = soup.find('h1')
        if h1 and h1.parent:
            content_area = h1.parent # Use parent of first H1
        else: # If all else fails, use the whole body, but issue warning
            content_area = soup.find("body")
            print(f"Warning: Could not find specific main content area for {page_url}. Using body tag.")
            if not content_area: 
                return f"# {doc_title}\n\n*Content extraction failed: No body tag found for {page_url}.*"

    # Selectors for elements to remove from the content area before conversion
    # These are common in Sphinx documentation or general web cruft
    selectors_to_remove = [
        'nav', 'footer', 'aside', 'script', 'style',
        '.sphinxsidebar',         # Sphinx sidebar
        'div[role="navigation"]', # Generic navigation role
        'div[role="search"]',     # Search boxes
        '.related',               # Sphinx related links bar
        '#searchbox',             # Sphinx search box
        '.footer',                # Sphinx footer div
        'form',                   # Remove forms (e.g. search, feedback)
        '.γενικές πληροφορίες', # Corrected: Removed space after .
        'div.feedback',           # Feedback sections
        'a.ลิ้งค์สำหรับช่วยพัฒนา', # Thai text link "ลิ้งค์สำหรับช่วยพัฒนา"
        'div[id="awsdocs-page- πίνακας περιεχομένων"]', # Corrected: Used attribute selector for ID with spaces
        '.docutils.container',    # Often boilerplate containers
        '.contents.local.topic',  # Sphinx local TOCs
        '#table-of-contents'      # Common ID for TOCs
    ]
    for selector in selectors_to_remove:
        for tag in content_area.select(selector):
            tag.decompose() # Remove the tag and its content

    # Determine page title from H1 if available, otherwise use document title
    page_specific_title = doc_title # Default to <title>
    main_h1 = content_area.find('h1')
    if main_h1:
        page_specific_title = main_h1.get_text(strip=True)
        # main_h1.decompose() # Optionally remove H1 if it will be part of the header below
                          # Or let to_markdown_recursive handle it. Better to let it handle.

    markdown_output = f"# {page_specific_title}\n\n"
    markdown_output += f"*Source: [{page_url}]({page_url})*\n\n"

    # Process the children of the identified content_area
    for child_element in content_area.contents:
         markdown_output += to_markdown_recursive(child_element, page_url)
    
    # Clean up excessive newlines and strip leading/trailing whitespace
    markdown_output = re.sub(r'\n{3,}', '\n\n', markdown_output).strip()
    
    return markdown_output
# --- End Custom Markdown Conversion ---

def save_markdown(markdown_content, url, base_url_for_paths, output_dir):
    """Saves the Markdown content to a file, mirroring the URL structure."""
    parsed_url = urlparse(url)
    
    if not base_url_for_paths.endswith('/'):
        base_url_for_paths += '/'
    
    relative_path = url.replace(base_url_for_paths, "")
    if not relative_path or relative_path.endswith('/'): 
        relative_path = os.path.join(relative_path, "index.html")

    path_parts = [part for part in relative_path.split('/') if part and part != '.']
    
    filename_html = "index.html" 
    dir_path_parts = path_parts

    if path_parts and '.' in path_parts[-1]:
        filename_html = path_parts[-1]
        dir_path_parts = path_parts[:-1]
    elif path_parts :
        dir_path_parts = path_parts
        filename_html = "index.html" 
    
    sanitized_dir_parts = [re.sub(r'[^\w\-_\.]', '_', part) for part in dir_path_parts]
    base_filename, file_extension = os.path.splitext(filename_html)
    sanitized_base_filename = re.sub(r'[^\w\-_\.]', '_', base_filename if base_filename else "index")


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
    normalized_base_url = BASE_URL.rstrip('/') + '/'
    
    normalized_skip_prefixes = [ (prefix.rstrip('/') + '/') for prefix in SKIP_URL_PREFIXES]


    while queue:
        current_url = queue.pop(0)
        

        normalized_url_for_visit_check = current_url.rstrip('/')
        if normalized_url_for_visit_check == BASE_URL.rstrip('/'):
             normalized_url_for_visit_check = BASE_URL.rstrip('/') + '/' 


        if any(current_url.startswith(prefix) for prefix in SKIP_URL_PREFIXES): 
            print(f"Skipping configured URL prefix: {current_url}")
            continue

        if normalized_url_for_visit_check in visited_urls:
            continue
        
        parsed_current_url = urlparse(current_url)
        base_parsed_url = urlparse(normalized_base_url)

        if not (parsed_current_url.hostname == base_parsed_url.hostname and \
                parsed_current_url.path.startswith(base_parsed_url.path)):
            print(f"Skipping irrelevant URL (domain/path mismatch): {current_url}")
            continue

        visited_urls.add(normalized_url_for_visit_check)
        
        html_content = fetch_page(current_url)
        if not html_content:
            time.sleep(REQUEST_DELAY)
            continue

        markdown_content = extract_markdown_content(html_content, current_url) 
        save_markdown(markdown_content, current_url, normalized_base_url, OUTPUT_DIR)

        soup = BeautifulSoup(html_content, "html.parser")
        print(f"\n--- Links on {current_url} ---") # DEBUG
        for link_tag in soup.find_all("a", href=True):
            href = link_tag['href']
            next_url_absolute = urljoin(current_url, href) 
            
            next_url_parsed = urlparse(next_url_absolute)
            next_url_clean = next_url_parsed._replace(query="", fragment="").geturl()
            
            normalized_next_clean_for_visit = next_url_clean.rstrip('/')
            if normalized_next_clean_for_visit == BASE_URL.rstrip('/'):
                normalized_next_clean_for_visit = BASE_URL.rstrip('/') + '/'

            print(f"  Found href: {href} -> Abs: {next_url_absolute} -> Clean: {next_url_clean} -> NormVisit: {normalized_next_clean_for_visit}") # DEBUG

            cond_not_visited = normalized_next_clean_for_visit not in visited_urls
            cond_same_hostname = next_url_parsed.hostname == base_parsed_url.hostname
            cond_correct_path = next_url_parsed.path.startswith(base_parsed_url.path)
            
            print(f"    Checking conditions: Not Visited? {cond_not_visited}, Same Host? {cond_same_hostname}, Correct Path? {cond_correct_path}") # DEBUG

            if cond_not_visited and cond_same_hostname and cond_correct_path:
                queue.append(next_url_clean)
                print(f"      Added to queue: {next_url_clean}") # DEBUG
            else:
                print(f"      NOT added to queue.") # DEBUG
        
        print("--- End Links ---") # DEBUG
        if REQUEST_DELAY > 0:
            time.sleep(REQUEST_DELAY)

    print("Crawling and Markdown conversion finished.")

if __name__ == "__main__":
    crawl_and_convert()
    print(f"All fetched AWS CLI documentation saved as Markdown in ./{OUTPUT_DIR}/") 