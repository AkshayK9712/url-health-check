import argparse
from urllib.parse import urlparse

import requests


def validate_url(url):
    """Check whether the URL has a valid HTTP or HTTPS scheme."""
    parsed = urlparse(url)

    if parsed.scheme not in ("http", "https"):
        return False

    if not parsed.netloc:
        return False

    return True


def check_url(url):
    """Send an HTTP request and report the health of the URL."""

    if not validate_url(url):
        print(f"\nURL: {url}")
        print("Error: Invalid URL. Use http:// or https://")
        return

    try:
        response = requests.get(url, timeout=5)

        response_time = response.elapsed.total_seconds()
        uses_https = urlparse(url).scheme == "https"

        print(f"\nURL: {url}")
        print(f"Status Code: {response.status_code}")
        print(f"Response Time: {response_time:.2f} seconds")
        print(f"HTTPS: {'Yes' if uses_https else 'No'}")

    except requests.exceptions.Timeout:
        print(f"\nURL: {url}")
        print("Error: Request timed out after 5 seconds.")

    except requests.exceptions.ConnectionError:
        print(f"\nURL: {url}")
        print("Error: Could not connect to the server. Check the URL, DNS, or network connection.")

    except requests.exceptions.RequestException as error:
        print(f"\nURL: {url}")
        print(f"Error: Request failed: {error}")


def main():
    """Read URLs from the command line and check each one."""

    parser = argparse.ArgumentParser(
        description="Check the health of one or more URLs."
    )

    parser.add_argument(
        "urls",
        nargs="+",
        help="One or more URLs to check"
    )

    args = parser.parse_args()

    print("URL Health Check")
    print("================")

    for url in args.urls:
        check_url(url)


if __name__ == "__main__":
    main()