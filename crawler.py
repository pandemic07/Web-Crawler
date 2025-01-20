import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor

# Patterns to identify product pages based on URL structure
# RegEx
PRODUCT_URL_PATTERNS = [r"/product/", r"/item/", r"/p/"]

# Function to validate if a URL corresponds to a product page
def validate_product_url(url):
    return any(re.search(pattern, url) for pattern in PRODUCT_URL_PATTERNS)

# Function to handle crawling for a single domain
def process_domain(domain):
    print(f"Initiating crawl for: {domain}")
    discovered_product_urls = set()
    processed_urls = set()
    pending_urls = [domain]

    while pending_urls:
        current_url = pending_urls.pop()
        if current_url in processed_urls:
            continue
        processed_urls.add(current_url)
        try:
            response = requests.get(current_url, timeout=10)
            page_content = BeautifulSoup(response.text, "html.parser")

            # Extract and process all hyperlinks
            for anchor in page_content.find_all("a", href=True):
                full_url = urljoin(domain, anchor["href"])
                if validate_product_url(full_url):
                    discovered_product_urls.add(full_url)
                elif full_url.startswith(domain) and full_url not in processed_urls:
                    pending_urls.append(full_url)
        except Exception as error:
            print(f"Error processing {current_url}: {error}")

    print(f"Crawl completed for {domain}. Found {len(discovered_product_urls)} product URLs.")
    return domain, list(discovered_product_urls)

# Function to manage crawling across multiple domains
def crawl_multiple_domains(domains, max_threads=5):
    crawl_results = {}
    with ThreadPoolExecutor(max_threads) as executor:
        future_to_domain = {executor.submit(process_domain, domain): domain for domain in domains}
        for future in future_to_domain:
            try:
                domain, product_links = future.result()
                crawl_results[domain] = product_links
            except Exception as error:
                print(f"Error processing domain: {future_to_domain[future]} - {error}")
    return crawl_results

# List of domains to be crawled
ecommerce_domains = ["https://example1.com", "https://example2.com", "https://example3.com"]

if __name__ == "__main__":
    # Execute the crawling process
    crawl_output = crawl_multiple_domains(ecommerce_domains)

    # Save the results to a JSON file
    with open("discovered_product_urls.json", "w") as output_file:
        import json

        json.dump(crawl_output, output_file, indent=4)

    print("Crawling completed. Results saved to discovered_product_urls.json.")