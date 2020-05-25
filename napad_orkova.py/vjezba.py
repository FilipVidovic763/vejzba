"""
igra orkova samostalna vježba
"""

import random

okupanti=['prijatelj', 'slobodno', 'neprijatelj']
igraj='da'
tekst="""
Vitez Talion se vraća iz bitke i traži sklonište u selu.
moraš pomoći Talionu pri odabiru kućice kako bi se odmorio.
ali moraš biti oprezan jer jedan pogrešan potez može značiti smrt
"""
print(tekst)
while igraj=='da':
    kucice=[]
    while len(kucice)<5:
        random_odabir=random.choice(okupanti)
        kucice+=[random_odabir]
    
    odluka=input('unesi broj od 1-5:')
    odluka=int(odluka)


    for i in range(len(kucice)):
        okupant_info=(i+1,kucice[i])
         

    if kucice[odluka-1]=='neprijatelj':
        print('izgubio si')
    else:
        print('pobijedio si')

    igraj=input('Igrati ponovno? DA ili NE:')

