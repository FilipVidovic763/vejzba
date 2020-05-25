# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 11:08:13 2018

@author: predavac
"""

#zadatak7

# Napravite igru kamen, papir, škare.
# Prvo igrač1 unese što želi,
# zatim igrač2 unese što želi i tada
# ispišete poruku tko pobjeđuje.
# Ako se unese nešto što nije kamen,
# papir ili škare, treba ispisati
# poruku da to nije valjan izbor.

i1 = input('Unesite K, S ili P: ')
i2 = input('Unesite K, S ili P: ')

i1 = i1.lower()
i2 = i2.lower()

#prvo provjerimo imamo li valjane unose
if (i1!='k' and i1!='s' and i1!='p'):
    print('Igrač1 nije napravio valjan izbor, unio je:',i1)
elif (i2!='k' and i2!='s' and i2!='p'):
    print('Igrač2 nije napravio valjan izbor, unio je:',i2)
elif i1=='k':
    if i2=='k':
        print('Neriješeno.')
    elif i2=='p':
        print('Igrač2 je pobijedio (p>k).')
    else:
        print('Igrač1 je pobijedio (k>s).')
elif i1=='p':
    if i2=='p':
        print('Neriješeno.')
    elif i2=='k':
        print('Igrač1 je pobijedio (p>k).')
    else:
        print('Igrač2 je pobijedio (s>p).')
else:
    if i2=='s':
        print('Neriješeno.')
    elif i2=='p':
        print('Igrač1 je pobijedio (s>p).')
    else:
        print('Igrač2 je pobijedio (k>s).')