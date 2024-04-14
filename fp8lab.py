import webbrowser
import requests
from bs4 import BeautifulSoup

# Function to make a GET request to a URL and return the HTML content
def fetch_html(url):
    response = requests.get(url)
    return response.text

# Function to parse HTML content and extract data using BeautifulSoup
def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    # Example: Extracting titles of all <h1> tags
    titles = [title.text for title in soup.find_all('h1')]
    return titles

# Function to perform scraping
def scrape(url):
    html = fetch_html(url)
    data = parse_html(html)
    return data

# Example usage
if __name__ == "__main__":
    url = 'https://example.com'
    scraped_data = scrape(url)
    print(scraped_data)

    # Open the website in the default web browser
    webbrowser.open(url)
