
bodovi_igrac1=int(0)
bodovi_igrac2=int(0)
igraj='da'


while igraj=='da':
    igrac1=input('igrač1 unesi k, s, p, L, sp: ')
    igrac2=input('igrač2 unesi k, s, L, sp: ')
    if igrac1=='p' and igrac2=='s':
        print('igrac2 pobijedio')
        bodovi_igrac2+=1
    elif igrac1=='p' and igrac2=='k':
        print('igrac1 pobijedio')
        bodovi_igrac1+=1
    elif igrac1=='p' and igrac2=='p':
        print('neriješeno')
    elif igrac1=='p' and igrac2=='sp':
        print('igrac1 pobijedio')
        bodovi_igrac1+=1
    elif igrac1=='p' and igrac2=='L':
        print('igrac2 je pobijedio')
        bodovi_igrac2+=1
    elif igrac1 =='s' and  igrac2=='s':
        print('neriješeno')
    elif igrac1=='s' and  igrac2=='p':
        print('igrac1 pobijedio')
        bodovi_igrac1+=1
    elif igrac1=='s' and igrac2=='k':   
        print('igrac2 pobijedio')
        bodovi_igrac2+=1
    elif igrac1=='s' and igrac2=='L':
        print('igrac1 pobijedio')
        bodovi_igrac1+=1
    elif igrac1=='s' and igrac2=='sp':
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
    elif igrac1=='k' and igrac2=='L':
        print('igrac1 je pobijedio')
        bodovi_igrac1+=1
    elif igrac1=='k' and igrac2=='sp':
        print('igrac2 je pbijedio')
        bodovi_igrac2+=1
    elif igrac1=='L' and igrac2=='p':
        print('igrac1 je pobijedio')
        bodovi_igrac1+=1
    elif igrac1=='L' and igrac2=='L':
        print('neriješeno')
    elif igrac1=='L' and igrac2=='s':
        print('igrac2 je pobijedio')
        bodovi_igrac2+=1
    elif igrac1=='L' and igrac2=='k':
        print('igrac2 je pobijedio')
        bodovi_igrac2+=1
    elif igrac1=='L' and igrac2=='sp':
        print('igrac1 je pobijedio')
        bodovi_igrac1+=1
    elif igrac1=='sp' and igrac2=='sp':
        print('neriješeno')
    elif igrac1=='sp' and igrac2=='s':
        print('igrac1 pobijedio')
        bodovi_igrac1+=1
    elif igrac1=='sp' and igrac2=='k':
        print('igrac1 pobijedio')
        bodovi_igrac1+=1
    elif igrac1=='sp' and igrac2=='p':
        print('igrac2 je pobijedio')
        bodovi_igrac2+=1
    elif igrac1=='sp' and igrac2=='L':
        print('igrac2 je pobijedio')
        bodovi_igrac2+=1

    else:
        print('greška')        

    print('igrač1 ima {} bodova'.format(bodovi_igrac1))        
    print('igrač2 ima {} bodova'.format(bodovi_igrac2))