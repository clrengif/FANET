# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 13:30:45 2023

@author: wzamb
"""
import math 

import numpy as np


At=90
Np=2*math.pi
Af=0
mdipolo=[]
m=[0.9576350054874248, 3.5736079658804942, 6.79802604347819, 3.1984283075467324, 6.121170700834444, 2.722982753036978, 2.967360252345255, 4.8745065756599315, 5.686612338161176, 4.57977258582889]
x11=m[0]
x22=m[1]
x33=m[2]
x44=m[3]
x55=m[4]
y11=m[5]
y22=m[6]
y33=m[7]
y44=m[8]
y55=m[9]

while Af<=6.28319:
    
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
   
    MJ11=math .sin(Rxy1)
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
    mdipolo.append(dipolos)
    Af +=0.025
    
    print(dipolos)