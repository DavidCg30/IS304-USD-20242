import time

class CuentaAtras:
    def __init__(self, inicio, espera):
        if inicio < 0 or espera < 0:
            raise ValueError("Los valores de inicio y espera deben ser números enteros positivos.")
        self.inicio = inicio
        self.espera = espera

    def iniciar(self):
        cuenta = self.inicio
        while cuenta >= 0:
            print(cuenta)
            time.sleep(self.espera)
            cuenta -= 1
        print("Cuenta atrás finalizada")
        
inicio = int(input("Ingrese el número en el que desea empezar la cuenta atrás: "))
espera = int(input("¿Cuántos segundos desea esperar entre cada número? "))
cuenta_atras = CuentaAtras(inicio, espera)
cuenta_atras.iniciar()
