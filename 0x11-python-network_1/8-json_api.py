#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
a URL with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    res = requests.post(url, data={'q': sys.argv[1]})

    try:
        res = res.json()

        if res:
            print("[{}] {}".format(res['id'], res['name']))
        else:
            print("No result")
    except Exception:
        print('Not a valid JSON')
