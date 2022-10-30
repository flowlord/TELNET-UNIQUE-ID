"""
TELNET PROTOTYPE
UNIC ID
BY SOLARIS SOFTWARE BULARES

CE PROGRAMME EST DESTINE POUR UNE OEUVRE FICTIVE
POUR LE PROJET DE FILM BYG EYE

30/10/2022
"""


from random import randint,choice
from hashlib import sha3_512
from string import ascii_letters

from collect_info import*


def hash(src):
	return sha3_512(src.encode()).hexdigest().upper()


def gen_mdp():
	x = randint(90,9999)
	
	p = ""
	
	for e in range(x):
		p = p+ choice(ascii_letters)
	
	return hash(p)


try:
	file = open("keys.pkm","a")
	file.close()
except FileNotFoundError:
	file = open("keys.pkm","w")
	file.close()


def save_keys(key):
	file = open("keys.pkm","a").write(key)

key1,key2,key3 = gen_mdp(),gen_mdp(),gen_mdp()

save_keys(key1+"\n\n")
save_keys(key2+"\n\n")
save_keys(key3+"\n\n")


user_entry = """
Jhon
Doe
44
Californie
23/05/1999
password: ay89ay89@@@
"""


user_entry = hash(user_entry)

gl = geolocalisation()
oes = others()

print("\n\n\n")

UID = hash(key1+key2+key3+user_entry+gl+oes)
UID = UID[:20]

print(UID)






