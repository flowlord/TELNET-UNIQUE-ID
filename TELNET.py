"""
TELNET V1
UNIQUE ID
BY SOLARIS SOFTWARE BULARES 🌞

CE PROGRAMME EST DESTINE POUR UNE OEUVRE FICTIVE
POUR LE PROJET DE FILM BIG EYE
IL N'EST EN AUCUN CAS A ÊTRE UTILISE POUR
SECURISE VOS DONNEES PERSONNELLES

15/11/2022
"""


from random import randint,choice
from hashlib import sha3_512
import uuid
from collect_info import*


def hash(src):
	return sha3_512(src.encode()).hexdigest().upper()


def gen_mdp():
	p = str(uuid.uuid4())
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
UID = UID[:randint(15,55)]

print(UID)






