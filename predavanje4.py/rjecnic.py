student1={'id':1234, 'ime':'Ivan','prezime': 'Ivi','ocjena':5}

keys=[k for k in student1.keys()]
print(keys)

del student1['ocjena']
print(student1)

student2={k:v for (k,v) in student1.items()}
student2

print(id(student1)==id(student2))

student2['status']='redovan'

print(student2)
