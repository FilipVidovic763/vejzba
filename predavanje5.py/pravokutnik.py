class Pravokutnik:
    """PYthon klasa za opis pravokutnika"""
    counter=0

    def __init__(self,a,b):
        """konstruktor klase"""
        self.a, self.b = a,b
        Pravokutnik.counter+=1


    def opseg(self):
        """metoda racuna opsega pravokutnika"""
        return 2*(self.a+self.b)

    def povrsina(self):
        """metoda racuna povrsinu pravokutinika"""
        return self.a*self.b 



if __name__ == '__main__':
    #instanciranje objekta 1
    p1= Pravokutnik(3,4)
    print(p1.opseg())
    print(p1.povrsina())

    p2= Pravokutnik(2,5)
    print(p2.opseg())
    print(p2.povrsina())

    print('Imamo ukupno {} pravokutnika'.format(p1.counter))
