# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 10:50:26 2018

@author: predavac
"""

#zadatak5

# Tražite od korisnika da unese neki
# broj te ispišite je li broj paran
# ili neparan.

br = input('Unesite broj: ')
br = int(br)

if br%2==0:
    print('Broj '+str(br)+' je paran.')
else:
    print('Broj',br,'je neparan.')