from typing import List
from typing import Tuple
import math

#MARK: ejercicio 1

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
        i += 1
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
            i += 1
    return False

def digitos_impares(s:List[int]) -> int:
    i:int=0
    lista_aux:List[int] = s.copy()
    res:List[int]=[]
    if (len(s)==0):
        return 0
    while (i < len(lista_aux)):
        while (lista_aux[i]>10):
            if ((lista_aux[i]%10)%2 != 0):
                res.append(lista_aux[i]%10)
            lista_aux[i]//=10
        if lista_aux[i]%2 !=0:
            res.append(lista_aux[i]%10) 
        i += 1
    return len(res)

def ceros_en_posiciones_pares(s:List[int]) -> None:
    i:int=0
    if len(s) <= 1:
        return s
    while i < len(s):
        if i%2 != 0:
            s[i] = 0
        i += 1
    return s

def sin_vocales(s:str) -> str:
    i: int=0
    res: str = ""
    opc: str = "aeiouAEIOU"
    while i < len(s):
        if not pertenece(opc, s[i]):
            res += s[i]
        i += 1
    return res

def remplaza_vocales(s:str) -> str:
    i:int =0
    res:str =""
    opc:str ="aeiouAEIOU"
    while i<len(s):
        if not pertenece(opc, s[i]):
            res += s[i]
        else:
            res += "_"
        i += 1
    return res

def da_vuelta_str(s:str) -> str:
    i:int=0
    res:str =""
    while i<len(s):
        res += s[len(s)-i-1]
        i += 1
    return res

def elimina_repetidos(s:str) -> str:
    i:int=0
    res:str="" 
    while i<len(s):
        if not pertenece(res, s[i]):
            res += s[i]
        i += 1
    return res

def resultado_materias(notas:List[int]) -> int:
    i:int=0
    lis_aux:List[int]=[]
    res:int=0
    while i < len(notas):
        if notas[i] >= 4:
            lis_aux.append(notas[i])
        else:
            return 3
        i += 1
    if ((suma_total(lis_aux)//len(lis_aux)) >= 7):
        res = 1
    else:
        res = 2
    return res

def movimientos_bancarios(movimientos:List[Tuple[str,int]]) -> int:
    i:int=0
    cuenta:int=0
    while i < len(movimientos):
        if movimientos[i][0] == "I":
            cuenta += movimientos[i][1]
        else:
            cuenta -= movimientos[i][1]
        i += 1
    return cuenta

#MARK: ejercicio 3

def pertenece_a_cada_uno(s:List[List[int]],e:int,res:List[bool]) -> None:
    i:int=0
    while i<len(s):
        res.insert(i, pertenece(s[i],e))
        i+=1
    return res

def pertenece_a_cada_uno_2(s:List[List[int]],e:int,res:List[bool]) -> None:
    i:int=0
    res.clear()
    while i<len(s):
        res.append(pertenece(s[i],e))
        i+=1
    return res

def pertenece_a_cada_uno_3(s:List[List[int]],e:int) -> None:
    i:int=0
    res:List[bool]=[]
    while i<len(s):
        res.append(pertenece(s[i],e))
        i+=1
    return res

#si se puede usar la implementacion del 2 para la esp. del ej 1. pues este siempre devuelve un "res" del mismo 
# largo que "s", mientras que el ej 1 no sirve para la esp. de 2. pues aunque este puede devolver un "res" del mismo
# largo que "s", tambien puede ser mayo y eso no cumpliria con la especificacion del 2.

def es_matriz(s:List[List[int]]) -> bool:
    if len(s) <= 0 or len(s[0]) <= 0:
        return False
    i:int=0
    while i<len(s):
        if s[i] == s[0]:
            return True

def filas_ordenadas(s:List[List[int]],res:List[bool]) -> None:
    i:int=0
    res.clear()
    while i<len(s):
        res.append(ordenado(s[i]))
        i+=1
    return res

def columna(s:List[List[int]], c:int) -> List[int]:
    i:int=0
    res:List[int]=[]
    while i<len(s):
        res.append(s[i][c])
        i+=1
    return res

def columnas_ordenadas(s:List[List[int]]) -> List[bool]:
    i:int=0
    c:int=0
    res:List[bool]=[]
    while i<len(s):
        while c<len(s[i]):
            res.append(ordenado(columna(s,c)))
            c+=1
        i+=1
    return res

def transponer(s:List[List[int]]) -> List[List[int]]:
    i:int=0
    c:int=0
    res:List[List[int]]=[]
    while i<len(s):
        while c<len(s[i]):
            res.append(columna(s,c))
            c+=1
        i+=1
    return res

def ta_te_ti(s:List[List[str]]) -> int:
    i:int=0
    c:int=0
    res:str=""
    while i<3: #chekeo tateti en horizontal
        if s[i][0] == s[i][1] == s[i][2] != " ":
            res = s[i][0]
        i+=1
    while c<3: #chekeo tateti en vertical
        if columna(s,c)[0] == columna(s,c)[1] == columna(s,c)[2] != " ":
            res = columna(s,c)[0]
        c +=1
    if (s[1][1] == s[0][0] == s[2][2]) or (s[1][1] == s[0][2] == s[2][0]): #chekeo diagonal
        res = s[1][1]
    if res == "X":
        return 1
    elif res == "O":
        return 0
    return 2

def nombres() -> List[str]:
    s=input("nombre de estudiantes: ")
    res:List[str]=[]
    while s!="Listo" and s!="":
        res.append(s)
        s=input("nombre de estudiantes: ")
    return res

def social_credits() -> List[Tuple[str,int]]:
    accion=input("Que desea hacer? _")
    res:List[Tuple[str,int]]=[]
    saldo:int=0
    while accion[0]!="X":
        monto=int(input("Monto: "))
        if accion == "D":
            res.append((accion,monto))
            saldo-=monto
        else:
            res.append((accion,monto))
            saldo+=monto
        
        accion=input("Que desea hacer? _")
    return res