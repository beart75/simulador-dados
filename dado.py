import random

INTERFAZ ="""
#############################
SCRIPT DE SIMULACION DE DADOS
#############################

"""
print(INTERFAZ)
numero_caras = int(input("¿De cuantas caras quieres el dado?"))
dado =random.randint(1,numero_caras)
print(f" El resultado de tu tirada es {dado}")
