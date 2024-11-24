from typing	import List
from typing	import Tuple
#Ej 1:

def ind_enesima_aparicion(s:List[int],n:int,elem:int)->int:
    res:int=0
    veces_de_elem:int=0
    if aparecera_n_veces(s,n,elem):
        i:int=0
        while veces_de_elem != n:
            if s[i] == elem:
                veces_de_elem += 1
            i+=1
        res = i-1
    else:
        res = -1
    return res


def aparecera_n_veces(s:List[int],n:int,elem:int)->bool:
    veces:int=0
    res:bool=False
    for i in s:
        if elem == i:
            veces +=1
    if veces >= n:
        res = True
    return res

print(ind_enesima_aparicion([-1, 1, 1, 5, -7, -1, 3],2,-1))