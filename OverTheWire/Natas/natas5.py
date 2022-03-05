#! /usr/bin/python3

import requests
import re

username = "natas5"
password = "iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq"
url = f"http://{username}.natas.labs.overthewire.org"

headers = {}
response = requests.get(url, auth = (username, password))
content = response.text

print(content)
