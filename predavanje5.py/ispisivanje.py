counter=0
def pprint(izraz):
    global counter
    counter+=1
    print ('[{}]>>>{}'.format(counter,izraz))

def print_upper(izraz):
    print(izraz.upper())

if __name__== '__main__':
    print('Ja san sada glavni modul za pokretanje !!!')
