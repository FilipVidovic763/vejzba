# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 10:58:11 2018

@author: predavac
"""

#zadatak6

# Tražite od korisnika da unese 
# vjerojatnost kiše za sutrašnji
# dan. U ovisnosti o vjerojatnosti
# ispišite odgovarajuću poruku:
# Ako je vjerojatnost veća ili jednaka
# 0.5 tada treba ponijeti kišobran,
# u suprotnom ne treba.
# Ispišite i upozorenje ako se unese
# negativna vjerojatnost ili vjerojatnost
# veća od 1.

vjerojatnost = input\
('Unesite vjerojatnost kiše:')
vjerojatnost = float(vjerojatnost)

if (0<=vjerojatnost<0.5):
    print('Ne treba ponijeti kišobran.')
elif (0.5<=vjerojatnost<=1):
    print('Trebate ponijeti kišobran.')
else:
    print('Niste unijeli valjanu vjerojatnost.')