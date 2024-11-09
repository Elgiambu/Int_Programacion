from queue import LifoQueue as Pila
from queue import Queue as Cola
from typing import List
from typing import Tuple
from queue import Queue
from collections import deque

import random

#MARK: Pilas

def generar_numeros_al_azar(cantidad:int,desde:int,hasta:int)->Pila:
    i:int=0
    res:Pila=Pila()
    while i < cantidad:
        res.put(random.randint(desde,hasta))
        i+=1
    return res

def cantidad_elementos(p:Pila)->int:
    copy:Pila=Pila()
    res:int=0
    while not p.empty():
        copy.put(p.get())
        res+=1
    while not copy.empty():
        p.put(copy.get())
    return res

def busca_el_maximo(p:Pila) -> int: 
    res:int=0
    n:int=0
    copy:Pila=Pila()
    while not p.empty():
        n=p.get()
        copy.put(n)
        if n > res:
            res = n
    while not copy.empty():
        p.put(copy.get())
    return res

def buscar_nota_maxima(p:Pila)->Tuple:
    copy:Pila=Pila()
    tupla:Tuple=["x",0]
    max_tupla:Tuple=[]
    while not p.empty():
        tupla = p.get()
        copy.put(tupla)
        if tupla[1] > max_tupla[1]:
            max_tupla = tupla
    while not copy.empty():
        p.put(copy.get())
    return max_tupla

def esta_bien_balanceada(operacion: str) -> bool:
    i:int=0
    p:Pila=Pila()
    while i < len(operacion):
        if operacion[i] == "(":
            p.put(operacion[i])
        elif operacion[i] == ")":
            if p.empty():
                return False
            p.get()
        i+=1
    return p.empty()

def pertenece(s:List,e)->bool:
    i:int=0
    while i<len(s):
        if e == s[i]:
            return True
        i+=1
    return False

            
def evaluar_expresion(s:str)->float:
    operadores:str="+-*/"
    i:int=0
    operando:str=""
    p:Pila=Pila()
    while i < len(s):
        if pertenece(operadores,s[i]):
            b:float=p.get()
            a:float=p.get()
            if s[i] == "+":
                p.put(a + b)
            elif s[i] == "-":
                p.put(a - b)
            elif s[i] == "*":
                p.put(a * b)
            else:
                p.put(a / b)
        elif s[i]==" " and not pertenece(operadores,s[i-1]):
            p.put(float(operando))
            operando = ""
        else: 
            operando += s[i]
        i+=1
    return p.get()    

print(evaluar_expresion("3 4 + 5 * 2 -"))