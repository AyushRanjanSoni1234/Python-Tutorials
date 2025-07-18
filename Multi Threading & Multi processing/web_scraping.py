import threading
import time
import requests
from bs4 import BeautifulSoup

def fetch_url(url):
    response = requests.get(url)
    try:
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.title.string if soup.title else 'No Title'
            print(f'Title: {title}')
            print(f'Length of Characters in {url}: {len(soup.text)}')
    except requests.exceptions.RequestException as e:
        print(f'Error fetching {url}: {e}')

urls = ['https://www.geeksforgeeks.org/xgboost/',
        'https://www.geeksforgeeks.org/data-science-with-python-tutorial/',
        'https://www.geeksforgeeks.org/data-analysis-tutorial/']        

# Create threads
threads = []
for url in urls:
    thread = threading.Thread(target=fetch_url, args=(url,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All threads completed.")
print("Done!")    