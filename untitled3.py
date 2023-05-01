# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 14:52:36 2023

@author: wzamb
"""

import os

archivos = ["primeraslineas.txt", "seleccion3ciclo.txt", "seleccion3.txt", "seleccion2ciclo.txt", "seleccion2.txt", "segundonum2ciclo.txt", "segundonum2.txt", "segundonum.txt", "nuevo_archivo.txt", "datos_ordenados.txt", "datos_evaluacion.txt", "datos.txt", "cordenadas2ciclo.txt", "cordenadas2.txt", "cordenadas.txt", "combinado3.txt", "combinado2.txt", "combinado1ciclo.txt", "combinado1.txt"]

for archivo in archivos:
    if os.path.exists(archivo):
        with open(archivo, "w") as f:
            f.write("")
    else:
        print("El archivo",archivo, " no existe o no se puede acceder.")
        
        
