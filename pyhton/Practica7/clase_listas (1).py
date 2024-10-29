############### code by Agustín Sansone ###############

from typing import List

################## Ejercicio 1.1 ##################

def pertence_v1(s: List[int], e: int) -> bool: # una forma de usar el 'for'
    for e_prima in s:
        if e == e_prima:
            return True
    return False

def pertenece_v2(s: List[int], e: int) -> bool: # otra forma de usar el 'for'
    for i in range(len(s)): # igual que range(0, len(s), 1)
        if e == s[i]:
            return True
    return False

def pertenece_v3(s: List[int], e: int) -> bool: # usando 'while'
    i: int = 0 # suele ser 'i' para denotar una variable usada como índice, bien podría llamarse 'indice' ó 'index'
    while i < len(s):
        if e == s[i]:
            return True
        i += 1
    return False

def pertence_v3(s: List[int], e: int) -> bool: # con un único 'return'
    resultado: bool = False
    for e_prima in s:
        if e == e_prima:
            resultado = True
    return resultado

def pertenece_v4(s: List[int], e: int) -> bool: # cortando potencialmente antes con 'break'
    resultado: bool = False
    for e_prima in s:
        if e == e_prima:
            resultado = True
            break
    return resultado

def pertenece_v5(s: List[int], e: int) -> bool: # versión ilegal para esta materia
    return e in s

################## Ejercicio 1.3 ##################

def suma_total(s: List[int]) -> int:
    suma: int = 0
    for e in s:
        suma += e # equivalente a 'suma = suma + e'
    return suma

################## Ejercicio 2.1 ##################

def CerosEnPosicionesPares(s: List[int]) -> None:
    for i in range(0, len(s), 2):
        s[i] = 0
    # también se puede recorrer los elemns y preguntar con un if si mandar a 0 o no, esta es más directa
    
################## Ejercicio 2.2 ##################

def CerosEnPosicionesPares2(s: List[int]) -> List[int]:
    resultado: List[int] = []
    for i in range(len(s)):
        if i % 2 == 0:
            resultado.append(0)
        else:
            resultado.append(s[i])
    return resultado
