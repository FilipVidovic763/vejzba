

import random
import textwrap
import sys



def show_theme_message(width):
    """Print the game theme in the terminal window"""
    print_dotted_line()
    print_bold("Attack of The Orcs v0.0.5:")
    msg = (
        """
        Hrabri vitez Talion vraća se iz boja i želi predahnuti u jednom seocetu. 
        U seocu se nalazi 5 kućica i želi stupiti u jednu od njih. 
        Hrabri vitez ne zna da u ovom području ima neprijatelja.
        Odluči se za jedna od vrata ...
        """)

    print(textwrap.fill(msg, width=width))


def show_game_mission():
    """Ispisi glavnu misiju na ekran terminala"""
    print_bold("Misija:")
    print("\tOdaberi kućicu u kojoj se Talion može odmoriti ...")
    print_bold("SAVJET:")
    print("PAZI kako biraš jer neprijatelji su blizu!")
    print_dotted_line()


def reveal_occupants(idx, huts):
    """ispisi okupanta kucice """
    msg = ""
    print("Otkrivam okupanta...")
    for i in range(len(huts)):
        occupant_info = "{}:{}".format(i+1, huts[i])
        if i + 1 == idx:
            occupant_info = "\033[1m" + occupant_info + "\033[0m"
        msg += occupant_info + " "

    print("\t" + msg)
    print_dotted_line()


def occupy_huts():
    """Nasumično napuni kućice s okupantima"""
    huts = []
    occupants = ['neprijatelj', 'prijatelj', 'slobodno']
    while len(huts) < 5:
        computer_choice = random.choice(occupants)
        huts.append(computer_choice)
    return huts


def process_user_choice():
    """zaprimi broj od korisnika"""
    msg = "\033[1m" + "Odaberi kućicu za ulaz (1-5): " + "\033[0m"
    user_choice = input("\n" + msg)
    idx = int(user_choice)
    return idx


def show_health(health_meter, bold=False):
    """pokaži hit bodove prijatelja i neprijatelja"""
    msg = "Zdravlje: Talion: {}, neprijatelj: {}".format(health_meter['igrac'], health_meter['neprijatelj'])

    if bold:
        print_bold(msg)
    else:
        print(msg)


def reset_health_meter(health_meter):
    """resetiraj vrijednosti rjecnika na početne"""
    health_meter['igrac'] = 40
    health_meter['neprijatelj'] = 30


def print_bold(msg, end='\n'):
    """napravi tekst masno otisnut"""
    print("\033[1m" + msg + "\033[0m", end=end)


def print_dotted_line(width=72):
    """ispiši točkastu liniju"""
    print('-'*width)

def attack(health_meter):
    """algoritam za utvrdjivanje stete"""
    hit_list = 4 * ['igrac'] + 6 * ['neprijatelj']
    injured_unit = random.choice(hit_list)
    hit_points = health_meter[injured_unit]
    injury = random.randint(10, 15)
    health_meter[injured_unit] = max(hit_points - injury, 0)
    print("NAPAD! ", end='')
    show_health(health_meter)


def play_game(health_meter):
    """Glavna kontrolna fukcija za pokretanje igre"""
    huts = occupy_huts()
    idx = process_user_choice()
    reveal_occupants(idx, huts)

    if huts[idx - 1] != 'neprijatelj':
        print_bold("Čestitke! POBIJEDIO SI!!!")
    else:
        print_bold('neprijatelj PRIMJEĆEN! ', end='')
        show_health(health_meter, bold=True)
        continue_attack = True

        # Ponavljaj dok korisnik zeli i dalje napadati
        while continue_attack:
            continue_attack = input(".......nastavi napad? (d/n): ")
            if continue_attack == 'n':
                print_bold("BJEŽIM s stanjem zdravlja ...")
                show_health(health_meter, bold=True)
                print_bold("KRAJ IGRE!")
                break

            attack(health_meter)

            # provjeri je li netko boraca poginuo
            if health_meter['neprijatelj'] <= 0:
                print_bold("neprijatelj poražen! POBIJEDIO SI!!!")
                break

            if health_meter['igrac'] <= 0:
                print_bold("IZGUBIO SI  :(  više sreće sljedeći puta")
                break


def run_application():
    """glavna kontrola aplikacije"""
    keep_playing = 'd'
    health_meter = {}
    reset_health_meter(health_meter)
    show_game_mission()

    while keep_playing == 'd':
        reset_health_meter(health_meter)
        play_game(health_meter)
        keep_playing = input("\nIgrati ponovno? Da(d)/Ne(n): ")



if __name__ == '__main__': # ovaj dio objasnjavamo na predavanju slijedeći puta
    run_application()

