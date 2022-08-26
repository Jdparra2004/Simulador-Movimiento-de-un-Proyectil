from cProfile import label
from logging import exception
import tkinter
from tkinter.ttk import LabeledScale,Frame
from tkinter import Button, Label, ttk
from turtle import color
import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import json


print("Bienvenido")
print("Ingresa los valores de la variable, para obtener la gráfica del movimiento de un proyectil")
print("Ten en cuenta que solo el valor del anguló es obligatorio.Si no tienes un dato, pon el valor de 0,")
print("El simulador, calculará los datos faltantes  ")

#@title DATOS NECESARIOS (Ojo, el angulo es necesario):

try:
  
  angulo = float(input("Ingresa el valor del Angulo(en grados): ")) #@param {type:"number"}
  #@markdown Ingrese la velocidad inicial:
  Vi = float(input("Ingresa el valor de la velocidad inicial(m/s): ")) #@param {type:"number"}
  #@markdown Ingrese la altura inicial:
  Hi = float(input("Ingresa el valor del la altura inicial(m): ")) #@param {type:"number"}
  #@markdown Ingrese la altura final:
  Hf = float(input("Ingresa el valor de la altura final(m): ")) #@param {type:"number"}
  #@markdown Ingrese la posicion inicial:
  Xi = float(input("Ingresa el valor de la posición inicial(m): ")) #@param {type:"number"}
  #@markdown Ingrese la posicion final:
  Xf = float(input("Ingresa el valor de la posición final(m): ")) #@param {type:"number"}
  #@markdown Ingrese el tiempo maximo:
  tMax = float(input("Ingresa el valor del tiempo maximo(s): ")) #@param {type:"number"}
  #@markdown Ingrese el valor de la Gravedad:
  g = float(input("Ingresa el valor d la gravedad(m/s^2): "))

  if Hi == None:
    Hi = 0

  if Xi == None:
    Xi = 0

  if Hf == None:
    Hf = 0

  if tMax == None:
    tMax = 0

  alpha = ((angulo * np.pi) / 180)
  #tMax = 2*Vi*np.sin(alpha)/g 

  if Vi == 0 or Vi == None:
    Vi = (g*tMax)/2*np.sin(alpha)

  raiz = (((Vi**2)*(np.sin(alpha)**2)) - (2*g*Hf) + (2*g*Hi))

  if raiz < 0:
      print("\nNO ES POSIBLE CALCULAR UNA PARABOLA CON LOS DATOS INGRESADOS.\nINTENTA CON OTROS VALORES")

  else:

    tMax2 = (((Vi*np.sin(alpha)) + (np.sqrt(((Vi**2)*(np.sin(alpha)**2)) - (2*g*Hf) + (2*g*Hi)))) / g)
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
    xXmax = Xi + (Vx*tMax2)

    fig, ax = plt.subplots(1,1, figsize = (15,5))
    ax.plot(X, Y,'k--',lw=3)
    ax.set_title("Trayectoria (x,y)", fontsize=25)
    ax.set_xlabel('x [m]', fontsize=16)
    ax.set_ylabel('y [m]', fontsize=16)
    ax.grid(True, which='both')
    ax.plot(xHmax,Ymax,'s',lw=4, label = (f'Altura Max: ({np.round(xHmax,2)}, {np.round(Ymax,2)})'))
    ax.plot(xXmax,Hf,'o',lw=4, label=f'Distancia Max: ({np.round(xXmax,2)}, {Hf})')
    ax.plot(Xi,Hi,'v',lw=4,label=f'Posicion Inicial: ({Xi}, {Hi})')
    ax.plot(lw=4,label=f'Velocidad Generada: ({np.round(Vi, 2)})')
    ax.legend()

    fig.show()
except(exception):
  print(exception)
  print("No se puede calcular debido a la falta de datos necesarios.")

#Interfaz.
ventana = tkinter.Tk()
ventana.mainloop()

