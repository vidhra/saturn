import os
import time
import requests
from bs4 import BeautifulSoup, NavigableString, Tag
from urllib.parse import urljoin, urlparse
import re

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

# --- Global Caches for GCLOUD WIDE FLAGS ---
gcloud_wide_flag_descriptions_cache = {}
gcloud_wide_flags_page_soup_cache = None
# --- End Global Caches ---

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

def get_gcloud_wide_flags_page_soup():
    """
    Fetches (if not already cached) and returns the BeautifulSoup object 
    for the main GCLOUD_WIDE_FLAGS_PAGE_URL.
    """
    global gcloud_wide_flags_page_soup_cache
    if gcloud_wide_flags_page_soup_cache is None:
        print(f"Fetching global flags definition page: {GCLOUD_WIDE_FLAGS_PAGE_URL}")
        html_content = fetch_page(GCLOUD_WIDE_FLAGS_PAGE_URL)
        if html_content:
            gcloud_wide_flags_page_soup_cache = BeautifulSoup(html_content, "html.parser")
        else:
            # Mark as error if fetching failed to prevent retries within the same run
            gcloud_wide_flags_page_soup_cache = "ERROR_FETCHING"
            print(f"Failed to fetch global flags page: {GCLOUD_WIDE_FLAGS_PAGE_URL}")
            
    if gcloud_wide_flags_page_soup_cache == "ERROR_FETCHING":
        return None
    return gcloud_wide_flags_page_soup_cache

