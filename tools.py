#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from random import shuffle,choice,randint
import shutil
from string import ascii_letters,digits,punctuation
from configs.init import name,carac_sub
from generateur_parametre import get_random_setting


def reinitialiser():
	"""
	Suprime vos clés de chiffrement !
	"""
	
	if os.path.exists("keylib.keys"):
		os.remove("keylib.keys")
	
	try:
		shutil.rmtree('__pycache__')
		shutil.rmtree('configs/__pycache__')
	except FileNotFoundError:
		pass


def mixer():
	"""
	Mélange l'ordre des caractères
	example:
		AAAZZZ ---> | mixer | ---> ZAAZAZ
	"""
	reinitialiser()
	
	init = open(name,'r',encoding='utf-8').readlines()
	init = "".join(init)
	init = list(init)

	shuffle(init)

	res = "".join(init)

	f = open(name,'w',encoding='utf-8')
	f.write(res)
	f.close()


def rebuild():
	"""
	reconstruit le fichier des caractères spéciaux
	en supriment les doublons et aussi les caractères
	indiqués dans carac_sub
	"""
	reinitialiser()
	
	old_carac = open(name,'r',encoding='utf-8').read()
	new_carac = []
	
	for e in old_carac:
		if e not in carac_sub and e not in new_carac:
			if e != "\n":
				new_carac.append(e)
	
	new_carac = "".join(new_carac)
	
	open(name,'w',encoding='utf-8').write(new_carac)
	

def first_mixer():
	"""
	Mélange l'ordre des caractères et génère des paramètre aléatoire, si
	l'utilisateur utilise pour la première fois
	le programme.
	"""

	try:
		f = open("user.data", "r")
		f.close()
	except:
		get_random_setting()
		mixer()
		rebuild()

		f = open("user.data", "w")
		f.close()


first_mixer()

