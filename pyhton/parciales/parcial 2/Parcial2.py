#Ej 1: 
from typing import List
from typing import Tuple

def ultima_aparicion(s:List[int],e:int)-> int:
    i:int=0
    res:int=0
    while i < len(s):
        if s[i] == e:
            res=i
        i+=1
    return res

#Ej 2:

def elementos_exclusivos(s:List[int],t:List[int])-> List[int]:
    res:List[int]=[]
    for i in s:
        if not pertenece_int(t,i):
            if not pertenece_int(res,i):
                res.append(i)
    for j in t:
        if not pertenece_int(s,j):
            if not pertenece_int(res,j):
                res.append(j)
    return res

def pertenece_int(s:List[int],n:int)->bool:
    res:bool=False
    for i in s:
        if i == n:
            res = True
    return res

#Ej 3:

def contar_traducciones_iguales(ingles:dict,aleman:dict)->int:
    res:int=0
    for i in ingles:
        if pertenece_key(aleman,i) and ingles[i] == aleman[i]:
            res += 1
    return res

def pertenece_key(diccionario:dict,a:str)->bool:
    res:bool=False
    for i in diccionario.keys():
        if a == i:
            res=True
    return res

#Ej 4:

def convertir_a_diccionario(lista:List[int])-> dict:
    res:dict={}
    for i in lista:
        if not pertenece_key(res,i):
            res[i]=1
        else:
            res[i]+=1
    return res
