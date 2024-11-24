#Ej: 1

def verificar_transacciones(s:str)-> int:
    saldo:int=0
    i:int=0
    terminar:bool= False
    while i < len(s) and not terminar:
        if s[i] == "v" and saldo >= 56:
            saldo -= 56
        elif s[i] == "x":
            terminar = True
        elif s[i]=="r":
            saldo += 350
        i+=1
    return saldo

#Ej 2:
from typing import List
from typing import Tuple

def valor_minimo(s:List[Tuple[float,float]])->float:
    res:float=s[0][0]
    for i in s:
        if i[0] < res:
            res = i[0]
    return res

#Ej 3:

def valores_extremos(cotizaciones_diarias:dict)-> dict:
    res:dict={}
    for keys in cotizaciones_diarias.keys():
        valores:List=cotizaciones_diarias[keys]
        min:float=valores[0][1]
        max:float=valores[0][1]
        for j in valores:
            if j[1]< min:
                min=j[1]
            elif j[1]>max:
                max=j[1]
        res[keys] = (min,max)
    return res

