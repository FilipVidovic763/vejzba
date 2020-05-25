class Car:
    """Definiramo klasu koja predstvalja auto"""
    motor = True
def __init__(self):
    """funkcija koja se poziva prilikom instancijacije objekta"""
    print('stvoreni auto')
    self.fuel=0
    self.speed=0
def refuel(self,fuel):
    """postavi količinu goriva"""
    self.fuel= fuel

def setSpeed(self,speed):
    """postavi brinu vozila"""
    self.speed=speed 

def getSpeed(self):
    """daj brzinu vozila"""
    return self.speed

# prvi objekt
audi = Car()
audi.setSpeed(10)
# drugi objekt
nissan = Car()
nissan.setSpeed(20)
print('Audi vozi {}km/h brzinom'.format(audi.setSpeed()))
print('Nissan vozi {}km/h brzinom'.format(nissan.setSpeed()))
# pristup varijabli klase
print(audi.motor)
print(nissan.motor)
# promjena varijabla klase
Car.motor = False
# varijabla klase
print(audi.motor)
print(nissan.motor)

