import random
from zadatak6Error import pogodi_brojError

class pogodi_kartu:
    def __init__(self):
        self.igrac_odabir=None
        self.broj_rundi=0

    def get_user_choice(self):
        print("[1] Igraj igru:")
        print("[x] Izlaz")

        return input("to želite napraviti:")

    def igra(self):
        self.komp_odabir=random.randint(1,100)
        self.broj_rundi=0
        while True: 
            self.igrac_odabir=int(input("Unesite broj između 1 i 100: "))
            if self.igrac_odabir==self.komp_odabir:
                print("Čestitamo, pogodili ste broj")
                break
            elif self.igrac_odabir>self.komp_odabir:
                print("vaš unešeni broj je veći od zadanog, pokušajte ponovno")
            elif self.igrac_odabir<self.komp_odabir:
                print("Vaš uneseni broj je manji od traženog")
            else:
                raise pogodi_brojError(000)
            
            if self.broj_rundi==10:
                print("potrošili ste sve pokušaje, trazeni broj je: {}".format(self.komp_odabir))
                break
            self.broj_rundi+=1

    def play(self):
        choice=''
        while choice!='x':
            choice= self.get_user_choice()
            if choice=='1':
                self.igra()
            elif choice=='x':
                print("Hvala na igri")
            else:
                raise pogodi_brojError(101)


if __name__=="__main__":
    game=pogodi_kartu()
    game.play()