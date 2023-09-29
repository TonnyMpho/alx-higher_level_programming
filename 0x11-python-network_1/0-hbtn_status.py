#!/usr/bin/python3
""" using urllib """
import urllib.request


if __name__ == "__main__":
    url = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(url) as response:
        data = response.read()
        print("Body response:")
        print("    - type: {}".format(type(data)))
        print("    - content: {}".format(data))
        print("    - utf8 content: {}".format(data.decode('utf8')))
