#Satnica
S,A,J,M = input('Unesite iznos satnice i dane za Antu, Juricu i Miru (redoslijedno): ').split(',', 4)
S = int(S)
A = int(A)
J = int(J)
M = int(M)

rj = ((A*8)+(J*4)+(M*10))*S

print("Ukupno su zaradili {} kuna".format(int(rj)))