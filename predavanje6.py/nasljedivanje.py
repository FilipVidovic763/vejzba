class Parent: # definiraj roditeljsku klasu
    parentAttr = 100
    def __init__(self):
        print ("pozivam konstruktor roditelja")

    def parentMethod(self):
        print ('Zovem roditeljsku metodu')

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print ("Roditeljski atribut :", Parent.parentAttr)

class Child(Parent):
    def __init__(self):
        print('pozivam konstruktor')
    def childMethod(self):
        print('Pozivam metodu djeteta')


        
c = Child() # instanca djeteta
c.childMethod() # poziv metode od djeteta
c.parentMethod() # poziv metode od roditelja
c.setAttr(20) # pozivamo roditeljsku metodu
c.getAttr() # pozivamo roditeljsku metodu
print(issubclass(Child,Parent))
print(isinstance(c,Parent))
print(isinstance(c,Child))
