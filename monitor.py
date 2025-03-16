
#### **monitor.py**
```python
import requests
import time

urls = ["https://www.google.com", "https://www.github.com", "https://api.github.com"]

def check_url(url):
    try:
        start = time.time()
        response = requests.get(url, timeout=5)
        duration = round(time.time() - start, 3)
        print(f"{url} - Status: {response.status_code}, Time: {duration}s")
    except requests.RequestException:
        print(f"{url} - Failed to connect")

for url in urls:
    check_url(url)
