from cProfile import label
import tkinter
from tkinter.ttk import LabeledScale
from turtle import color
import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt

import json

window = tkinter.Tk()

print("Bienvenido")
print("Ingresa los valores de la variable, para obtener la gráfica del movimiento de un proyectil")

angulo = float(input("ingrese el valor del ángulo: "))#@param {type:"number"}
#@markdown Ingrese la altura inicial:
Hi = float(input("ingrese el valor de la altura inicial: ")) #@param {type:"number"}
#@markdown Ingrese la velocidad inicial:
Vi = float(input("ingrese el valor de la velocidad inicial: ")) #@param {type:"number"}
#@markdown Ingrese la posicion inicial:
Xi = float(input("ingrese el valor de la posición inicial en X: ")) #@param {type:"number"}
#@markdown Ingrese la posicion final:
Xf = float(input("ingrese el valor de la posición final(opcional, si no ponga 0): ")) #@param {type:"number"}
#@markdown Ingrese el tiempo maximo:
tMax = float(input("ingrese el valor del tiempo max(opcional, si no ponga 0): ")) #@param {type:"number"}
g = float(input("ingrese el valor a usar de la gravedad: "))

if angulo == 0:
  angulo = 0.001

alpha = ((angulo * np.pi) / 180)
#tMax = 2*Vi*np.sin(alpha)/g 

raiz = (((Vi**2)*(np.sin(alpha)**2)) + 2*g*Hi)

if raiz < 0:
    print(raiz)
    print("\nTu Parabola NO sale de la tierra. Intenta con otros valores\n")

else:

    if Vi == 0:
      Vi = (g*tMax)/2*np.sin(alpha)

    tMax2 = (((Vi*np.sin(alpha)) + (np.sqrt(((Vi**2)*(np.sin(alpha)**2)) + 2*g*Hi))) / g)
    t = np.arange(0, tMax2+tMax2/50, tMax2/50)


    Vx = Vi*np.cos(alpha)
    X = (Xi + (Vx*t))
    Xmax = (((Vi**2)*(2*np.cos(alpha)*np.sin(alpha))) / g)

    Vy = ((Vi*np.sin(alpha)) - (g*t))
    Y = (((Vi*np.sin(alpha)*t) - (0.5*g*t**2)) + Hi)
    Ymax = ((((Vi**2)*(np.sin(alpha)**2)) / (2*g)) + Hi)

    tHmax = ((Vi*np.sin(alpha))/g)
    xHmax = Xi + (Vx*tHmax)

    tXmax = tMax2
    xXmax = Xi + (Vx*tXmax)

    fig, ax = plt.subplots(1,1, figsize = (15,5))
    ax.plot(X, Y,'k--',lw=3)
    ax.set_title("Trayectoria (x,y)", fontsize=25)
    ax.set_xlabel('x [m]', fontsize=16)
    ax.set_ylabel('y [m]', fontsize=16)
    ax.grid(True, which='both')
    ax.plot(xHmax,Ymax,'s',lw=4, label = (f'Altura Max: ({np.round(xHmax,3)}, {np.round(Ymax,3)})'))
    ax.plot(xXmax,0,'o',lw=4, label=f'Distancia Max: ({np.round(xXmax,3)}, {0})')
    ax.plot(Xi,Hi,'v',lw=4,label=f'Posicion Inicial: ({Xi}, {Hi})')
    ax.legend()

    
    fig.show()
window.mainloop()