import random
class Dado:
    def __init__(self, numero_caras: int):
        generacion_correcta = self.generar_dado(numero_caras)
        while not generacion_correcta:
            try:
                nuevo_numero_caras = int(input("Este numero de caras es incorrecto, dame otro: "))
            except ValueError:
                nuevo_numero_caras = -1
            generacion_correcta = self.generar_dado(nuevo_numero_caras)
        
    def tirada(self) -> int | None:
        valor_tirada = random.randint(1, self.numero_caras)
        print(f"Se ha hecho una tirada y ha salido {valor_tirada}")
        return valor_tirada
        
    def generar_dado(self, numero_caras: int) -> bool:
        if numero_caras < 1:
            return False
        self.numero_caras = numero_caras
        return True