'''

Real - World Example -  Multithreading for I/O-bound Tasks
Scenario: Web Scraping
Web Scaraping often involves making numerous network requests to
fetch web pages. These tasks are I/O-bound because they spend a lot of time waiting for responses from servers.
Multithreading can significantly improve the performance by allowing web pages to be fetched concurrently.

'''
'''
https://langchain-ai.github.io/langgraph/tutorials/introduction/

https://langchain-ai.github.io/langgraph/concepts/

https://langchain-ai.github.io/langgraph/how-tos/

'''

import threading
import requests
from bs4 import BeautifulSoup

urls = [
    "https://langchain-ai.github.io/langgraph/tutorials/introduction/",
    "https://langchain-ai.github.io/langgraph/concepts/",
    "https://langchain-ai.github.io/langgraph/how-tos/"
]

def fetch_content(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        print(f"Fetched {len(soup.text)} characters from {url}")
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")

threads = []

for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All web pages done")


print("All Web pages DOne")

