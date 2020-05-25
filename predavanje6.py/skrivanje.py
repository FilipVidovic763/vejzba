class Brojac:    
    __brojac = 0

    def broji(self):
        self._tekst = 'dodajem +1'
        self.__brojac += 1
        print(self.__brojac)

brojac = Brojac()
brojac.broji()
brojac.broji()
print(brojac._tekst)
print(brojac.__brojac)


