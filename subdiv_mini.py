#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
SUBDIV MINI
-----------
Principe et fonctionnement

on divise le mot au milieu et met la première moitié à la fin
et si le nombre de lettres est impair,
la dernière moitié du mot reçoit le caractère supplémentaire.

C = Combinaision

"""

from configs.init import rolling


def milieu(char):
	"""
	abcd --> nombre de carcatères --> 4 --> 4/2 ---> 2
	"""
	return int(len(char)/2)


def C1(t):
	m = milieu(t)
	start = t[:m]
	middle = t[m:-1]
	end = t[-1]
	return middle+end+start

def C1_inv(t):
	m = milieu(t)
	start = t[m+1:]
	middle = t[:m]
	end = t[m]
	return start+middle+end



def C2(t):
	m = milieu(t)
	start = t[:m]
	end = t[m:]
	return end+start
	
def C2_inv(t):
	m = milieu(t)
	start = t[m:]
	end = t[:m]
	return start+end


def inverser_mot(word):
	n = len(word)
	
	if n == 1:
		return word
	elif n%2 == 0:
		return C2(word)
	else:
		return C1(word)


def remettre_mot(word):
	n = len(word)
	
	if n == 1:
		return word
	elif n%2 == 0:
		return C2_inv(word)
	else:
		return C1_inv(word)


def remettre_phrase(code):
	code = code.split(' ')
	msg = ''
	
	for word in code:
		msg = msg + remettre_mot(word) + ' '
	
	return msg[:-1]


def inverser_phrase(msg):
	msg = msg.split(' ')
	code = ''
	
	for word in msg:
		code = code + inverser_mot(word) + ' '
	
	return code[:-1]


def palm_1(msg):
	a1 = inverser_phrase(msg)
	a2 = inverser_mot(a1)
	a3 = inverser_phrase(a2)
	a4 = inverser_mot(a3)
	a5 = inverser_phrase(a4)
	a6 = inverser_mot(a5)
	a7 = inverser_phrase(a6)
	a8 = inverser_mot(a7)
	a9 = inverser_phrase(a8)
	a10 = inverser_mot(a9)

	return a10


def palm_1_rev(msg):
	a1 = remettre_mot(msg)
	a2 = remettre_phrase(a1)
	a3 = remettre_mot(a2)
	a4 = remettre_phrase(a3)
	a5 = remettre_mot(a4)
	a6 = remettre_phrase(a5)
	a7 = remettre_mot(a6)
	a8 = remettre_phrase(a7)
	a9 = remettre_mot(a8)
	a10 = remettre_phrase(a9)

	return a10


def palm_2(msg):
	for _ in range(rolling):
		msg = palm_1(msg)
	return msg


def palm_2_rev(msg):
	for _ in range(rolling):
		msg = palm_1_rev(msg)
	return msg

