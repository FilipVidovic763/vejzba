"""
aplikacija: Napad orkova v0.05
autor: Filip Vidović

"""


import random 
import textwrap
import sys


def naslov():
    ukras='-'
    sirina=72
    ukras=ukras*sirina
    poruka= """
        Hrabri vitez Talion vraća se iz boja i želi predahnuti u jednom seocetu. 
        U seocu se nalazi 5 kućica i želi stupiti u jednu od njih. 
        Hrabri vitez ne zna da u ovom području ima neprijatelja.
        Odluči se za jedna od vrata ...
    """
    print(ukras)
    print(poruka)
    print(ukras)

def misija():
    """ispisi glavnu misiju na ekranu"""
    print('Misija')
    print('\todaberi kućicu u kojoj se Talion može odmoriti')
    print('SAVJET:')
    print('pazi kako biraš, neprijatelji su u blizini')

def okupanti(idx,huts):
    """ispiši okupante kućica"""
    poruka=''
    for i in range(len(huts)):
        okupant_info="{}:{}".format(i+1, huts[i])
        if i + 1 == idx:
            okupant_info = "\033[1m" + okupant_info + "\033[0m"
        poruka += okupant_info + " "

    print(poruka)

def okupanti_kucica():
    """Nasumično napuni kućice okupantima"""
    kucice=[]
    okupanti=['neprijatelj','prijatelj','prazno']
    while len(kucice)<5:
        komp_odabir= random.choice(okupanti)
        kucice+=[komp_odabir]
    return kucice

def izbor_korisnika():
    """zaprimi broj korisnika"""
    poruka='odaberi broj od 1-5:'
    izbor_korisnika=input("\n" + poruka)
    idx = int(izbor_korisnika)
    return idx

def pokazi_zdravlje(health_meter, bold=False):
    """pokaži hit bodove prijatelja i neprijatelja"""
    poruka="Zdravlje: Talion: {}, neprijatelj: {}".format(health_meter['igrac'], health_meter['neprijatelj'])

    if bold:
        print(poruka)
    else:
        print(poruka)

def resetiraj_zdravlje_igraca(health_meter):
    """resetiraj zdravlje igrača"""
    health_meter['igrac'] = 40
    health_meter['neprijatelj'] = 40

def napad(health_meter):
    """algoritam za izračun napada"""
    hit_list=4*['igrac']+6*['neprijatelj']
    injured_unit = random.choice(hit_list)
    hit_points = health_meter[injured_unit]
    injury = random.randint(10, 15)
    health_meter[injured_unit] = max(hit_points - injury, 0)
    print("NAPAD! ", end='')
    pokazi_zdravlje(health_meter)

def igraj_igru(health_meter):
    """glavna kontrolna funkcija"""
    kucice=okupanti_kucica()
    idx=izbor_korisnika()
    okupanti(idx,kucice)

    if kucice[idx-1] != 'nepriatelj'
    










