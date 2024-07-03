from interfaz import INTERFAZ, INTERFAZ_FINAL
from dado import Dado

print(INTERFAZ)

numero_caras = int(input("De cuantas caras quieres el dado: "))
try:
    dado = Dado(numero_caras)
except ValueError:
    print("El dado no se ha generado correctamente")
    dado = Dado(2)  # TODO: Este dado es un arreglo temporal, necesitamos una forma de generar dados en bucle
tiradas = []
terminar = False

while terminar is False:
    tirada = dado.tirada()
    tiradas.append(tirada)
    if input(INTERFAZ_FINAL).lower() not in ("si", "yes", "y"):
        terminar = True

print(tiradas)