def to_markdown_recursive(element, page_url):
    """
    Recursively converts an HTML element and its children to Markdown.
    page_url is the URL of the current page, used for resolving relative links.
    """
    if isinstance(element, NavigableString):
        return str(element)

    if element.name is None:
        return ""

    # --- Elements that manage their children's conversion explicitly ---
    if element.name == 'ul':
        list_items_md = ""
        for li_tag in element.find_all('li', recursive=False):
            li_content_md = to_markdown_recursive(li_tag, page_url)
            list_items_md += f"- {li_content_md}\n"
        return f"\n{list_items_md.strip()}\n\n" if list_items_md.strip() else ""

    if element.name == 'ol':
        list_items_md = ""
        for i, li_tag in enumerate(element.find_all('li', recursive=False)):
            li_content_md = to_markdown_recursive(li_tag, page_url)
            list_items_md += f"{i+1}. {li_content_md}\n"
        return f"\n{list_items_md.strip()}\n\n" if list_items_md.strip() else ""

    if element.name == 'li':
        inner_content = "".join(to_markdown_recursive(child, page_url) for child in element.contents)
        return inner_content.strip()

    if element.name == 'dl':
        markdown_for_dl = ""
        processed_children = [c for c in element.children if isinstance(c, Tag) or \
                              (isinstance(c, NavigableString) and c.string and c.string.strip())]
        idx = 0
        while idx < len(processed_children):
            current_child_element = processed_children[idx]
            
            if isinstance(current_child_element, Tag) and current_child_element.name == 'dt':
                dt_beautifulsoup_element = current_child_element # Keep ref to the original bs4 element
                dt_inner_md = "".join(to_markdown_recursive(c, page_url) for c in dt_beautifulsoup_element.contents).strip()
                
                flag_text_candidate = ""
                code_tag_in_dt = dt_beautifulsoup_element.find('code')
                if code_tag_in_dt:
                    raw_code_text = code_tag_in_dt.get_text(strip=True)
                    if raw_code_text.startswith('--') or \
                       (raw_code_text.startswith('-') and len(raw_code_text) > 1 and not raw_code_text.startswith('---')):
                        flag_text_candidate = raw_code_text
                
                term_to_display = flag_text_candidate if flag_text_candidate else dt_inner_md

                # --- Special handling for "GCLOUD WIDE FLAGS" section ---
                if term_to_display.upper() == "GCLOUD WIDE FLAGS":
                    next_dd_index = idx + 1
                    if next_dd_index < len(processed_children) and \
                       isinstance(processed_children[next_dd_index], Tag) and \
                       processed_children[next_dd_index].name == 'dd':
                        
                        dd_element_for_wide_flags = processed_children[next_dd_index]
                        
                        current_section_md_parts = [f"\n**{term_to_display}**:\n"] # Section title
                        
                        individual_flags_details_md = ""
                        # Find <a> tags within the <dd> that link to flags
                        flag_anchor_tags = dd_element_for_wide_flags.find_all('a', href=True)
                        processed_any_flag_links = False

                        for link_tag in flag_anchor_tags:
                            flag_name_from_link = link_tag.get_text(strip=True)
                            if not (flag_name_from_link.startswith('--') or \
                                   (flag_name_from_link.startswith('-') and len(flag_name_from_link) > 1 and not flag_name_from_link.startswith('---'))):
                                continue # Skip if it doesn't look like a flag name
                            processed_any_flag_links = True

                            description_md = gcloud_wide_flag_descriptions_cache.get(flag_name_from_link)
                            if description_md is None: # Not in cache
                                fetched_desc_for_cache = "[Description not available]" # Default
                                main_flags_page_soup = get_gcloud_wide_flags_page_soup()
                                if main_flags_page_soup:
                                    # ID on the target page is usually the fragment from href (e.g., #--format -> id="--format")
                                    target_id = urlparse(link_tag.get('href')).fragment or flag_name_from_link
                                    
                                    flag_dt_on_global_page = main_flags_page_soup.find('dt', id=target_id)
                                    if flag_dt_on_global_page:
                                        desc_dd_on_global_page = flag_dt_on_global_page.find_next_sibling('dd')
                                        if desc_dd_on_global_page:
                                            # Convert the <dd>'s content to Markdown, using the global page URL as base
                                            fetched_desc_for_cache = "".join(to_markdown_recursive(c, GCLOUD_WIDE_FLAGS_PAGE_URL) for c in desc_dd_on_global_page.contents).strip()
                                        else: fetched_desc_for_cache = f"[Description <dd> not found for {flag_name_from_link} on global page]"
                                    else: fetched_desc_for_cache = f"[Flag <dt id='{target_id}'> not found for {flag_name_from_link} on global page]"
                                else: fetched_desc_for_cache = "[Global flags page could not be processed to find description]"
                                
                                description_md = fetched_desc_for_cache
                                gcloud_wide_flag_descriptions_cache[flag_name_from_link] = description_md
                            
                            individual_flags_details_md += f"**{flag_name_from_link}**:\n{description_md}\n\n"
                        
                        if processed_any_flag_links:
                            current_section_md_parts.append(individual_flags_details_md)
                        else:
                            # Fallback: if no specific flag links processed, render original <dd> content
                            original_dd_content = "".join(to_markdown_recursive(c, page_url) for c in dd_element_for_wide_flags.contents).strip()
                            current_section_md_parts.append(f"{original_dd_content}\n\n")
                        
                        markdown_for_dl += "".join(current_section_md_parts)
                        idx = next_dd_index + 1 # Advance index past the processed <dt> and <dd>
                        continue # Skip normal <dt>/<dd> processing for this handled section
                    # else: GCLOUD WIDE FLAGS <dt> was not followed by a <dd>. Fall through to normal processing.
                # --- End of special handling for "GCLOUD WIDE FLAGS" ---
                
                # Regular <dt>/<dd> processing (if not GCLOUD WIDE FLAGS or special handling didn't apply)
                markdown_for_dl += f"\n**{term_to_display}**" # The term/flag itself
                idx += 1 # Advance past <dt>
                
                if idx < len(processed_children) and \
                   isinstance(processed_children[idx], Tag) and processed_children[idx].name == 'dd':
                    dd_element = processed_children[idx]
                    dd_inner_md = "".join(to_markdown_recursive(c, page_url) for c in dd_element.contents).strip()
                    if dd_inner_md:
                        markdown_for_dl += f":\n{dd_inner_md}\n" # Description on new line(s)
                    else: # Empty <dd>
                        markdown_for_dl += "\n" # Newline after <dt>
                    idx += 1 # Advance past <dd>
                else: # <dt> without a corresponding <dd>
                    markdown_for_dl += "\n\n" # Add paragraph spacing

            elif isinstance(current_child_element, Tag) and current_child_element.name == 'dd':
                # This <dd> was not immediately preceded by a <dt> in our filtered list (or <dl> starts with <dd>)
                dd_inner_md = "".join(to_markdown_recursive(c, page_url) for c in current_child_element.contents).strip()
                if dd_inner_md:
                     markdown_for_dl += f"\n: {dd_inner_md}\n\n"
                idx += 1
            
            elif isinstance(current_child_element, Tag): # Some other tag found directly within <dl>
                markdown_for_dl += to_markdown_recursive(current_child_element, page_url)
                idx += 1
            
            elif isinstance(current_child_element, NavigableString): # A significant string node directly in <dl>
                markdown_for_dl += str(current_child_element)
                idx += 1
            else:
                idx +=1

        if markdown_for_dl.strip():
            return "\n" + markdown_for_dl.strip() + "\n\n"
        return ""

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
                 header_processed = True
        return table_md + "\n" if table_md.strip() else ""

    children_md_concat = "".join(to_markdown_recursive(child, page_url) for child in element.contents)

    if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
        level = int(element.name[1])
        return '#' * level + ' ' + children_md_concat.strip() + '\n\n'
    
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
        current_classes = element.get('class', [])
        lang_class = [cls.replace('language-', '') for cls in current_classes if isinstance(cls, str) and cls.startswith('language-')]
        lang_hint = lang_class[0] if lang_class else ""
        return f"\n```{lang_hint}\n{code_text.strip()}\n```\n\n"

    if element.name == 'strong' or element.name == 'b':
        return f"**{children_md_concat.strip()}**"
    if element.name == 'em' or element.name == 'i':
        return f"*{children_md_concat.strip()}*"

    if element.name == 'dt': # Fallback for dt outside handled dl
        stripped_content = children_md_concat.strip()
        if stripped_content: return f"\n**{stripped_content}**\n"
        return ""
    if element.name == 'dd': # Fallback for dd outside handled dl
        stripped_content = children_md_concat.strip()
        if stripped_content: return f": {stripped_content}\n\n"
        return ""

    if element.name == 'a':
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

    if element.name in ['div', 'section', 'article', 'main', 'aside', 'header', 'footer', 'figure', 'figcaption', 'details', 'summary']:
        stripped_content = children_md_concat.strip()
        if not stripped_content:
            return ""
        return f"\n{stripped_content}\n\n"

    return children_md_concat


