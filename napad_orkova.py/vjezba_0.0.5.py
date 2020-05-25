import random
import sys
import textwrap

def show_theme_message():
    
    print("Attack of The Orcs v0.0.5:")
    msg=(
        """
        Hrabri vitez Talion vraća se iz boja i želi predahnuti u jednom seocetu. 
        U seocu se nalazi 5 kućica i želi stupiti u jednu od njih. 
        Hrabri vitez ne zna da u ovom području ima neprijatelja.
        Odluči se za jedna od vrata ...
        """)

    print(msg)

def show_game_mission():
    print('Misija')
    print("Odaberi kućicu u kojoj se Tallion može odmoriti")
    print("SAVJET")
    print("Pazi kako biraš neprijatelji su u blizini")

def reveal_occupants(idx,huts):
    msg=""
    print('Otkivamo okupante')
    for i in range(len(huts)):
        occupant.info="{}:{}".format(i+1, huts[i])
        if i +1 == idx:
            occupant_info=occupant_info
        msg+=occupant_info+" "
    print(msg)

def occupy_huts():
    huts=[]
    occupants=["prijatelj", "nepriajtelj","preazno"]
    while len(huts)<5:
        computer_choice=random.choice(occupants)
    return huts

def process_user_choice():
    msg="Odaberi kućicu ua ulaz (1-5):"
    user_choice=input(msg)
    idx=int(user_choice)
    return idx


def show_health(health_meter, bold=False):
    msg="Zdravlje: Talion: {}, neprijatelj: {}".format(health_meter['igrac'], health_meter['neprijatelj'])

    if bold:
        print(msg)
    else:
        print(msg)

def reset_health_meter(health_meter):
    health_meter['igrac']=40
    health_meter['neprijatelj']=30

def attack(health_meter):
    hit_list=4*['igrac']+6*['neprijatelj']
    injured_unit=random.choice(hit_list)
    hit_points=health_meter[injured_unit]
    injury=random.randint(10,15)
    health_meter[injured_unit]=max(hit_points-injury,0)
    print("NAPAD")
    show_health(health_meter)

def play_game(health_meter):
    huts=occupy_huts()
    idx=process_user_choice()
    reveal_occupants(idx, huts)

    if huts[idx-1]!='neprijatelj':
        print("Čestitke! pobijedio si")
    else:
        print('Neprijatelj primjećen')
        show_health(health_meter)
        continue_attack=True


        while continue_attack:
            continue_attack=input("......nastavi napad? (d/n):")
            if continue_attack=='n':
                print("Bježim s stanjem zdravlja...")
                show_health(health_meter, bold=True)
                print("Kraj igre")
                break

            attack(health_meter)

            if health_meter['neprijatelj']<=0:
                print("neprijatelj je poržen, pobijedio si!")

            if health_meter['igrac']<=0:
                print("Izgubio si")
                break
           

def run_application():
    keep_playing='d'
    health_meter={}
    reset_health_meter(health_meter)
    show_game_mission()

    while keep_playing=='d':
        reset_health_meter(health_meter)
        play_game(health_meter)
        keep_playing=("Igrati opet? DA (d)/ NE(n):")



if __name__=='__main__':
    run_application()

        






