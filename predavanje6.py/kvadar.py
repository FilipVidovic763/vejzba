class Cetverokut:
    def __init__(self,a,b,c,d):
        self.a, self.b, self.c, self.d = a,b,c,d

    def opseg(self):
        return self.a+self.b+self.c+self.d
    
class Pravokutnik(Cetverokut):
    def __init__(self,a,b):
        Cetverokut.__init__(self,a,b,a,b)

    def povrsina(self):
        return self.a*self.b

    
class Kvadar(Pravokutnik):
    def __init__(self,a,b,h):
        self.h = h
        Pravokutnik.__init__(self,a,b)       
      
   
    def povrsina(self):
        return 2*self.a*self.b + 2*self.a*self.h+2*self.b*self.h

    def volumen(self):
        return self.povrsina() * self.h

if __name__ == '__main__':
    pravokutnik = Pravokutnik(2,3)
    print('opseg: {} povrsina: {}'.format(pravokutnik.opseg(),pravokutnik.povrsina()))

    kvadar = Kvadar(2,3,5)      
    print('povrsina: {} volumen: {}'.format(kvadar.povrsina(),kvadar.volumen()))

  








    

    

