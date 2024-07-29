#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays the value
of the X-Request-Id variable found in the header ofthe response.
"""

if __name__ == "__main__":
    import sys
    import urllib.request as ur

    url = sys.argv[1]

    request = ur.Request(url)
    with ur.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
