
bodovi_igrac1=int(0)
bodovi_igrac2=int(0)
igraj='da'

while igraj=='da':
    igrac1=input('igrač1 unesi k, s ili p: ')
    igrac2=input('igrač2 unesi k, s ili p: ')
    if igrac1=='p' and igrac2=='s':
        print('igrac2 pobijedio')
        bodovi_igrac2+=1
    elif igrac1=='p' and igrac2=='k':
        print('igrac1 pobijedio')
        bodovi_igrac1+=1
    elif igrac1=='p' and igrac2=='p':
        print('neriješeno')
    elif igrac1 =='s' and  igrac2=='s':
        print('neriješeno')
    elif igrac1=='s' and  igrac2=='p':
        print('igrac1 pobijedio')
        bodovi_igrac1+=1
    elif igrac1=='s' and igrac2=='k':   
        print('igrac2 pobijedio')
        bodovi_igrac2+=1
    elif igrac1=='k' and igrac2=='k':
        print('nerijšeno')
    elif igrac1=='k' and igrac2=='p':
        print('igrac2 pobijedio')
        bodovi_igrac2+=1
    elif igrac1=='k' and igrac2=='s':
        print('igrac1 pobijedio')
        bodovi_igrac1+=1
    else:
        print('greška')        

    print('igrač1 ima {} bodova'.format(bodovi_igrac1))        
    print('igrač2 ima {} bodova'.format(bodovi_igrac2))


