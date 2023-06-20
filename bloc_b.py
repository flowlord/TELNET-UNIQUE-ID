#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
	II) Bloc B
		Chaque carcatère est substituer.
"""

from configs.init import*
from random import choice,randint
import os

if os.path.exists("keylib.keys"):
	listkey = open('keylib.keys','r',encoding="utf-8").readlines()
else:
	from generateur_cle import gen_lib_cle
	gen_lib_cle(randint(nombre_cle[0],nombre_cle[1]))
	listkey = open('keylib.keys','r',encoding="utf-8").readlines()


class caracNotInList(Exception):
	"""
	lève une erreur si un caractères n'est pas dans la variable carac_sub.
	
	Attributes:
		carac -- le caractères qui peut causer une erreur
		message -- explication de l'erreur
	
	"""
	def __init__(self, carac,message="un caractère n'est pas dans la variable des caractères à substituer"):
		self.carac = carac
		self.message = message
		super().__init__(self.message)
	
	def __str__(self):
		return f"le caractère: {self.carac} n'est pas dans la variable carac_sub."


def verifier_carac(text):
	"""
	Vérifie tous les caractères d'un text et
	lève une erreur si un caractères n'est pas dans la variable carac_sub.
	"""
	
	for c in text:
		if c not in carac_sub:
			raise caracNotInList(c)


def cipher(plain_text):
	"""
	Je prend une clé au hazard et substitue les caractères
	
	exemple: a ---> 57$2^P-
	"""
	
	#verifier_carac(plain_text)
	
	key = choice(listkey).split(' ')
	key = [element.replace('\n','') for element in key]

	for n in range(len_carac_sub):
		plain_text = plain_text.replace(carac_sub[n],key[n])
		
	return plain_text


def decipher(coded_msg):
	"""
	Déchiffre un message codé.
	"""
   
	for key in listkey:
	
		key = key.split(' ')
		key = [e.replace('\n','') for e in key]
 
		for n in range(len_carac_sub):
			coded_msg = coded_msg.replace(key[n],carac_sub[n])
	
	return coded_msg


