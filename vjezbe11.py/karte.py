# karte od keca do kralja sa 4 boje
# računalo izvlači jednu kartu i izvukli ste sada kartu broj 5 i vi sada kažete viša ili manja


import  random

class Karte:
    def __init__(self):
        self.ranks=["Kec", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Decko", "Dama", "Kralj"]
        self.suits=["Tref", "Srce", "Karo", "Pik"]
        self.deck=[]
        value=1
        for rank in self.ranks:
            for suit in self.suits:
                self.deck.append([rank+ "iz"+ suit + "boje" ,value ])
            value=value+1

        random.shuffle(self.deck)
        self.score=0
        self.card01=self.deck.pop(0)

    def  display_title_bar(self):
        print("\t********************************")
        print("\t****kartaška igra--izvlačenje***")
        print("\t********************************")

    def get_user_choice(self):
        print("[1] pokreni kartašku igru")
        print("[x] Izlaz")

        return input("što želite napraviti:")


    def start_game(self):
        while True:
            print("vas trenutni rezultat {}:".format(self.score))
            print("\nvaša trenutna karta je {}:".format(self.card01[0]))
            while True:
                choice=input("(v)iša ili (n)iža karta: ")
                if choice[0].lower() in ["v", "n"]:# ako je prvo slov v ili n izlazi iz ove while petlje i nastavljas
                    break
            self.card02=self.deck.pop(0)
            print("sljedeće odabrana karta je {}:".format(self.card02))
            # vi sada trebate vidjet jeli korisnik upisao v ili n
            # te ovisno o upisu v ili n usporediti i reći i ispisat pogodak i nastaviti
            #ako je pogodak, igra se nastavlja i rezultat pogođenih karata je kumulitativno povećava u
            # u varijabli score,
            #ako nije izaći iz petlje i završiti igru
           
            if choice[0].lower()=="v" and self.card02[1]>self.card01[1]:
                print("pogodili ste")
                self.score=self.score+1
            elif choice[0].lower()=="v" and self.card02[1]<self.card01[1]:
                print ("promašili ste i vaš konačan rezultat je {}".format(self.score))
            elif choice[0].lower()=="v" and self.card02[1]==self.card01[1]:
                print("nerijeeno je, odaberite drugi broj")

            elif choice[0].lower()=="n" and self.card02[1]<self.card01[1]:
                print("pogodili ste")
                self.score=self.score+1
            elif choice[0].lower()=="n" and self.card02[1]>self.card01[1]:
                print ("promašili ste i vaš konačan rezultat je {}".format(self.score))
                break
            elif choice[0].lower()=="n" and self.card02[1]==self.card01[1]:
                print("nerijeeno je, odaberite drugi broj")

            
                
            

            self.card01=self.card02

            #if choice[0].lower=='(n)iža':
                #if self.card02<self.card01:
                   # print("pogodili ste")
                   # self.score+=1
                

               # elif self.card02>self.card01:
                   # print("promašili ste")
                   # break

            



    def play(self):
        choice=''
        self.display_title_bar
        while choice!='x':
            choice= self.get_user_choice()
            self.display_title_bar
            if choice=='1':
                self.start_game()
            elif choice=='x':
                print("Hvala na igri")
            else:
                print("Hvatanje izuzetaka")

if __name__=="__main__":
    game=Karte()
    game.play()
