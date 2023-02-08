def lisa_andmed(i:list,p:list):
    """Kirlejdus
    :param list i: Inimeste järjend
    :param list p: Palgade järjend
    :rtype: list, list
    """
    n=int(input("Mitu inimest: "))
    for j in range(n):
        nimi=input("Sisesta nimi: ")
        palk=int(input("Sisesta palk: "))
        i.append(nimi)
        p.append(palk)
    return i,p

def kustutamine(i:list,p:list):
    """Inimesed ja palk eemaldatakse välja
    :param list i: Inimeste järjend
    :param list p: Inimeste järjend
    :rtype: list, list
    """
    nimi=input("Sisesta nimi: ")
    if nimi in i:
        n=i.count(nimi)
        for j in range(n):
            ind=i.index(nimi)
            i.pop(ind)
            p.pop(ind)

    return i,p


def suurim_palk(i:list,p:list):
    """Kõige suurem palk ja kes seda saab
    :param list i: Inimeste järjend
    :param list p: Inimeste järjend
    :rtype: int, str
    """
    palk=max(p)
    ind=p.index(palk)
    nimi=i[ind]

    return palk, nimi

def luhim_palk(i:list,p:list):
    """Kõige luhim palk ja kes seda saab
    :param list i: Inimeste järjend
    :param list p: Inimeste järjend
    :rtype: int, str
    """
    palk=min(p)
    ind=p.index(palk)
    nimi=i[ind]
    return palk, nimi


def uhtlustamine(i:list,p:list):
    """Palkade järjestamine kasvavas ja kahanevas järjekorras koos nimedega
    :param list i: Inimeste järjend
    :param list p: Inimeste järjend
    rtype: int, str
    """
    v=int(input("1-kahaneb, 2-kasvab?"))
    if v==1:
        n=len(p)
        for j in range(0,n-1):
             for k in range(j+1,n):
                 if p[j]>p[k]:
                     abi=p[j] 
                     p[j]=p[k] 
                     p[k]=abi 
                     abi=i[j] 
                     i[j]=i[k] 
                     i[k]=abi 
    elif v==2:
        n=len(p)
        for j in range(0,n-1):
             for k in range(j+1,n):
                 if p[j]<p[k]:
                     abi=p[j] 
                     p[j]=p[k] 
                     p[k]=abi 
                     abi=i[j] 
                     i[j]=i[k] 
                     i[k]=abi 
    return i,p

def vordsed_palgad(i:list,p:list):
    """Kirjedus
    :param list i:Inimiste järjend
    :param list p:Palgade järjend
    :rtype: list, list
    """
    dublikatid=[x for in p if p.count(x)>1 ]
    dublikatid=list(set(dublikatid)) #[1200,750]
    