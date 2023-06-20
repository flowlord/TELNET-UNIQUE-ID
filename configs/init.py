#!/usr/bin/env python
# -*- coding: utf-8 -*-

from string import ascii_lowercase,ascii_uppercase, ascii_letters, digits, punctuation
import json
import os.path

accent = 'ÄÀÂÉÈÊËÎÏÔÙÛÜÇàâéèêëîïôùûüç'

file = open('configs/setting.json', 'r')
data = json.load(file)
file.close()

carac_sub = data['cipher']

if data['cipher'] == 'ascii_lowercase':
	carac_sub = ascii_lowercase
elif data['cipher'] == 'ascii_uppercase':
	carac_sub = ascii_uppercase
elif data['cipher'] == 'ascii_letters':
	carac_sub = ascii_letters
else:
	raise Exception('uknown cipher option')


if data["cipher punctuation"] == True:
	carac_sub = carac_sub+ punctuation
if data["cipher space"] == True:
	carac_sub = carac_sub+ ' '
if data["cipher digits"] == True:
	carac_sub = carac_sub+ digits
if data["cipher accent"] == True:
	carac_sub = carac_sub+ accent

len_carac_sub = len(carac_sub)

name = data['substitue with']

if os.path.exists(name) is False:
	raise Exception('carac file name not found')


len_caractere = data['len_caractere']
longeur_carac_special = data['len_carac_special']
nombre_cle = data['nombre_cle']
mini,maxi = data['mini'],data['maxi']


groupe_caracteres_initial = "".join(open(name,'r',encoding='utf-8').readlines())
milieu = int(len(groupe_caracteres_initial)/2)
groupe_a = groupe_caracteres_initial[:milieu]
groupe_b = groupe_caracteres_initial[milieu:]

carac_special = 'esantirulodcp '

groupe_b = groupe_b+carac_sub*8000+carac_special*2000


rolling = data['rolling']





