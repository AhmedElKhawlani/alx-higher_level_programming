#!/usr/bin/python3
"""
Python script that takes your Github credentials (username and password)
and uses the Github API to display your id
"""

if __name__ == '__main__':
    import requests
    import sys
    from requests.auth import HTTPBasicAuth

    url = 'https://api.github.com/users/{}'.format(sys.argv[1])
    r = requests.get(url,
                     auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    print(r.json().get('id'))
