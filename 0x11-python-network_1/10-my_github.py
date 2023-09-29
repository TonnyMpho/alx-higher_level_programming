#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    header = {"Authorization": "Basic {}:{}".format(username, password)}

    res = requests.get('https://api.github.com/user', headers=header)

    if res.status_code == 200:
        user = res.json()
        print(user['id'])
    else:
        print("None")
