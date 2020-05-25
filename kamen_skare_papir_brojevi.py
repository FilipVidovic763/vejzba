#FIlip Vidović
#kamen-0
#škare-1
#papir-2
#(igrac1-igrac2) igrac1 pobjeđuje kod 1.... igrac2 pobjeđuje kod 2, neriješeno ako je 0

from kspkerror import kspkerror
class kspbrojevi:
    def __init__(self):
        self.igrac1_input=None
        self.igrac1_number=-3
        self.igrac2_input=None
        self.igrac2_number=-3


    def string_u_broj_igrac1(self):
        if self.igrac1_input=="kamen":
            self.igrac1_number=0
        elif self.igrac1_input=="škare":
            self.igrac1_number=1
        elif self.igrac1_input=="papir":
            self.igrac1_number=2
        else: 
            self.igrac1_number=-1
            raise kspkerror(101)
        return self.igrac1_number

    def string_u_broj_igrac2(self):
        if self.igrac2_input=="kamen":
            self.igrac2_number=0
        elif self.igrac2_input=="škare":
            self.igrac2_number=1
        elif self.igrac2_input=="papir":
            self.igrac2_number=2
        else: 
            self.igrac2_number=-3
            raise kspkerror(102)
        return self.igrac2_number

    def play(self):
        self.igrac1_input=input("Igrac 1 unesite kamen, škare, papir: ").lower()
        self.igrac1_number=self.string_u_broj_igrac1()

        self.igrac2_input=input("Igrac 2 unesite kamen, škare, papir: ").lower()
        self.igrac2_number=self.string_u_broj_igrac2()
        ostatak=(self.igrac1_number - self.igrac2_number)
        
        if self.igrac1_number== -3 :
            raise kspkerror(103)
        else:
            if ostatak== 0 :
                print("Neriješeno")
            if ostatak ==-1 or ostatak==2:
                print("Igrac1 pobijedio")
            if ostatak==-2 or ostatak==1:
                print("igrac2 pobijedio")
        print("Igrac1 je odabrao {}".format(self.igrac1_input.title()))
        print("Igrac2 je odabrao {}".format(self.igrac2_input.title()))
        

if __name__ == "__main__":
    game =kspbrojevi()
    game.play()

