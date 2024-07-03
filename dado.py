import random

INTERFAZ ="""
#############################
SCRIPT DE SIMULACION DE DADOS
#############################

"""
print(INTERFAZ)

Class Dado:
    def __init__(seft, numero_caras:int)
        seft.numero_caras = numero_caras
    def tirada(seft):
        return random.randint(1 , seft.numero_caras)

numero_caras = int(input("¿De cuantas caras quieres el dado? "))
dado =random.randint(1,numero_caras)
tirada = dado.tirada()

print(f" El resultado de tu tirada es {tirada}")
