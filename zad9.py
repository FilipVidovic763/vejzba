#Moj način

N=input('broj redaka')
N=int(N)
if N%2==0:
    broj_cigli=(9)*N/2
    broj_cigli=int(broj_cigli)
else :
    broj_cigli=4*N+(N+1)/2
print(int(broj_cigli))



#Drugi način

N=input('broj redaka')
N=int(N)

rez=(4*N+1+3*N)/2
print(int(rez))
