import random

lista=[random.randrange(1,100) for i in range(7)]

print(lista)

manji_od_50= [x for x in lista if x<=50]

print(manji_od_50)
