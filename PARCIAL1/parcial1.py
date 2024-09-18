# Escribir un programa en python que permita clasificar triángulos (Isósceles, Escaleno, Equilátero, Rectángulo) a partir de 3 valores flotantes o doubles ingresados desde el teclado.
# Definir y utilizar al menos una referencia de herencia que incluya encapsulamiento.
# El progarama debe repetirse continuamente hasta que uno de los supuestos triángulos no lo sea 

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        # Encapsulamos las propiedades de los lados
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__lado3 = lado3


    def get_lado1(self):
        return self.__lado1

    def get_lado2(self):
        return self.__lado2

    def get_lado3(self):
        return self.__lado3


    def es_triangulo(self):
        return (self.__lado1 + self.__lado2 > self.__lado3 and
                self.__lado1 + self.__lado3 > self.__lado2 and
                self.__lado2 + self.__lado3 > self.__lado1)

# Aquí se utiliza la herencia. ClasificadorTriangulo es una subclase de Triangulo. 
#ClasificadorTriangulo hereda todos los métodos y atributos de la clase Triangulo, como los métodos es_triangulo() y los getters de los lados.

class ClasificadorTriangulo(Triangulo):
    def __init__(self, lado1, lado2, lado3):
        # Llamamos al constructor de la clase padre
        super().__init__(lado1, lado2, lado3)

    def tipo_triangulo(self):
        if not self.es_triangulo():
            return "No es un triángulo válido"
        elif self.get_lado1() == self.get_lado2() == self.get_lado3():
            return "Equilátero"
        elif (self.get_lado1() == self.get_lado2() or
              self.get_lado1() == self.get_lado3() or
              self.get_lado2() == self.get_lado3()):
            return "Isósceles"
        else:
            return "Escaleno"

    def es_rectangulo(self):
        lados = sorted([self.get_lado1(), self.get_lado2(), self.get_lado3()])
        return abs(lados[0]**2 + lados[1]**2 - lados[2]**2) < 1e-6

def main():
    while True:
        try:
            lado1 = float(input("Ingrese el primer lado del triángulo: "))
            lado2 = float(input("Ingrese el segundo lado del triángulo: "))
            lado3 = float(input("Ingrese el tercer lado del triángulo: "))
          
            triangulo = ClasificadorTriangulo(lado1, lado2, lado3)

            if not triangulo.es_triangulo():
                print("No es un triángulo. Fin del programa.")
                break

            print(f"El triángulo es: {triangulo.tipo_triangulo()}")

            if triangulo.es_rectangulo():
                print("El triángulo es además rectángulo.")
        except ValueError:
            print("Por favor, ingrese valores numéricos válidos.")
            
if __name__ == "__main__":
    main()
