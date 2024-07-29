#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL
& displays the body of the response
"""

if __name__ == '__main__':
    import requests
    import sys

    r = requests.get(sys.argv[1])
    status = r.status_code
    print(r.text) if status < 400 else print(
        "Error code: {}".format(r.status_code))
