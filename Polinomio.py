import random
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize

class Polinomio:
    def _init_(self, grado):
        self.grado = grado
        self.coeficientes = [random.uniform(-10, 10) for _ in range(grado + 1)]

    def resolver_ecuacion(self):
        if self.grado == 2:
            a, b, c = self.coeficientes
            discriminante = b**2 - 4*a*c
            print('LA DISCRIMINANTE ES: ',discriminante)
            if discriminante < 0:
                return None, None, None
            elif discriminante == 0:
                x = -b / (2*a)
                return x, discriminante, None
            else:
                x1 = (-b + math.sqrt(discriminante)) / (2*a)
                x2 = (-b - math.sqrt(discriminante)) / (2*a)
                return x1, x2, discriminante
        elif self.grado == 3:
            return None, None, None
        else:
            return None, None, None

    def calcular_foco_directriz(self):
        if self.grado < 2:
            print("El polinomio debe ser de grado 2 o superior para calcular el foco, el discriminante y la directriz.")
            return

        a = self.coeficientes[-3]  # Coeficiente principal del término cuadrático
        b = self.coeficientes[-2]  # Coeficiente del término lineal
        c = self.coeficientes[-1]  # Término independiente

        if a == 0:
            print("El coeficiente principal (a) no puede ser igual a 0.")
            return

        distancia_foco_directriz = 1 / (4 * abs(a))
        coordenada_x_vertice = -b / (2 * a)
        coordenada_y_vertice = c - (b ** 2) / (4 * a)
        coordenada_x_foco = coordenada_x_vertice
        if a > 0:
            coordenada_y_foco = coordenada_y_vertice + distancia_foco_directriz
            coordenada_y_directriz = coordenada_y_vertice - distancia_foco_directriz
        else:
            coordenada_y_foco = coordenada_y_vertice - distancia_foco_directriz
            coordenada_y_directriz = coordenada_y_vertice + distancia_foco_directriz

        return (coordenada_x_foco, coordenada_y_foco), coordenada_y_directriz

    def encontrar_maximo_minimo(self):
        if self.grado < 2:
            print("El polinomio debe ser de grado 2 o superior para encontrar máximos y mínimos.")
            return

        def funcion_objetivo(x):
            return -np.polyval(self.coeficientes, x)

        x_inicial = random.uniform(-10, 10)
        resultado = minimize(funcion_objetivo, x_inicial, method='BFGS')
        return resultado.fun, resultado.x[0]

    def graficar_polinomio(self):
        if self.grado < 2:
            print("El polinomio debe ser de grado 2 o superior para graficarlo.")
            return

        x = np.linspace(-10, 10, 400)
        y = np.polyval(self.coeficientes, x)
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Gráfica del Polinomio')
        plt.grid(True)
        plt.show()

def main():
    grado = int(input("Ingresa el grado del polinomio: "))

    polinomio = Polinomio(grado)
    soluciones, discriminante, directriz = polinomio.resolver_ecuacion()
    foco, _ = polinomio.calcular_foco_directriz()
    extremo, extremo_x = polinomio.encontrar_maximo_minimo()

    print(f"Los coeficientes del polinomio son: {polinomio.coeficientes}")
    if grado == 2:
        if discriminante < 0:
            print("La ecuación cuadrática no tiene soluciones reales.")
        else:
            if discriminante == 0:
                print(f"La única solución es x = {soluciones[0]}")
            else:
                print(f"Las soluciones son x1 = {soluciones[0]} y x2 = {soluciones[1]}")
            print(f"El discriminante es: {discriminante}")
            if foco:
                print(f"El foco de la parábola es: ({foco[0]}, {foco[1]})")
            else:
                print("No se pudo calcular el foco.")
            if directriz:
                print(f"La ecuación de la directriz es: y = {directriz}")
            else:
                print("No se pudo calcular la directriz.")
        if extremo:
            print(f"El valor extremo es: {extremo} en x = {extremo_x}")
        else:
            print("No se pudo encontrar el valor extremo.")
    else:
        print("Este programa solo resuelve ecuaciones cuadráticas o superiores y grafica polinomios de grado 2 o superiores.")
    
    polinomio.graficar_polinomio()

if __name__ == "__main__":
    main()