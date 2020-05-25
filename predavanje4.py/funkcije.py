def apsolutna_vrijednost(x):
    """ova funkcija vraca apsolutnu vrijednost broja """
    if x<0:
        return -x
    else:
        return x

print(help(apsolutna_vrijednost))
x,y = -5,3
print(apsolutna_vrijednost(x))
print(apsolutna_vrijednost(y))

