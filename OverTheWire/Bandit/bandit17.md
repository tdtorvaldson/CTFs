## Solution

``` Shell
$: chmod 440 rsa_key_16
$: ssh bandit17@bandit.labs.overthewire.org -p 2220 -i rsa_key_16
bandit17@bandit:~$ diff passwords.new passwords.old
42c42
< kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
---
> w0Yfolrc5bwjS4qw5mq1nnQi6mF03bii
```

>key = 
kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
