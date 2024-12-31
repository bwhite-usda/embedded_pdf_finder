# This is embedded_pdf_finder.py
import requests
from bs4 import BeautifulSoup
import re

def find_embedded_pdfs(url):
    # Fetch the HTML content of the page
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return []

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all links that contain 'pdf' in the href attribute
    pdf_links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        if href.endswith('.pdf') or 'pdf' in href.lower():
            # Convert relative links to absolute links
            pdf_url = requests.compat.urljoin(url, href)
            pdf_links.append(pdf_url)

    # Display results
    if pdf_links:
        print("Found the following PDF links:")
        for pdf in pdf_links:
            print(pdf)
    else:
        print("No PDFs found on this page.")

    return pdf_links

# URL of the directive page
url = "https://www.usda.gov/directives/dr-2100-003"
pdf_links = find_embedded_pdfs(url)