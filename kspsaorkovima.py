izbori=['k', 's', 'p']
import random
bodovi_igrac=int(0)
bodovi_komp=int(0)
igraj='Da'


while igraj=='Da':
    igrac=input('Talion unesi k, p, s: ')
    komp_odabir= random.choice (izbori)
    

    if igrac=='p' and komp_odabir=='s':
        print('komp_odabir pobijedio') 
        bodovi_komp+=1    
    elif igrac=='p' and komp_odabir=='k':
        print('igrac pobijedio')   
        bodovi_igrac+=1
    elif igrac=='p' and komp_odabir=='p':
        print('neriješeno')
    elif igrac =='s' and  komp_odabir=='s':
        print('neriješeno')
    elif igrac=='s' and  komp_odabir=='p':
        print('igrac pobijedio')
        bodovi_igrac+=1
    elif igrac=='s' and komp_odabir=='k':   
        print('komp_odabir pobijedio')
        bodovi_komp+=1
    elif igrac=='k' and komp_odabir=='k':
        print('nerijšeno')
    elif igrac=='k' and komp_odabir=='p':
        print('komp_odabir pobijedio')
        bodovi_komp+=1
    elif igrac=='k' and komp_odabir=='s':
        print('igrac pobijedio') 
        bodovi_igrac+=1  
    else:
        print('greška')

    print('Talion ima {} bodova'.format(bodovi_igrac)) 
    print('Ork ima {} bodova'.format(bodovi_komp))    