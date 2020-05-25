x=0
def inkrement(x):
    x+=1
    return x

print(x)
print(inkrement(x))
print(x)
x=inkrement(x)

lista=[1,2,3]
def inkrement_liste(l):
    for i in range(len(l)):
        l[i]+=1 

print (lista)
print(inkrement_liste(lista))
print(lista)