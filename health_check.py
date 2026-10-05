import requests


def check_url(url):
    response = requests.get(url, timeout=5)

    print(f"URL: {url}")
    print(f"Status Code: {response.status_code}")
    print(f"Response Time: {response.elapsed.total_seconds():.2f} seconds")
    print(f"HTTPS: {'Yes' if url.startswith('https://') else 'No'}")


check_url("https://google.com")