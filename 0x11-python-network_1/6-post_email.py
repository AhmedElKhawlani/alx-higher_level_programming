#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays the value
of the X-Request-Id variable found in the header ofthe response.
"""

if __name__ == '__main__':
    import requests
    import sys

    load = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], data=load)
    print(r.text)
