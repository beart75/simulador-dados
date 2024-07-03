from interfaz import INTERFAZ
from dado import Dado

print(INTERFAZ)

numero_caras = int(input("¿De cuantas caras quieres el dado? "))
dado =random.randint(1,numero_caras)
tirada = dado.tirada()

print(f" El resultado de tu tirada es {tirada}")
