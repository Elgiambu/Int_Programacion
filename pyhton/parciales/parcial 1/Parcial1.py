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

print(verificar_transacciones("ssrvvrrvvsvvsxrvvv"))