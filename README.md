
## **Project Title**  
E-commerce Product URL Crawler

---

## **Project Description**  
This project is a web crawler designed to discover and extract product URLs from multiple e-commerce websites. The crawler scans websites, identifies URLs matching predefined product URL patterns, and outputs a structured JSON file mapping each domain to its corresponding product URLs.

---

## **Features**  
- **URL Discovery:** Detects product URLs using patterns like `/product/`, `/item/`, and `/p/`.  
- **Scalability:** Supports concurrent crawling of multiple domains using threading.  
- **Efficiency:** Handles large websites with deep hierarchies by processing links iteratively.  
- **Robustness:** Includes error handling for network issues and invalid links.  
- **Output:** Generates a structured JSON file with unique product URLs for each domain.

---

## **Technologies Used**  
- **Python Libraries:**
  - `requests` for HTTP requests.
  - `BeautifulSoup` from `bs4` for parsing HTML and extracting links.
  - `re` for regular expressions to identify product URLs.
  - `concurrent.futures` for parallel processing.

---

## **How It Works**  
1. **Input:** A list of e-commerce domains (e.g., `["https://example1.com", "https://example2.com"]`).  
2. **Crawling:**  
   - For each domain:
     - Fetch the homepage using `requests`.
     - Parse the HTML using `BeautifulSoup`.
     - Extract links and convert relative links to absolute URLs.
     - Identify product URLs using predefined patterns.
   - Crawl internal links iteratively to discover more product pages.  
3. **Output:** A JSON file (`discovered_product_urls.json`) mapping each domain to its list of unique product URLs.

---

## **Setup and Installation**  
1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/ecommerce-crawler.git
   cd ecommerce-crawler
   ```
2. Create a virtual environment and activate it:  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

---

## **Usage**  
1. Add the domains you want to crawl to the `domains` list in the script:  
   ```python
   domains = ["https://example1.com", "https://example2.com"]
   ```
2. Run the script:  
   ```bash
   python crawler.py
   ```
3. The results will be saved to `discovered_product_urls.json` in the project directory.

---

## **Output Format**  
The output file `discovered_product_urls.json` will have the following structure:  
```json
{
  "https://example1.com": [
    "https://example1.com/product/123",
    "https://example1.com/item/456"
  ],
  "https://example2.com": [
    "https://example2.com/p/789"
  ]
}
```

---

## **Limitations**  
- Cannot handle dynamic content or infinite scrolling.  
- Relies on predefined patterns for product URLs.  

---

## **Future Enhancements**  
- Integrate support for dynamic content using Selenium or Puppeteer.  
- Implement domain-specific crawling rules for better accuracy.
