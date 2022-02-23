# Glitch Cat

## Overview
Points: 100 | Category: General Skills

## Description
> Our flag printing service has started glitching! $ nc saturn.picoctf.net 53639

## Step 1
Save the flag given by netcat:
``` shell
$ nc saturn.picoctf.net 53639 >> flag.txt
```

## Step 2
Here we can see the flag is encoded in hexadecimal, so I wrote a script to get the rest of the flag:
> 'picoCTF{gl17ch_m3_n07_' + chr(0x38) + chr(0x31) + chr(0x31) + chr(0x66) + chr(0x66) + chr(0x66) + chr(0x65) + chr(0x65) + '}'

``` python
#! /usr/bin/python3
import sys
import re

# Open the file where you saved the output
file = sys.argv[1]
flag = open(file).read()

# Find the pattern inside the output
pattern = "(chr\(....\))"
result = re.findall(pattern, flag)

# Convert the pattern to ASCII
def convert_to_ascii(string):
    encoded = string[4:-1]          # take only the hex part
    decoded = int(encoded, base=16) # don't forget to specify the base                                                                                
    decoded = chr(decoded)          # finally convert to ascii                                                                                        
    return decoded                                                                                                                                    
                                                                                                                                                      
# Output the encoded flag                                                                                                                             
encoded_flag = list(map(convert_to_ascii, result))                                                                                                    
encoded_flag = "".join(encoded_flag)                                                                                                                  
print(encoded_flag) 
```

Don't forget to pass the file as argument:
``` shell
$ python3 get_flag.py flag.txt
```

## Flag
> picoCTF{gl17ch_m3_n07_811fffee}