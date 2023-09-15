import numpy as np
import matplotlib.pyplot as plt
import random
from math import sqrt

class Polinomio:
    def __init__(self, grado):
        self.grado = grado
        self.coeficientes = [random.randint(-5, 11) for _ in range(grado + 1)]

    def calcular_foco(self):
        if self.grado != 2:
            print("No es un polinomio de grado 2.")
            return None

        a, b, c = self.coeficientes

        # Calcular la distancia entre el vértice y el foco
        distancia_foco_vertice = 1 / (4 * a)

        # Calcular las coordenadas del vértice
        coordenada_x_vertice = -b / (2 * a)
        coordenada_y_vertice = c - (b ** 2) / (4 * a)

        # Calcular las coordenadas del foco
        coordenada_x_foco = coordenada_x_vertice
        coordenada_y_foco = coordenada_y_vertice + distancia_foco_vertice

        return (coordenada_x_foco, coordenada_y_foco)

    def raices(self):
        a, b, c = self.coeficientes

        print(f'LOS COEFICIENTES SON: ', 'A=', a, 'B=', b, 'C=', c)

        discriminante = b * b - 4 * a * c
        print('------------------------------')
        print("Discriminante: ", discriminante)

        if discriminante < 0:
            print('------------------------------')
            print(f'La ecuación no tiene soluciones reales.')
        else:
            raiz = sqrt(discriminante)
            x_1 = (-b + raiz) / (2 * a)
            if discriminante != 0:
                x_2 = (-b - raiz) / (2 * a)
                print('------------------------------')
                print(f'Las soluciones son {x_1} y {x_2}.')
            else:
                print('------------------------------')    
                print(f'La única solución es x = {x_1}')

        foco = self.calcular_foco()
        if foco:
            print('------------------------------')
            print(f"El foco de la parábola es: ({foco[0]}, {foco[1]})")

    def resolver_grado_3(self):
        if self.grado != 3:
            print("No es un polinomio de grado 3.")
            return

        a, b, c, d = self.coeficientes

        print(f'LOS COEFICIENTES SON: ', 'A=', a, 'B=', b, 'C=', c, 'D=', d)

        # Calcular las coordenadas del foco
        coordenada_x_foco = -b / (3 * a)
        coordenada_y_foco = (c - b*2 / (3 * a)) - (a * coordenada_x_foco*3)

        print('------------------------------')
        print(f"El foco de la parábola es: ({coordenada_x_foco}, {coordenada_y_foco})")

        # Calcular la ecuación de la directriz
        distancia_foco_directriz = abs(1 / (4 * a))
        coordenada_y_directriz = coordenada_y_foco - distancia_foco_directriz

        print('------------------------------')
        print(f"La ecuación de la directriz es: y = {coordenada_y_directriz}")


    def graficar_polinomio(self):
        if self.grado != 2:
            print("No es un polinomio de grado 2.")
            return

        a, b, c = self.coeficientes

        x = np.linspace(-10, 10, 400)
        y = a * x**2 + b * x + c

        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Gráfica del Polinomio de Grado 2')
        plt.grid(True)
        plt.show()

    def calcular_maximo_o_minimo(self):
        if self.grado != 2:
            print("No es un polinomio de grado 2.")
            return None

        a, _, _ = self.coeficientes

        if a > 0:
            tipo = "mínimo"
        elif a < 0:
            tipo = "máximo"
        else:
            tipo = "No es un polinomio de grado 2."

        return tipo

    def graficar_polinomio3(self):
        if self.grado != 3:
            print("No es un polinomio de grado 3.")
            return

        a, b, c, d = self.coeficientes

        x = np.linspace(-10, 10, 400)
        y = a * x**3 + b * x**2 + c * x + d

        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Gráfica del Polinomio de Grado 3')
        plt.grid(True)
        plt.show()

    def calcular_directriz(self):
        if self.grado != 2:
            print("No es un polinomio de grado 2.")
            return None

        a, b, c = self.coeficientes

        # Calcular la coordenada x de la directriz
        coordenada_x_directriz = -b / (2 * a)

        print('------------------------------')
        print(f"La ecuación de la directriz es: x = {coordenada_x_directriz}")

    def info(self):
        print(f'Ecuaciones de tercer grado')
        print(f'    ax³ + bx² + cx + d = 0\n')


grado = input("Ingresa el grado del polinomio (1, 2 o 3): ")
print('------------------------------')

if grado in ("1", "2", "3"):
    if grado == "1":
        a = random.randint(1, 11)
        b = random.randint(1, 11)
        print('LOS COEFICIENTES SON: ', a, ' y ', b)
        if a == 0:
            if b == 0:
                print("Infinitas soluciones")  # El polinomio es equivalente a 0x = 0
            else:
                print("No hay soluciones")  # El polinomio es equivalente a 0x = b
        else:
            x = -b / a
            print("La solución es:", x)

    elif grado == "2":
        polinomio = Polinomio(int(grado))
        polinomio.raices()
        polinomio.graficar_polinomio()
        
        tipo = polinomio.calcular_maximo_o_minimo()
        print(f'El polinomio tiene un punto de {tipo}.')
        polinomio.calcular_directriz()

    elif grado == "3":
        polinomio = Polinomio(int(grado))
        polinomio.graficar_polinomio3()
        #polinomio.raices()
        polinomio.resolver_grado_3()
else:
    print("El programa solo admite polinomios de grado 1, 2 o 3.")