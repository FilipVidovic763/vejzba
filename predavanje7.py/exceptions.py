# iznimke

def rijesi():
    a = int(input("Unesite broj za 'a': "))
    assert a > 0 # provjeri je li a > 0
    if a==10: raise ValueError('10 ne dopuštamo')

    print('Uneseni broj je OK!')
    d = x+a
    e = 2*d

if __name__ == '__main__':
    try:    
        rijesi()
    except NameError as e: # greska varijable x        
        print('Postoji varijabla koja nije inicirana',e.args)
    except AssertionError:
        print('vrijednost nije veća od 0')
        return
    finally:
        print('Izvrsi unatoc svemu')

