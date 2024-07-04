#from interfaz import INTERFAZ, INTERFAZ_FINAL
from interfaz import * #traer todas las variablesfrom interfaz import *
from dado import Dado

print(INTERFAZ)
try:
    numero_caras = int(input("De cuantas caras quieres el dado: "))
except ValueError:
    numero_caras = -1
dado = Dado(numero_caras)
tiradas = []
terminar = False

while terminar is False:
    tirada = dado.tirada()
    tiradas.append(tirada)
    if input(INTERFAZ_FINAL).lower() not in ("si", "yes", "y"):
        terminar = True

print(LISTA_TIRADAS, tiradas)
print(TOTAL_TIRADAS, sum(tiradas))