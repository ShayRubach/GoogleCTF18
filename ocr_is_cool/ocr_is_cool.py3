#!/usr/bin/env python
#OCR is cool

import re

#read cipher text and assign to global var
f = open("cropped_img.ocr.txt","r")
cipher_txt = f.read()
f.close()
offset_a = -19
offset_b = 7

def decrypt_caesar(txt):
	offset = offset_a
	for c in txt:
		if re.match('^[a-zA-Z]+$',c):
			print( chr(ord(c)+fixed_offset(c)), end = '')
		else:
			print(c, end = '')
	print("")

def fixed_offset(c):
		# check ascii boundries for offsets calculated:
		if(97 <= ord(c) <= 115 or 65 <= ord(c) <= 83):
			return offset_b
		else:
			return offset_a


#lazy decrypt
decrypt_caesar(cipher_txt)
