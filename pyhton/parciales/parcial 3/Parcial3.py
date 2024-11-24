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

#Ej 2:

def mezclar(s1:List[int],s2:List[int])->List[int]:
    i:int=0
    res:List[int]=[]
    while i < len(s2):
        res.append(s1[i])
        res.append(s2[i])
        i+=1
    return res

#Ej 3:

def frecuencia_posiciones_por_caballo(caballos:List[str],carreras:dict)-> dict:
    res:dict={}
    for i in caballos:
        res[i]=[]
        j:int=0
        while j < len(carreras.values()[j]):
            
    

def cuadrilla(caballos:List[str])->dict:
    res:dict={}
    for i in caballos:
        res[i]=[]
        j:int=0
        while j < len(caballos):
            
            j+=1
    return res
print(cuadrilla(["linda", "petisa", "mister", "luck" ],{"carrera1":["linda", "petisa", "mister", "luck"],"carrera2":["petisa", "mister", "linda", "luck"]}))
