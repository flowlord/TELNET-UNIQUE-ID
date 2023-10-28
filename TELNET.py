"""
TELNET ID V3
UNIQUE ID
BY SOLARIS SOFTWARE BULARES 🌞

28/10/2023
"""

from hashlib import sha3_512
from collect_info import*
import os
from asensio import aes_encrypt, aes_decrypt


def hash(src):
	return sha3_512(src.encode()).hexdigest().upper()


def get_user_ID(geo):

	gl = ""
	user_entry = get_user_entry()

	if geo is True:
		gl = geolocalisation()

	gmi = get_more_info()

	os.remove("result.txt")
	os.remove("network.txt")

	UID = user_entry+gl+gmi

	return hash(UID)


def auto_encrypt(file):
	ID = get_user_ID(True)
	print(ID)
	aes_encrypt(file, ID)
	

def auto_decrypt(file):
	ID = get_user_ID(True)
	aes_decrypt(file, ID)


file = r"C:\Users\SSB\Documents\pic.png"
auto_encrypt(file)


# auto_decrypt("C:\Users\SSB\Documents\out_pic.png")


