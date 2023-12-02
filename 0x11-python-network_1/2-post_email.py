#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter, and displays the body of
the response
"""

import urllib.request
import sys
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('ascii')
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        body = response.read().decode('utf-8')
        print(body)
