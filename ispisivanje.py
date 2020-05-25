counter=0
def pprint(izraz):
    global counter
    counter+=1
    print ('[{}]>>>{}'.format(counter,izraz))

def print_upper(izraz):
    print(izraz.upper())