#dokumentarij aplikacija za ispis i unos novih studenata
#na kolegiju RPA
#Filip Vidović
from dokumentarijError import dokumentarijError

class Dokumentarij:
    def __init__(self):
        self.names=[]

    def display_title_bar(self):
        print("\t************************")
        print("\t*** Dokumentarij- RPA***")
        print("\t************************")

    def get_user_choice(self):
        #ispisujemo korisniku sta moze da radi u aplikaciji
        #na kraju uzimamo njegovo odabir te taj odabir vraćamo
        print("\n[1] Pogledaj listu studenata")
        print("[2] Dodaj novog studenta")
        print("[x] Izlaz iz aplikacije")

        return input("Što želite napraviti u dokumentariju?")

    def show_names(self):
        #prikazuje imena svih studenata dodanih u listi
        print("\n Ovo je popis studenata na kolegiju RPA 2019/2020:\n")
        for name in self.names:
            print(name.title())

    def get_new_name(self):
        #uzimamo kroz input od korisnika novo ime te ga dodajemo u listu ako to ime već nije u listi
        new_name=input("Unesite ime studenta:")
        if new_name in self.names:
            print("\n Ovaj student je već unešen u dokumentariju".format(new_name.title()))
        else:
            self.names.append(new_name)
            print("dobrodošao".format(new_name.title()))

    def play(self):
        choice=''
        self.display_title_bar()
        while choice!="x":
            choice= self.get_user_choice()
            self.display_title_bar()
            if choice=="1":
                self.show_names()
            elif choice=="2":
                self.get_new_name()
            elif choice=="x":
                print("Hvala na pregledavanju dokumentarija")
            else:
                raise dokumentarijError(101)  
            
if __name__=="__main__":
    game=Dokumentarij()
    game.play()






