#!/usr/bin/env python
#security_by_obscurity

import re

#read cipher text and assign to global var
f = open("security_by_obscurity.txt","r")
cipher_txt = f.read()
f.close()

cipher_txt = cipher_txt.replace('password', '')
cipher_txt = cipher_txt.replace('.', ' ')

counter = 0
for c in cipher_txt:
	if c is ' ':
		counter += 1

print(counter)
print(cipher_txt)