import random


class Rulet:
    def __init__(self):
        self.money=100
        self.limit=5000

    def display_title_bar(self):
        print("\t*****************************************")
        print("\t*** Rulet- Razvoj poslovnih aplikacija***")
        print("\t*****************************************")

    def get_user_choice(self):
        print("[1] Igrati Rulet")
        print("[x] Izlaz")

        return input("Što želite napraviti:")

    def start_game(self):
        while self.money<=self.limit:
            print("Imate: {} kn.".format(self.money))
            if self.money<=0:
                print("Završili ste sa igrom")
                break
            bet_amount=int(input("Ulog:"))
            while bet_amount>self.money:
                print("\t Nemate dovoljno novca za takav ulog")
                bet_amount=int(input("Ulog:"))
            self.money=self.money - bet_amount
            bet =input("Na što želite uložiti?: [1] Broj ili [2] Boja")
            if bet=='1':
                final_bet=int(input("Odaberite broj na koji stavljate ulog (1-36)"))
                if 1<= final_bet <=36:
                    print("Rulet se pokreće...")
                    k= random.randint(1,37)
                    print("\n Kuglica na ruletu je na broju: {}".format(k))
                    if k ==final_bet:
                        print("čestitamo! Vaš ulog će se povećat za 20 puta")
                        self.money=self.money+bet_amount*20
                    else:
                        print("Izgubili ste, više sreće drugi put")
                else:
                    self.money=self.money+bet_amount
                    print("Hvatanje izuzetaka")
            elif bet=="2":
                final_bet=input("Na koju boju stavljate ulog? Upišite crna ili crvena:")
                if final_bet.lower()=="crna" or final_bet.lower()=="crvena":
                    print("Rulet se pokreće...")
                    k=random.choice(["crna", "crvena"])
                    print("\nKuglica je na boji: {}".format(k))
                    if k== final_bet:
                        print("Čestitamo, vaš ulog se povećao za dva puta")
                        self.money=self.money+bet_amount*2
                    else:
                        print("Izgubili ste, više sreće drugi put")
                else:
                    self.money = self.money + bet_amount
                    print("Hvatanje izuzetaka")
            else:
                self.money=self.money + bet_amount
                print("Hvatanje izuzetaka")

    def play(self):
        choice=''
        while choice !='x':
            self.display_title_bar()
            choice=self.get_user_choice()
            if choice=='1':
                self.start_game()
            elif choice=='x':
                print("Hvala na igranju. Pozdrav")
            else:
                print("hvatanje izuzetaka")


if __name__=='__main__':
    game=Rulet()
    game.play()

