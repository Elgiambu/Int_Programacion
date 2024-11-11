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

def intercalar(p1:Pila,p2:Pila)->Pila:
    p1aux:Pila=Pila()
    p2aux:Pila=Pila()
    pfinal:Pila=Pila()
    while not p2.empty():
        p2aux.put(p2.get())
        p1aux.put(p1.get())
    while not p2aux.empty():
        n:int=0
        n = p1aux.get()
        p1.put(n)
        pfinal.put(n)
        n = p2aux.get()
        p2.put(n)
        pfinal.put(n)
    return pfinal

#MARK: Colas 
from queue import Queue as Cola

def generar_numeros_al_azar_colas(cantidad:int,desde:int,hasta:int)-> Cola:
    cola:Cola=Cola()
    while cantidad>0:
        cola.put(random.randint(desde, hasta))
        cantidad -= 1
    return cola

def cantidad_elementos_colas(c:Cola)-> int:
    res:int=0
    c2:Cola=Cola()
    while not c.empty():
        c2.put(c.get())
        res+=1
    while not c2.empty():
        c.put(c2.get())
    return res

def buscar_el_maximo_colas(c:Cola)->int:
    res:int=0
    n:int=0
    c2:Cola=Cola()
    while not c.empty():
        n = c.get()
        c2.put(n)
        if res < n:
            res = n
    while not c2.empty():
        c.put(c2.get())
    return res

def buscar_nota_minima(c:Cola)-> int:
    res:int=0
    a:Tuple[str,int]=c.get()
    c2:Cola=Cola(a)
    while not c.empty():
        b:Tuple[str,int] = c.get()
        c2.put(b)
        if a[1] < b[1]:
            res = a[1]
        else:
            res = b[1]
    while not c2.empty():
        c.put(c2.get())
    return res

def intercalar_colas(c1:Cola,c2:Cola)-> Cola:
    c1aux:Cola=Cola()
    c2aux:Cola=Cola()
    cfinal:Cola=Cola()
    e:int=0
    while not c1.empty():
        e = c2.get()
        c2aux.put(e)
        cfinal.put(e)
        e = c1.get()
        c1aux.put(e)
        cfinal.put(e)
    while not c1aux.empty():
        c2.put(c2aux.get())
        c1.put(c1aux.get())
    return cfinal

def armar_secuencia_de_bingo()->Cola:
    l:List[int]=[]    
    c:Cola=Cola()
    for i in range(100):
        l.append(i)
    i:int=99
    while i >= 0:
        elemento:int=random.randint(0,i)
        c.put(l[elemento])
        l.remove(l[elemento])
        i-=1
    return c

def jugar_carton_de_bingo(carton:List[int],bolillero:Cola)-> int:
    tiradas:int=0
    i:int=12
    bolilla:int=0
    while i!=0:
        bolilla = bolillero.get()
        if pertenece(carton,bolilla):
            i-=1
        tiradas+=1
    return tiradas

print(jugar_carton_de_bingo([0,1,4,13,56,45,99,78,83,90,7,54],armar_secuencia_de_bingo()))