import numpy as np
import matplotlib.pyplot as plt

def graficar_seno(frecuencia=1.0):
    x = np.linspace(0, 2*np.pi, 400)
    y = np.sin(frecuencia*x)
    plt.plot(x,y)
    plt.title(f'Onda sinusoidal con frecuenca {frecuencia}')
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.show()

if __name__ == '__main__':
    graficar_seno(3)