def extract_markdown_content(html_content, page_url):
    """Extracts the main documentation content and converts it to Markdown."""
    soup = BeautifulSoup(html_content, "html.parser")
    
    doc_title = "Untitled Document"
    title_tag = soup.find("title")
    if title_tag:
        doc_title = title_tag.get_text(strip=True)

    content_area = soup.find("div", class_="devsite-article-body")
    if not content_area: content_area = soup.find("devsite-content")
    if not content_area: content_area = soup.find("article", class_="devsite-article")
    if not content_area: content_area = soup.find("main")
    
    if not content_area:
        print(f"Warning: Could not find main content area for {page_url}. Using fallback.")
        h1 = soup.find('h1')
        if h1 and h1.parent:
            content_area = h1.parent
        else:
            content_area = soup.find("body")
            if not content_area: 
                return f"# {doc_title}\n\n*Content extraction failed: No body tag found for {page_url}.*"

    selectors_to_remove = [
        'nav', 'footer', 'aside', 'script', 'style',
        '.devsite-page-title-attributes', '.devsite-feedback-project',
        '.devsite-breadcrumb-link', 'div.devsite-header', 'div.devsite-footer-promos',
        'div.devsite-toc', 'div.devsite-tabs-section', 'div.devsite-search-form',
        'div#gc-site-footer', 'div.project-feedback', '.toc'
    ]
    for selector in selectors_to_remove:
        for tag in content_area.select(selector):
            tag.decompose()

    main_h1 = content_area.find('h1')
    if main_h1:
        page_specific_title = main_h1.get_text(strip=True)
    else:
        page_specific_title = doc_title

    markdown_output = f"# {page_specific_title}\n\n"
    markdown_output += f"*Source: [{page_url}]({page_url})*\n\n"

    for child_element in content_area.contents:
         markdown_output += to_markdown_recursive(child_element, page_url)
    
    markdown_output = re.sub(r'\n{3,}', '\n\n', markdown_output).strip()
    
    return markdown_output

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
    
    sanitized_dir_parts = [re.sub(r'[^\w\-_\.]', '_', part) for part in dir_path_parts]
    base_filename, file_extension = os.path.splitext(filename_html)
    sanitized_base_filename = re.sub(r'[^\w\-_\.]', '_', base_filename)

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

        markdown_content = extract_markdown_content(html_content, current_url)
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