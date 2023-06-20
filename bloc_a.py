#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	I) Bloc A
		Serie d'opération sur une chaine de caractère
		servant à modifier le text entré.
"""

from subdiv_mini import palm_2,palm_2_rev

def complexifier(plain_text):
	"""
		example:
			hello word ---> lrowd lleho
	"""

	plain_text =  plain_text[::-1]
	plain_text = palm_2(plain_text)
	plain_text = palm_2(plain_text)
	plain_text = palm_2(plain_text)

	return plain_text


def complexifier_inv(coded_text):
	""" 
		Remet le text dans le bon sens
		example:
			rowdl lehol ---> hello world
	"""

	coded_text = palm_2_rev(coded_text)
	coded_text = palm_2_rev(coded_text)
	coded_text = palm_2_rev(coded_text)
	coded_text =  coded_text[::-1]

	return coded_text

