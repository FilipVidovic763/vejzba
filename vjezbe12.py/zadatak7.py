import random

class kartaska_igra:
    def __init__(self):
        self.player_karte=None
        self.komp_karte=None
        self.karta_odabir=["2","3","4","5","6","7","8","9","0","Decko","Dama","Kralj","As"]
        self.bodovi_igrac=0
        self.komp_bodovi=0
        self.broj_rundi=0

    def get_user_choice(self):
        print("[1]Igraj kartašku igru:")
        print("[x] izlaz")

        return input ("što želite napravit:")

    def kartePlayer(self):
        if self.player_karte=="2":
           self.karta_vrijednost=2
        elif self.player_karte=="3":
            self.karta_vrijednost=3
        elif self.player_karte=="4":
            self.karta_vrijednost=4
        elif self.player_karte=="5":
            self.karta_vrijednost=5
        elif self.player_karte=="6":
            self.karta_vrijednost=6
        elif self.player_karte=="7":
            self.karta_vrijednost=7
        elif self.player_karte=="8":
            self.karta_vrijednost=8
        elif self.player_karte=="9":
            self.karta_vrijednost=9
        elif self.player_karte=="0":
            self.karta_vrijednost=10
        elif self.player_karte=="Decko":
            self.karta_vrijednost=10
        elif self.player_karte=="Dama":
            self.karta_vrijednost=10
        elif self.player_karte=="Kralj":
            self.karta_vrijednost=10
        elif self.player_karte=="As":
            self.karta_vrijednost=1
        
            
        
    def karteRacunalo(self):
        if self.komp_karte=="2":
           self.karta_vrijednost=2
        elif self.komp_karte=="3":
            self.karta_vrijednost=3
        elif self.komp_karte=="4":
            self.karta_vrijednost=4
        elif self.komp_karte=="5":
            self.karta_vrijednost=5
        elif self.komp_karte=="6":
            self.karta_vrijednost=6
        elif self.komp_karte=="7":
            self.karta_vrijednost=7
        elif self.komp_karte=="8":
            self.karta_vrijednost=8
        elif self.komp_karte=="9":
            self.karta_vrijednost=9
        elif self.komp_karte=="0":
            self.karta_vrijednost=10
        elif self.komp_karte=="Decko":
            self.karta_vrijednost=10
        elif self.komp_karte=="Dama":
            self.karta_vrijednost=10
        elif self.komp_karte=="Kralj":
            self.karta_vrijednost=10
        elif self.komp_karte=="As":
            self.karta_vrijednost=1
        

    def igra(self):
        deck = (['2', '3', '4', '5', '6', '7', '8', '9', '0', 'Decko', 'Dama', 'Kralj', 'Kec'])*4
        random.shuffle(deck)
        player = [deck.pop() for _ in range(2)] 
        computer = [deck.pop() for _ in range(2)]
        self.broj_rudni=0
        while True:
            print("Igračeva (Vaša) ruka: {}".format(player))
            stop = self.player_input()
            if not stop and self.broj_rundi<=3:
                player.append(deck.pop())
                computer.append(deck.pop())
                self.broj_rundi+=1
                player_total = sum(self.SPIL[card] for card in player)
                computer_total = sum(self.SPIL[card] for card in computer)
        else:
            if player_total > computer_total:
                print("Igrač pobjeđuje. Rezultat Igrač {} vs. Računalo {}".format(player_total, computer_total))
            else:
                print("Računalo pobjeđuje. Rezultat: Računalo {} vs. Igrač {}".format(computer_total, player_total))

    def play(self):
        
        choice = ''
        
        while choice != 'x':
            choice = self.get_user_choice()
            
            if choice == '1':
                self.igra()
            elif choice == 'x':
                print("\nHvala na igranju Anjca. Pozdrav!")
            else:
                print("Hvatanje IZUZETKA")

        
if __name__ == '__main__':
    game = kartaska_igra()
    game.play()
            