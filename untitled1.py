# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 13:25:02 2023

@author: wzamb
"""
import os

directorio = "proyecto de grado/"  # reemplaza con el nombre de tu directorio

for archivo in os.listdir(directorio):
    if archivo.endswith(".txt"):
        ruta = os.path.join(directorio, archivo)
        with open(ruta, "w") as archivo_vacio:
            archivo_vacio.write("")
