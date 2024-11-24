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

#Se desea verificar si una matriz es cuasi decreciente por columnas. Esto es que el máximo de cada columna sea mayor estricto que el máximo de la columna siguiente

#Para ello se pide desarrollar una función en Python que implemente esta idea respetando la siguiente especificación:

#matriz_cuasi_decreciente (in matriz: seq⟨seq⟨Z⟩⟩): Bool {
#  requiere: {|matriz| > 0}
#  requiere: {|matriz[0]| > 0}
#  requiere: {todos los elementos de matriz tienen la misma longitud}
#  asegura: {res es igual a True <=> para todo 0<=i<|matriz[0]|-1, el máximo de la columna i de matriz > el máximo de la columna i + 1 de matriz }
# }

#Ej 5:

def matriz_cuasi_decreciente(matriz:List[List[int]])->bool:
    res:bool=True
    m_transpuesta:List[List[int]]=traspuesta(matriz)
    i:int=0
    list_aux:List[int]=[]
    for i in m_transpuesta:
        list_aux.append(mayor(i))
    j:int=0
    while j+1 < len(list_aux):
        if list_aux[j] <= list_aux[j+1]:
            res= False
        j+=1
    return res

m_ej=[[20,10,5,3],
      [2,3,2,2],
      [4,2,1,1]]

def mayor(columna:List[int])-> int:
    res:int=columna[0]
    for i in columna:
        if i >= res:
            res = i
    return res

def traspuesta(matriz:List[List[int]])->List[List[int]]:
    res:List[List[int]]=[]
    j:int=0
    while j < len(matriz[0]):
        list:List[int]=[]
        for i in matriz:
            list.append(i[j])
        res.append(list)
        j+=1
    return res

print(matriz_cuasi_decreciente(m_ej))
