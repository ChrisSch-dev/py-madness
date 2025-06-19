import requests
from bs4 import BeautifulSoup

def fetch_headlines(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    return [h.get_text(strip=True) for h in soup.find_all("h2")][:10]

def main():
    print("Simple Web Scraper")
    url = input("Enter website URL (e.g. https://news.ycombinator.com/): ")
    headlines = fetch_headlines(url)
    print("\nTop Headlines:")
    for h in headlines:
        print("-", h)

if __name__ == "__main__":
    main()