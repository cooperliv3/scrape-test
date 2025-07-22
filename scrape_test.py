import urllib.robotparser
from urllib.parse import urlparse

def check_scraping_allowed():
    url = input("Enter the full URL of the news site (e.g., https://www.example.com): ").strip()

    parsed_url = urlparse(url)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
    robots_url = f"{base_url}/robots.txt"

    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(robots_url)
    try:
        rp.read()
        user_agent = "*"
        can_fetch = rp.can_fetch(user_agent, url)
        if can_fetch:
            print(f"Scraping is allowed for {url}")
        else:
            print(f"Scraping is NOT allowed for {url}")
    except Exception as e:
        print(f"Could not read robots.txt from {robots_url}. Error: {e}")

if __name__ == "__main__":
    check_scraping_allowed()