#Filip Vidović- prvi kolokvij
import random
from AnjcError import AnjcError
class Anjc:
    def __init__(self):
        self.player_karte=None
        self.komp_karte=None
        karta=["2","3","4","5","6","7","8","9","0","Decko","Dama","Kralj","As"]
        self.bodovi_igrac=0
        self.komp_bodovi=0
        
        

    def get_user_choice(self):
        print("[1]Igraj Anjc:")
        print("[x] izlaz")

        return input ("što želite napravit:")

    def karte(self):
        if karta=="2":
           self.karta_vrijednost=2
        elif karta=="3":
            self.karta_vrijednost=3
        elif karta=="4":
            self.karta_vrijednost=4
        elif karta=="5":
            self.karta_vrijednost=5
        elif karta=="6":
            self.karta_vrijednost=6
        elif karta=="7":
            self.karta_vrijednost=7
        elif karta=="8":
            self.karta_vrijednost=8
        elif karta=="9":
            self.karta_vrijednost=9
        elif karta=="0":
            self.karta_vrijednost=10
        elif karta=="Decko":
            self.karta_vrijednost=10
        elif karta=="Dama":
            self.karta_vrijednost=10
        elif karta=="Kralj":
            self.karta_vrijednost=10
        elif karta=="As":
            self.karta_vrijednost=1
        else:
            raise AnjcError(000)

        return self.karta_vrijednost

        

    def igra(self):
        self.player_karte=random.choice(self.karta_odabir)
        self.komp_karte=random.choice(self.karta_odabir)
        #kada ubacim da zbroji vrijednosti ruši mi se program, ne znam sad do čega je nisam imao vremena da nađem grešku
        self.player_input=input("unesite vuci ili stop:").lower()
        if self.player_input=="vuci":
            print("Igrac je dobio {}:".format(self.player_karte))
            print("komp je dobio {}:".format(self.komp_karte))
            
            self.bodovi_igrac+=self.karte(self.karta_vrijednost)
            self.komp_bodovi+=self.karte(self.karta_vrijednost)
            print(self.bodovi_igrac)
            print(self.komp_bodovi)
        elif self.player_input=="stop":
            print("Hvala na igri, konačni bodovi su:")
            print(self.bodovi_igrac)
            print(self.komp_bodovi)
        else:
            raise AnjcError(101)
        

    def play(self):
        choice=''
        while choice!="x":
            choice=self.get_user_choice()
            while self.bodovi_igrac<21 or self.komp_bodovi<21:
                if choice=="1":
                    self.igra()
                elif choice=="x":
                    print("Hvala na igri")
                else:
                    raise AnjcError(101)
                if self.bodovi_igrac>self.komp_bodovi:
                    print("česititamo igrač je pobijedio")
                elif self.bodovi_igrac<self.komp_bodovi:
                    print("Računalo je pobijedilo")

if __name__=="__main__":
    game=Anjc()
    game.play()


        







