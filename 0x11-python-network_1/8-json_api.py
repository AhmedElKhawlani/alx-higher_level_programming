#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""

if __name__ == '__main__':
    import requests
    import sys

    q = sys.argv[1] if len(sys.argv) == 2 else ""
    url = 'http://0.0.0.0:5000/search_user'
    r = requests.post(url, data={'q': q})
    try:
        r_dict = r.json()
        id, name = r_dict.get('id'), r_dict.get('name')
        if len(r_dict) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(r_dict.get('id'), r_dict.get('name')))
    except Exception:
        print("Not a valid JSON")
