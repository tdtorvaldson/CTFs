# Nice netcat...

## Overview
Points: 15 | Category: General Skills

## Description
> There is a nice program that you can talk to by using this command in a shell: $ nc mercury.picoctf.net 22342, but it doesn't speak English...

## Step 1
Save the flag given by netcat.
```
$ nc mercury.picoctf.net 22342 > flag.txt
```

## Step 2
The hint gives away that the flag is using ASCII format, so I wrote a simple script that makes the conversion.
```
#! /usr/bin/python3

with open('flag.txt') as f:
    lines = f.readlines()
    
flag = ""
for c in lines:
    c = int(c.strip(" \n"))
    s = chr(c) 
    flag += s

print(flag)
```

## Flag
picoCTF{g00d_k1tty!_n1c3_k1tty!_5fb5e51d}