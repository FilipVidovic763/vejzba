import random

class Anjc:
    def __init__(self):
        self.SPIL={"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "0":10,
                    "Decko":10, "Dama":10, "Kralj":10, "Kec":1}

    def display_title_bar(self):
        print("\t*****************")
        print("\t*** Anjc-RPA ****")
        print("\t*****************")

    def get_user_choice(self):
        print("\n[1] igraj anjc")
        print("[x] Izlaz")
        return input("Odaberite što želite napravit")

    def player_input(self):
        while True:
            vuci=input("Želite li odabrati (V))uci ili (S)top").lower()
            if vuci in ("vuci", "v"):
                return False
            elif vuci in ("stop", "s"):
                return True
            else:
                print("Hvatanje izuzetaka")

    def start_game(self):
        deck= (["2", "3", "4", "5", "6","7", "8", "9", "0", "Decko", "Dama", "Kralj", "Kec"])*4
        random.shufle(deck)
        player= [deck.pop() for _ in range(1)]
        computer =[deck.pop() for _ in range(1)]

        while True:
            print("Igračeva ruka: {}".format(player))
            stop = self.player_input()
            if not stop:
                player.append(deck.pop())
                computer.append(deck.pop())

            else:
                player_total=sum(self.SPIL[card] for card in player)
                computer_total=sum(self.SPIL[card] for card in computer)
                if player_total >computer_total:
                    print("igrac pobjeđuje. Rezultat igrač {} vs Računalo {}".format(player_total, computer_total))
                else:
                    print("računalo pobjeđuje. Rezultati kompjuter {} vs igrač {}".format(computer_total, player_total))

            total=sum(self.SPIL[card] for card in player)  
            if total >21:
                print("Premašili ste rezultat, vaša ruka je {}".format(total))
                break
            elif total==21:
                print("Pobjeđujete, imate anjc,vaša ruka je {}".format(total))
                break
            elif stop:
                print("stali ste s igrom. Završeni rezultat je igrač {} vs računalo {}".format(total, sum(self.SPIL[card] for card in computer)))   
                break

    def play(self):
        choice = ''
        self.display_title_bar()
        while choice!= 'x':
            choice=self.get_user_choice()
            self.display_title_bar()
            if choice=='1':
                self.start_game()
            elif choice=='x':
                print("Hvala na igranju")
            else:
                print("Hvataj greške")
                
if __name__=='__main__':
    game=Anjc()
    game.play
