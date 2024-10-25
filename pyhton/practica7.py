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
    

def ordenar(s:List[int]) -> List[int]:  #no esta en la guia, ordena una lista desordenada
    res : List[int] = []
    while(len(s) != 0):
        res.append(menor(s))
        s.remove(menor(s))
    return res

print(ordenado_org([9,2,3,1,54,0]))
print(ordenado_org([0,2,3,1,54]))
print(ordenado_org([1,2,3,1,54,0]))
