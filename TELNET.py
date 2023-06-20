"""
TELNET V2
UNIQUE ID
BY SOLARIS SOFTWARE BULARES 🌞

20/06/2023
"""


from random import randint,choice
from hashlib import sha3_512
import uuid
from collect_info import*
from MSE import mse_cipher


def hash(src):
	return sha3_512(src.encode()).hexdigest().upper()


def gen_mdp():
	p = str(uuid.uuid4())
	return hash(p)


def get_user_ID(user_entry):
	ID = hash(user_entry)
	gl = geolocalisation()
	oes = others()

	print("\n\n\n")

	UID = hash(user_entry+gl+oes)

	return UID


def get_devian_user_ID(user_entry):
	ID = hash(user_entry)
	gl = geolocalisation()
	oes = others()

	key1,key2,key3 = gen_mdp(),gen_mdp(),gen_mdp()

	print("\n\n\n")

	UID = hash(key1+key2+key3+user_entry+gl+oes+mse_cipher(gen_mdp()))

	return UID



user_entry = """
Jhon
Doe
jhon_doe@gmail.com
44
California
23/05/1999
password: ay429ay887@@@
"""

ID = get_user_ID(user_entry)
print(ID)





