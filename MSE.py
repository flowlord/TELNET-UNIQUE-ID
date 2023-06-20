#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
# Copyright 2019-2023 by Motion Kerling. All Rights Reserved.
#
# Permission to use, copy, modify, and distribute this software and its
# documentation for any purpose and without fee is hereby granted,
# provided that the above copyright notice appear in all copies and that
# both that copyright notice and this permission notice appear in
# supporting documentation, and that the name of Motion Kerling
# not be used in advertising or publicity pertaining to distribution
# of the software without specific, written prior permission.
# Motion Kerling DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE, INCLUDING
# ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL
# Motion Kerling BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR
# ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER
# IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT
# OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.


	███╗   ███╗  ██████╗ ███████╗
	████╗ ████║ ██╔════╝ ██╔════╝
	██╔████╔██║ ╚█████╗  █████╗
	██║╚██╔╝██║  ╚═══██╗ ██╔══╝
	██║ ╚═╝ ██║ ██████╔╝ ███████╗
	╚═╝     ╚═╝ ╚═════╝  ╚══════╝
	
	MSE (multiple substitution encryption)

	Créer le mardi 22 janvier 2019 à 01:10 

"""

__author__  = "Motion Kerling"
__version__ = "20.1.0"
__date__    = "20 JUIN 2023"

from random import randint
from pyperclip import copy

from bloc_a import complexifier,complexifier_inv
from bloc_b import cipher,decipher
from bloc_c import ajout_carac_b,enleve_carac_b

from configs.init import*


def mse_cipher(msg):
	"""
	MESSAGE --> |A| --> |B| -->|C| --> |D| --> |E| --> CODED MESSAGE
	"""
	a  = complexifier(msg)
	b = cipher(a)
	c  = complexifier(b)
	d = ajout_carac_b(c,randint(mini,maxi))
	e = cipher(d)
	
	copy(e)
	return e

