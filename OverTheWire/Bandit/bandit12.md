## Solution

Create a tmp directory.
``` Shell
bandit12@bandit:~$ mdkir /tmp/tdt
bandit12@bandit:~$ cp data.txt /tmp/tdt
bandit12@bandit:/tmp/tdt$ xxd -r data.txt > flag
```

---
**Here the fun begins** :)<br>
You have to analyze each file type and revert back, let's start by hexdump file.
``` Shell
bandit12@bandit:/tmp/tdt$ xxd -r data.txt > flag
bandit12@bandit:/tmp/tdt$ file flag 
flag: gzip compressed data, was "data2.bin", last modified: Thu May  7 18:14:30 2020, max compression, from Unix
```

---
Don't forget to change the file extension!
``` Shell
bandit12@bandit:/tmp/tdt$ mv flag flag.gz
bandit12@bandit:/tmp/tdt$ gunzip flag.gz 
bandit12@bandit:/tmp/tdt$ file flag 
flag: bzip2 compressed data, block size = 900k
```

---
Repeat the same step a thousand times.
``` Shell
bandit12@bandit:/tmp/tdt$ mv flag flag.bz2
bandit12@bandit:/tmp/tdt$ bunzip2 flag.bz2 
bandit12@bandit:/tmp/tdt$ file flag 
flag: gzip compressed data, was "data4.bin", last modified: Thu May  7 18:14:30 2020, max compression, from Unix
```

---
I refuse to paste the same thing twice.
``` Shell
bandit12@bandit:/tmp/tdt$ file flag 
flag: POSIX tar archive (GNU)
bandit12@bandit:/tmp/tdt$ mv flag flag.tar
bandit12@bandit:/tmp/tdt$ mv flag flag.tar
bandit12@bandit:/tmp/tdt$ tar -xvf flag.tar 
data5.bin
```
Tar flags:
- x: extract an arquive
- v: verbose
- f: use archive file

---
Finally...
``` Shell
bandit12@bandit:/tmp/tdt$ cat data8
The password is 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL
```

>key = 
8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL
