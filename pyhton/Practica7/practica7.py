from typing import List

def pertenece(s: List[int], e: int) -> bool:
    i : int = 0
    while (i < len(s)):
        if e == s[i]:
            return True
        i += 1
    return False    

def divide_a_todos_org(s: List[int], e: int) -> bool:
    i : int = 0
    while (i < len(s)):
        if s[i] % e != 0 :
            return False
        i += 1
    return True

def divide_a_todos(s: List[int], e: int) -> bool: #mismos ej distinta resolucion
    for e_prima in s:
        if e_prima % e != 0:
            return False
    return True

def suma_total(s:List[int]) -> int:
    i: int = 0
    res = 0
    while (i < len(s)):
        res += s[i]
        i += 1
    return res

def mayor(s:List[int]) -> int:
    i: int = 0
    res: int = s[0]
    while ((i) < len(s)):
        if (s[i] > res):
            res = s[i]
        i += 1
    return res

def menor(s:List[int]) -> int:
    i: int = 0
    res: int = s[0]
    while ((i) < len(s)):
        if (s[i] < res):
            res = s[i]
        i += 1
    return res

def ordenado(s:List[int]) -> bool:
    i: int = 0
    while ((i+1) < len(s)):
        if s[i]>s[i+1]:
            return False
        i += 1
    return True
    

def ordenar(s:List[int]) -> List[int]:  #no esta en la guia, ordena una lista desordenada
    res : List[int] = []
    while(len(s) != 0):
        res.append(menor(s))
        s.remove(menor(s))
    return res

def pos_maximo(s:List[int]) -> int:
    if len(s) == 0:
        return -1
    else:
        return s.index(mayor(s))

def pos_minimo(s:List[int]) -> int:
    if len(s) == 0:
        return -1
    else:
        return s.index(menor(s))

def largo_de_palabras(s:List[str]) -> bool:
    i: int =0
    while i<len(s):
        if len(s) == 0:
            return False
        elif len(s[i]) > 7:
            return True
        i += 1
    return False

def palindromo(s: List[str]) -> bool: #no esta terminado
    res : List[str] = []
    i: int = 0
    while i < len(s):
        res.append(s[i])
        i =+ 1
    if res == s:
        return True
    return False

def tres_consecutivos(s:List[int]) -> bool:
    i: int=0
    if len(s)>2:
        while i+2 < len(s):
            if s[i] == s[i+1]:
                if s[i] == s[i+2]:
                    return True
            i =+ 1
    return False

print(tres_consecutivos([1,2,2,3,4,5]))
print(tres_consecutivos([1,2,2,2,3,4,5]))
print(tres_consecutivos([]))
print(tres_consecutivos([1,2,2,3,4,2,5]))