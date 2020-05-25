kisa=input('unesi vjerovatnost kiše:')
kisa=float(kisa)
if kisa >= 0.0 and kisa <=0.5: 
    print('nema potrebe ponijet kišobran')   
elif kisa >=0.5 and kisa <=1: 
    print('ponesi kišobran')     
else:
    print('neispravna vrijednost') 




