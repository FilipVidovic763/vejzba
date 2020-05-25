class Parent:        # define parent class
   def myMethod(self):
      print ('Pozivam roditeljsku metodu')

class Child(Parent): # define child class
   def myMethod(self):
      print ('Pozivam metodu djeteta')

c = Child()          # instanca klase dijete
c.myMethod()         # dijete poziva metodu djeteta ne roditelja jer je predefinirana


class Razlomak:
    def __init__(self,a,b):
        self.a, self.b = a,b

    def __str__(self):
        return '{}/{}'.format(self.a,self.b)

    def __add__(self,drugi):
        return Razlomak(self.a*drugi.b+self.b*drugi.a,self.b*drugi.b)

q1 = Razlomak(1,2)
q2 = Razlomak(1,3)

q = q1 + q2
print(q)

