# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 19:24:57 2022

@author: wzamb
"""

import random
from os import remove
import math 
import numpy as np


# rango0=input("ingrese el numero de coordenadas que desea generar: ")
# rango1=input("ingrese el rango en el que se generan las cooredenadas aleatorios: ")
# rango2=input(": ")
# rango3=input("ingrese la margen de error que genera el movimiento del dron: ")
rango0=4#int(rango0)
rango1=1#float(rango1) 
rango2=10#float(rango2) 
rango3=1#float(rango3) 
At=math.pi/2
Af=0
Np=2*math.pi
def creartxt():
 
	archivo=open('cordenadas.txt','a')
	archivo.close()  
    
remove('cordenadas.txt')
for i in range(rango0):
    x11=(random.uniform(rango1,rango2))
    x22=(random.uniform(rango1,rango2))
    x33=(random.uniform(rango1,rango2))
    x44=(random.uniform(rango1,rango2))
    x55=(random.uniform(rango1,rango2))
    y11=(random.uniform(rango1,rango2))
    y22=(random.uniform(rango1,rango2))
    y33=(random.uniform(rango1,rango2))
    y44=(random.uniform(rango1,rango2))
    y55=(random.uniform(rango1,rango2))
    
    #print(x11,x22,x33,x44,x55,y11,y22,y33,y44,y55)
    
    x111=x11-rango3
    x112=x11+rango3
    x221=x22-rango3
    x222=x22+rango3
    x331=x33-rango3
    x332=x33+rango3
    x441=x44-rango3
    x442=x44+rango3
    x551=x55-rango3
    x552=x55+rango3

    y111=y11-rango3
    y112=y11+rango3
    y221=y22-rango3
    y222=y22+rango3
    y331=y33-rango3
    y332=y33+rango3
    y441=y44-rango3
    y442=y44+rango3
    y551=y55-rango3
    y552=y55+rango3

     
    for x1 in range(1):
      x1= random.uniform(x111,x112)
      x2= random.uniform(x221,x222)
      x3= random.uniform(x331,x332)
      x4= random.uniform(x441,x442)
      x5= random.uniform(x551,x552)
      y1= random.uniform(y111,y112)
      y2= random.uniform(y221,y222)
      y3= random.uniform(y331,y332)
      y4= random.uniform(y441,y442)
      y5= random.uniform(y551,y552)
    
    
    def agregar_item():
        todo_descripcion1 =  str(x1)
        todo_descripcion2 =  str(x2)
        todo_descripcion3 =  str(x3)
        todo_descripcion4 =  str(x4)
        todo_descripcion5 =  str(x5)
        todo_descripcion6 =  str(y1)
        todo_descripcion7 =  str(y2)
        todo_descripcion8 =  str(y3)
        todo_descripcion9 =  str(y4)
        todo_descripcion10 =  str(y5)
        archivo=open('cordenadas.txt','a')
        archivo.write(todo_descripcion1)
        archivo.write("  ")
        archivo.write(todo_descripcion2)
        archivo.write("  ")
        archivo.write(todo_descripcion3)
        archivo.write("  ")
        archivo.write(todo_descripcion4)
        archivo.write("  ")
        archivo.write(todo_descripcion5)
        archivo.write("  ")
        archivo.write(todo_descripcion6)
        archivo.write("  ")
        archivo.write(todo_descripcion7)
        archivo.write("  ")
        archivo.write(todo_descripcion8)
        archivo.write("  ")
        archivo.write(todo_descripcion9)
        archivo.write("  ")
        archivo.write(todo_descripcion10)

        archivo.write("\n")
        archivo.close()
    creartxt()
    agregar_item()
    
linea=[]    
with open("cordenadas.txt") as archivo:
    for linea in archivo:
        print(linea)        



   


        
        