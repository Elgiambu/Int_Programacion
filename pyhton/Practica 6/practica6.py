import math

def imprimir_un_verso():
    print("Chekea puta, no confundas el trazo.\nAca manda mi clika, los tuyos se van al mazo")

def raiz_2() -> float:
    return 1.4142

def perimetro() -> float:
    return 2 * math.pi

def es_multiplo_de (n:int, m:int ) -> bool:
    return n % m == 0

def saludo(nombre:str):
    print(f"hola,{nombre}" )

def raiz(n:int) -> float:
    return math.sqrt(n)

def fahrenheit_a_celsius(temp:float) -> float:
    return ((temp - 32) * 5) / 9

def es_par(n: int) -> bool:
    return es_multiplo_de(n , 2)

def  cantidad_de_pizzas(comensales:int , min_cant_de_porciones:int ) -> float:
    porciones_totales : int = comensales * min_cant_de_porciones
    if (porciones_totales % 8 > 4) : 
        return round(porciones_totales / 8)
    return round((porciones_totales / 8) + 1)
    
def alguno_es_0(numero1: int, numero2: int) -> bool:
    return (numero1 == 0) or (numero2 == 0)

def ambos_0(numero1: int, numero2: int) -> bool :
    return (numero1 == 0) and (numero2 == 0)

def es_nombre_largo(nombre: str) -> bool:
    return (len(nombre) >= 3) and (len(nombre) <= 8)

def es_bisiesto(año: int) -> bool :
    return (año % 400 == 0) or ((año % 4 == 0) and (año % 100 != 0))

def peso_pino(alturaDePino: int) -> int : 
    if (alturaDePino <= 300) :
        return  alturaDePino * 3
    return 900 + (alturaDePino - 300) * 2

def es_peso_util(peso: int) -> bool :
    return (min(peso,400) == 400) and (max(peso, 1000) == 1000)

def sirve_pino(pino: int) -> bool :
    return es_peso_util(peso_pino(pino))

#problema devolver_el_doble_si_es_par (numero : Z) : Z {
# requiere{True}
# asegura{res = 2 x numero <-> numero es par}
# asegura{res = numero <-> numero no es par}
# }

def devolver_el_doble_si_es_par(numero : int) -> int :
    if (numero % 2 == 0) :
        return numero * 2
    return numero

#prblema devolver_valor_si_es_par_sino_el_que_sigue(numero:Z) : Z{
# requiere{True}
# asegura{res = numero <-> numero es par}
# asegura{res = numero + 1 <-> numero es impar}
#}

def devolver_valor_si_es_par_sino_el_que_sigue(numero : int) -> int:
    if (numero % 2 == 0) :
        return numero
    else:
        return numero + 1

def devolver_valor_si_es_par_sino_el_que_sigue_aux (numero : int) -> int:
    if (numero % 2 == 0) :
        return numero
    if (numero % 2 != 0) : 
        return numero + 1
    
# problema devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numebro : Z) : Z {
# requiere{True}
# asegura{res = 2 x numero <-> numero % 3 == 0}
# asegura{res = 3 x numero <-> numero % 9 == 0}
# asegura{res = numero si no cumple lo anterior}
# }

def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero : int) -> int:
    if (numero % 9 == 0):
        return numero *3
    elif (numero % 3 == 0):
        return numero *2
    else:
        return numero
    
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9_aux(numero : int) -> int:
    if (numero % 9 == 0):
        return numero *3
    if (numero % 3 == 0):
        return numero *2
    else:
        return numero

# problema lindo_nombre(nombre: string) :string{
# requiere{True}
# asegura{res = “Tu nombre tiene muchas letras!” <-> |nombre| >= 5}
# asegura{res = “Tu nombre tiene menos de 5 caracteres” <-> |nombre| < 5}
# }

def lindo_nombre(nombre: str) -> str:
    if (len(nombre) < 5):
        print("Tu nombre tiene menos de 5 caracteres")
    else:
        print("Tu nombre tiene muchas letras!")

def real_nombre_lindo(nombre: str):
    if (len(nombre)<8):
        print("Alto nombre crack!")
    elif (nombre == "Milton"):
        print("Milton sos un pelotudo, que nombre de mierda")
    else:
        print("Sos un accidente")
  
def el_rango(numero : int):
    if (numero < 5):
        print("Menor a 5")
    elif (10 < numero < 20 ):
        print("Entre 10 y 20")
    elif (numero > 20):
        print("Mayor a 20")

def tiene_vacas(sexo:str, edad:int) -> bool:
    return (sexo == "M" and edad >= 65) or (sexo == "F" and edad >= 60) or (edad < 18)

def situacion_de_persona(sexo: str, edad: int):
    if (tiene_vacas(sexo,edad)):
        print("Andá de vacaciones")
    else:
        print("Te toca trabajar")

def one_to_10():
    i: int = 1
    while (i <= 10):
        print(i)
        i += 1

def pares_entre_10_40():
    i: int = 10
    while (i <= 40):
        print(i)
        i += 2

def eco():
    i: int = 0
    while (i < 10):
        print("eco")
        i += 1

def cuenta_regresiva(n: int):
    i: int = n
    while (i >= 1):
            print(i)
            i -= 1
    print("Despegue!")

def viaje_al_pasado(añoInicial: int, añoDeseado: int):
    i: int= añoInicial - añoDeseado
    o: int= añoInicial 
    while (i >= 1):
        i -= 1
        o -= 1
        print(f"Viajó un año al pasado, estamos en el año: {o}")
    print("Llegaste")

def viaje_aristoteles(añoInicial: int):
    i: int= añoInicial - 384
    o: int= añoInicial
    while(i >= 19):
        i -= 20
        o -= 20
        print(f"Viajó un año al pasado, estamos en el año: {o}")
    print("Llegaste")

viaje_aristoteles(1000)