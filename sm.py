class Car:
    """definiramo klasu koja predstavlja auto"""
# varijable klase
motor = True
# konstruktor
def __init__(self):
    """funkcija koja se poziva prilikom instancijacije objekta"""
    print('stvoren auto!')
    self.fuel = 0
    self.speed = 0
# metoda
def refuel(self,fuel):
    """postavi količinu goriva"""
    self.fuel = fuel
def setSpeed(self,speed):
    """postavi brzinu vozila"""
    self.speed = speed
def getSpeed(self):
    """"daj brzinu vozila"""
    return self.speed

