import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
import sys
import time
def animated(text):
     for x in text:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.01)

logo = '''
  ██████  ▄████▄   ██▀███   ▄▄▄       ██▓███  ▓█████  ██▀███  
▒██    ▒ ▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒
░ ▓██▄   ▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ▓██░ ██▓▒▒███   ▓██ ░▄█ ▒
  ▒   ██▒▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██ ▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  
▒██████▒▒▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒▒██▒ ░  ░░▒████▒░██▓ ▒██▒
▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░▒  ░ ░  ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░
░  ░  ░  ░          ░░   ░   ░   ▒   ░░          ░     ░░   ░ 
      ░  ░ ░         ░           ░  ░            ░  ░   ░     
         ░  '''
animated(logo)
print('     »»»Devoloper_By_White_Devil«««')
def get_webpage_details(url):
    try:
        # Fetch the content of the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Get the page title
        title = soup.title.string if soup.title else 'No Title Found'
        
        # Get all meta tags
        meta_tags = {}
        for meta in soup.find_all('meta'):
            name = meta.get('name') or meta.get('property')
            content = meta.get('content')
            if name and content:
                meta_tags[name] = content
        
        # Get all links
        links = [urljoin(url, a.get('href')) for a in soup.find_all('a', href=True)]
        
        # Get the content of the webpage
        body = soup.get_text()
        
        # Display the webpage details
        print(f"Page Title: {title}\n")
        
        print("Meta Tags:")
        for name, content in meta_tags.items():
            print(f"  {name}: {content}")
        print()
        
        print("Links:")
        for link in links:
            print(f"  {link}")
        print()
        
        print("Page Content (First 1000 characters):")
        print(body[:1000])
    
    except requests.RequestException as e:
        print(f"Error: Unable to fetch the webpage content. {e}")

if __name__ == "__main__":
    url = 'https://smartvalue.biz'  # Replace with the URL of the website to scrape
    get_webpage_details(url)

