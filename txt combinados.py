# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 16:13:05 2023

@author: wzamb
"""

with open('segundonum.txt', 'r') as archivo1, open('cordenadas.txt', 'r') as archivo2, open('combinado1.txt', 'w') as combinado:
    while True:
        linea1 = archivo1.readline()
        linea2 = archivo2.readline()
        if not linea1 and not linea2:
            break
        combinado.write(linea1.strip()+" "+ linea2.strip() + '\n')
archivo1.close()
archivo2.close()
combinado.close()
with open('segundonum2.txt', 'r') as archivo1, open('cordenadas2.txt', 'r') as archivo2, open('combinado2.txt', 'w') as combinado:
    while True:
        linea1 = archivo1.readline()
        linea2 = archivo2.readline()
        if not linea1 and not linea2:
            break
        combinado.write(linea1.strip()+" "+ linea2.strip() + '\n')
archivo1.close()
archivo2.close()
combinado.close()
with open('combinado1.txt', 'r') as archivo1, open('combinado2.txt', 'r') as archivo2, open('combinado3.txt', 'w') as combinado:
    contenido1 = archivo1.read()
    combinado.write(contenido1)
    contenido2 = archivo2.read()
    combinado.write(contenido2)
archivo1.close()
archivo2.close()
combinado.close()
with open("combinado3.txt", "r") as archivo:
    lineas = archivo.readlines()
lineas_ordenadas = sorted(lineas, key=lambda x: float(x.split()[0]))
with open("datos_ordenados.txt", "w") as archivo_ordenado:
    archivo_ordenado.writelines(lineas_ordenadas)
with open('datos_ordenados.txt', 'r') as f:
    lineas = f.readlines()[:15]
with open('nuevo_archivo.txt', 'w') as f:
    for linea in lineas:
        f.write(linea)
