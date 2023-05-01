# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 12:32:37 2022

@author: wzamb
"""
import math 
import random
import numpy as np
from os import remove

Np=2*math.pi
x11=-0.6459312262342367
x22=7.366154438852812
x33=-7.64931932511062
x44=-8.567102461722344
x55=3.487607095699775
y11=8.740905321913319
y22=2.460643793606872
y33=-7.668843194747846
y44=-4.086194216654618
y55=-0.32975905181133536
At=90
Af=0



def creartxt():
 
	archivo=open('datos.txt','a')
	archivo.close()    
remove('datos.txt')
while Af<=6.28319:
    #time.sleep(0.5)
   Rx1=(Np*x11)*math.sin(At)*math.cos(Af)
   Rx2=(Np*x22)*math.sin(At)*math.cos(Af)
   Rx3=(Np*x33)*math.sin(At)*math.cos(Af)
   Rx4=(Np*x44)*math.sin(At)*math.cos(Af)
   Rx5=(Np*x55)*math.sin(At)*math.cos(Af)
    
   Ry1=(Np*y11)*math.sin(At)*math.sin(Af)
   Ry2=(Np*y22)*math.sin(At)*math.sin(Af)
   Ry3=(Np*y33)*math.sin(At)*math.sin(Af)
   Ry4=(Np*y44)*math.sin(At)*math.sin(Af)
   Ry5=(Np*y55)*math.sin(At)*math.sin(Af)
    
   Rxy1=Rx1+Ry1
   Rxy2=Rx2+Ry2
   Rxy3=Rx3+Ry3
   Rxy4=Rx4+Ry4
   Rxy5=Rx5+Ry5

   MJ1=math.cos(Rxy1)
   MJ2=math.cos(Rxy2)
   MJ3=math.cos(Rxy3)
   MJ4=math.cos(Rxy4)
   MJ5=math.cos(Rxy5)
   
   MJ11=math.sin(Rxy1)
   MJ22=math.sin(Rxy2)
   MJ33=math.sin(Rxy3)
   MJ44=math.sin(Rxy4)
   MJ55=math.sin(Rxy5)
   
   A=MJ1+MJ2+MJ3+MJ4+MJ5
   B=MJ11+MJ22+MJ33+MJ44+MJ55
    
   total=math.sqrt((A*A)+(B*B))
   T=np.absolute(total)
   
   antdi=((math.cos((math.pi/2)*math.cos(At)))/math.sin(At))
   D=np.absolute(antdi)
   
   dipolos=T*D
   

   def agregar_item():
       todo_descripcion =  str(dipolos)
       archivo=open('datos.txt','a')
       archivo.write(todo_descripcion)
       archivo.write("\n")
       archivo.close()
   creartxt()
   agregar_item()
  
    
   Af +=0.025
M=[]
with open("datos.txt") as archivo:
    for linea in archivo:
        M.append(linea)
      
M.sort()
print(M[-2])