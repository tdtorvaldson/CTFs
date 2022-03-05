#! /bin/bash

user=natas6
pass=aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1
page_source=index.html

curl --user $user:$pass http://${user}.natas.labs.overthewire.org/${page_source}
