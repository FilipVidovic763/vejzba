def zbroji(x,y=3):
    return x+y
print(zbroji(2,3))

print(zbroji(2))

print(zbroji(y=3,x=2))

def mean (*podaci):
    sum=0
    for p in podaci:
        sum+=p
    return sum/len(podaci)

print(mean(1,4,3,8,7,5))
print(mean(7,9,1))