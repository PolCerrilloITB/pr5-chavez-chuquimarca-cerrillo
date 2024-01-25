"""
Franco Chavez/Jordi Chuquimarca/Pol Cerrillo
23/01/2023
ASIXc1C M03 UF1
Descripcion: Programa que generi una llista de 100 nombres aleatoris entre 1 i 50.
Obtenir la mitja dels nombres que es troben a les posicions parelles i la mitja del nombre de les posicions senars.
"""
import random

random_num = [random.randint(1, 50) for _ in range(100)]

par_sum = 0
par_cont = 0
impar_sum = 0
impar_cont = 0

for i in range(len(random_num)):
    if i % 2 == 0:
        par_sum += random_num[i]
        par_cont += 1
    else:
        impar_sum += random_num[i]
        impar_cont += 1

par_mitja = par_sum / par_cont if par_cont > 0 else 0
impar_mitja = impar_sum / impar_cont if impar_cont > 0 else 0

print("Mitja pares:", par_mitja)
print("Mitja impares:", impar_mitja)
