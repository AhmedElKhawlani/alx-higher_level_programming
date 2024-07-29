#!/usr/bin/python3
"""
Script that takes list commits
"""

if __name__ == '__main__':
    import requests
    import sys

    arg1, arg2 = sys.argv[1], sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(arg2, arg1)
    r = requests.get(url)
    commits = r.json()
    for commit in commits[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
