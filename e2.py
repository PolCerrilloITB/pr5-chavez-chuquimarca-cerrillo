"""
Franco Chavez/Jordi Chuquimarca/Pol Cerrillo
23/01/2023
ASIXc1C M03 UF1
Descripcion:Programa que generi una llista de 100 nombres aleatoris entre 1 i 50. Obtenir la mitja dels nombres que es troben a les posicions parelles i la mitja del nombre de les posicions senars.
Per aconseguir nombres aleatoris en Python podem utilitzar la funció random.randint(limitInferior,limitSuperior)
"""
import random

suma_pares = 0
suma_impares = 0
tupla = []

for x in range (1,51):
    tupla.append(random.randint(1,50))
