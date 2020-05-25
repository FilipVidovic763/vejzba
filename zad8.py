satnica=input('zarada po satu')
satnica=int(satnica)

A=input('broj dana rada Ante')
A=int(A)
J=input('broj dana rada Jurica')
J=int(J)
M=input('broj dana rada Miro')
M=int(M)

res=A*satnica*8+J*satnica*4+M*satnica*10
print(int(res))
