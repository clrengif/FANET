from ast import literal_eval
import math 
import random
import numpy as np
from os import remove
rango9=input("ingrese la margen de error que genera el movimiento del dron: ")
rango9=int(rango9)
At=90
totaldipolo2=[]
totaldipolomutacion2=[]
totaldipolocruzamineto3=[]
Np=2*math.pi
m2dipolo=[]
coordenadas=[]
for i in range(rango9):
    with open("cordenadas.txt", "r") as archivo:
         lineas = archivo.readlines()
         indices_aleatorios = random.sample(range(len(lineas)), 2)
         
         linea1 = lineas[indices_aleatorios[0]].strip().split()
         linea2 = lineas[indices_aleatorios[1]].strip().split()

         a = [float(num) for num in linea1]
         b = [float(num) for num in linea2]
         print(a) 
         print(b)
         Mcruzamiento=[
                      [a[0],b[1],a[2],b[3],a[4],a[5],b[6],a[7],b[8],a[9]],
                      [b[0],a[1],b[2],a[3],b[4],b[5],a[6],b[7],a[8],b[9]],
                      [b[0],b[1],a[2],b[3],a[4],b[5],b[6],a[7],b[8],a[9]],
                      [a[0],a[1],b[2],a[3],b[4],a[5],a[6],b[7],a[8],b[9]],
                      [b[0],b[1],b[2],a[3],a[4],b[5],b[6],b[7],a[8],a[9]],
                      [a[0],a[1],a[2],b[3],b[4],a[5],a[6],a[7],b[8],b[9]],
                      [a[0],a[1],b[2],b[3],b[4],a[5],a[6],b[7],b[8],b[9]],
                      [b[0],b[1],a[2],a[3],a[4],b[5],b[6],a[7],a[8],a[9]],
                      [a[0],b[1],a[2],b[3],b[4],a[5],b[6],a[7],b[8],b[9]],
                      [b[0],a[1],b[2],a[3],a[4],b[5],a[6],b[7],a[8],a[9]]
                      ]
         cruzamiento =0
         C=[]
         k=[]
         def creartxt():
               archivo=open('seleccion2.txt','a')
               archivo.close()   
               archivo=open('seleccion3.txt','a')
               archivo.close() 
         
         for i in range(1):
             Af=0
             m2dipolo=[]
             m3dipolo=[]
             j=random.random()
             l=random.random()
             if j>0.9:
                 break
             if (j>=0)and(j<=0.9): #Cruzamiento
                 cruzamineto =1
                 C=(random.choice(Mcruzamiento))
                 #print(C,"correcto, combinacion  ")  
             mutacion=0
             if (l>0.9)and(l<=1): #Mutacion
                    mutacion=1
                    Mmutacion=[
                            [C[0]+0.1,C[1],C[2],C[3],C[4],C[5],C[6],C[7],C[8],C[9]],
                            [C[0],C[1]+0.1,C[2],C[3],C[4],C[5],C[6],C[7],C[8],C[9]],
                            [C[0],C[1],C[2]+0.1,C[3],C[4],C[5],C[6],C[7],C[8],C[9]],
                            [C[0],C[1],C[2],C[3]+0.1,C[4],C[5],C[6],C[7],C[8],C[9]],
                            [C[0],C[1],C[2],C[3],C[4]+0.1,C[5],C[6],C[7],C[8],C[9]],
                            [C[0],C[1],C[2],C[3],C[4],C[5]+0.1,C[6],C[7],C[8],C[9]],
                            [C[0],C[1],C[2],C[3],C[4],C[5],C[6]+0.1,C[7],C[8],C[9]],
                            [C[0],C[1],C[2],C[3],C[4],C[5],C[6],C[7]+0.1,C[8],C[9]],
                            [C[0],C[1],C[2],C[3],C[4],C[5],C[6],C[7],C[8]+0.1,C[9]],
                            [C[0],C[1],C[2],C[3],C[4],C[5],C[6],C[7],C[8],C[9]+0.1],
                            [C[0]-0.1,C[1],C[2],C[3],C[4],C[5],C[6],C[7],C[8],C[9]],
                            [C[0],C[1]-0.1,C[2],C[3],C[4],C[5],C[6],C[7],C[8],C[9]],
                            [C[0],C[1],C[2]-0.1,C[3],C[4],C[5],C[6],C[7],C[8],C[9]],
                            [C[0],C[1],C[2],C[3]-0.1,C[4],C[5],C[6],C[7],C[8],C[9]],
                            [C[0],C[1],C[2],C[3],C[4]-0.1,C[5],C[6],C[7],C[8],C[9]],
                            [C[0],C[1],C[2],C[3],C[4],C[5]-0.1,C[6],C[7],C[8],C[9]],
                            [C[0],C[1],C[2],C[3],C[4],C[5],C[6]-0.1,C[7],C[8],C[9]],
                            [C[0],C[1],C[2],C[3],C[4],C[5],C[6],C[7]-0.1,C[8],C[9]],
                            [C[0],C[1],C[2],C[3],C[4],C[5],C[6],C[7],C[8]-0.1,C[9]],
                            [C[0],C[1],C[2],C[3],C[4],C[5],C[6],C[7],C[8],C[9]-0.1]
                            ] 
                    k=(random.choice(Mmutacion))
                    
                    if cruzamineto==1:
                        print("mutacion")
                        x111=k[0]
                        x222=k[1]
                        x333=k[2]
                        x444=k[3]
                        x555=k[4]
                        y111=k[5]
                        y222=k[6]
                        y333=k[7]
                        y444=k[8]
                        y555=k[9]

                        while Af<=6.28319:
                            Rx1=(Np*x111)*math.sin(At)*math.cos(Af)
                            Rx2=(Np*x222)*math.sin(At)*math.cos(Af)
                            Rx3=(Np*x333)*math.sin(At)*math.cos(Af)
                            Rx4=(Np*x444)*math.sin(At)*math.cos(Af)
                            Rx5=(Np*x555)*math.sin(At)*math.cos(Af)
                            
                            Ry1=(Np*y111)*math.sin(At)*math.sin(Af)
                            Ry2=(Np*y222)*math.sin(At)*math.sin(Af)
                            Ry3=(Np*y333)*math.sin(At)*math.sin(Af)
                            Ry4=(Np*y444)*math.sin(At)*math.sin(Af)
                            Ry5=(Np*y555)*math.sin(At)*math.sin(Af)
                            
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
                           
                            dipolos2=T*D
                            m2dipolo.append(dipolos2)
                            #print(m2dipolo)
                            def agregar_item():
                                 todo_descripcion =  str(dipolos2)
                                 archivo=open('seleccion2.txt','a')
                                 archivo.write(todo_descripcion)
                                 archivo.write("\n")
                                 archivo.close()
                            creartxt()
                            agregar_item()
                
                            Af +=0.025
                        totaldipolomutacion2.append([m2dipolo]) 
                        totaldipolo2.append([m2dipolo]) 
                        coordenadas.append([k])
          
             if mutacion==0:
                 print("cruzamiento")
                 x1111=C[0]
                 x2222=C[1]
                 x3333=C[2]
                 x4444=C[3]
                 x5555=C[4]
                 y1111=C[5]
                 y2222=C[6]
                 y3333=C[7]
                 y4444=C[8]
                 y5555=C[9] 

                 while Af<=6.28319:
                     Rx1=(Np*x1111)*math.sin(At)*math.cos(Af)
                     Rx2=(Np*x2222)*math.sin(At)*math.cos(Af)
                     Rx3=(Np*x3333)*math.sin(At)*math.cos(Af)
                     Rx4=(Np*x4444)*math.sin(At)*math.cos(Af)
                     Rx5=(Np*x5555)*math.sin(At)*math.cos(Af)
                     
                     Ry1=(Np*y1111)*math.sin(At)*math.sin(Af)
                     Ry2=(Np*y2222)*math.sin(At)*math.sin(Af)
                     Ry3=(Np*y3333)*math.sin(At)*math.sin(Af)
                     Ry4=(Np*y4444)*math.sin(At)*math.sin(Af)
                     Ry5=(Np*y5555)*math.sin(At)*math.sin(Af)
                     
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
                    
                     dipolos3=T*D
                     m3dipolo.append(dipolos3)
                     #print(m2dipolo)
                     def agregar_item():
                          todo_descripcion =  str(dipolos3)
                          archivo=open('seleccion3.txt','a')
                          archivo.write(todo_descripcion)
                          archivo.write("\n")
                          archivo.close()
                     creartxt()
                     agregar_item()
         
                     Af +=0.025
                 totaldipolocruzamineto3.append([m3dipolo]) 
                 totaldipolo2.append([m3dipolo])  
                 coordenadas.append([C])
   
def creartxt():
      archivo=open('segundonum2.txt','a')
      archivo.close()     
remove('segundonum2.txt')
numlistas=(len(totaldipolo2))
for q in range(numlistas):
    w=totaldipolo2[q]
    a = str(w)[1:-1]
    a=literal_eval(a)
    s=sorted(a)[-2]
    
    def agregar_item():
        todo_descripcion =  str(s)
        archivo=open('segundonum2.txt','a')
        archivo.write(todo_descripcion)
        archivo.write("\n")
        archivo.close()
    creartxt()
    agregar_item()    
    
