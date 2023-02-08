from module1 import *


palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","A"]
while True:
    print(inimesed)
    print(palgad)
    menu=int(input("Valik:\n 1-Lisa andmed\n2-Kustuta andmed\n3-Suurim palk\n4-Luhim palk\n5-Palka uhtlustamine\n6-Palgade dublikatid"))
    if menu==0:
        break
    elif menu==1:
        inimesed,palgad=lisa_andmed(inimesed,palgad)
        print(inimesed)
        print(palgad)
    elif menu==2:
        inimesed,palgad=kustutamine(inimesed,palgad)
        print(inimesed)
        print(palgad)
    elif menu==3:
        palk,nimi=suurim_palk(inimesed,palgad)
        print(f"Suurim palk on {palk} {nimi}")
    elif menu==4:
        palk,nimi=luhim_palk(inimesed,palgad)
        print(f"Luhim palk on {palk} {nimi}")
    elif menu==5:
        inimesed,palgad=uhtlustamine(inimesed,palgad)
        print(inimesed)
        print(palgad)
    elif menu==6:
        inimesed,palgad=dublikatid


