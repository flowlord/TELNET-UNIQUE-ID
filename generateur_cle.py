#!/usr/bin/env python
# coding: utf-8

"""
librairie de clé = keylib
fichier qui contient plusieurs clé de chiffrement

Reprend une partie du code source du logiciel GENESIS KEY © qui,
dans une sombre époque du projet était un logiciel payant ;)
"""

from random import randint,choice
from configs.init import*

def gen_caractere(x):
	"""
	générateur de groupe de carcatère
	(comme un générateur de mot de passe)
	"""
	carac = ''
	for _ in range(x):
		carac = carac+choice(groupe_a)
	return carac


def gen_cle(len_carac_sub):
	"""
	Génère une clé de substitution avec une longeur choisit

	Exemple:

		| ID | TUYSQ | ZEOD | UTT | UZU | FRYS | RZ | EWQ | PMZWK |
		-----------------------------------------------------------
		| a  | b     | c    | d	  | e	| f	   | g  | h   | i     |
		
	"""

	cle = ''

	for carac in range(len_carac_sub):

		long_carac = randint(len_caractere[0],len_caractere[1])
		long_carac_spe = randint(longeur_carac_special[0],longeur_carac_special[1])
				
		if carac_sub[carac] in carac_special:
			cle = cle + f'{gen_caractere(long_carac_spe)} '
		cle = cle + f'{gen_caractere(long_carac)} '

	return cle[:-1]
   
   
def gen_lib_cle(nombre_cle):
	"""
	Génère une librairie de clé
	"""

	file = open('keylib.keys','w',encoding='utf-8')
	
	for number in range(nombre_cle):
		file.write(f'{gen_cle(len_carac_sub)}\n')

	file.close()







