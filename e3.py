"""
Franco Chavez/Jordi Chuquimarca/Pol Cerrillo
25/01/2023
ASIXc1C M03 UF1
Descripcion: Programa de traducció d’insults. Crear una estructura de dues dimensions amb els insults en català
i afegir la traducció en castellà, anglès i klingon
El programa, demanarà a l’usuari que escrigui per teclat un insult, en català,
i el mostrarà traduït a castellà, anglès i klingon.
"""
try:
#Hacemos una tabla de dos dimensiones en las que las filas, determinan una série de insultos en x idioma#
#En el eje de las y, cada fila está asignada del 0 al 3#

    insults = [
        ["Mocós", "Capsigrany","Fill de puta"],
        ["Mocoso", "Cabezón","Hijo de puta"],
        ["Brat", "Big head","Motherfucker"],
        ["Bach", "QI'tu'","targh ghu"]
    ]

#Pedimos que el usuario que introduzca un insulto en catalán para mostrar en pantalla la traducción en diferentes idiomas#

    insult_CATALÀ = input("Introduce un insulto en catalán: ")

#En "insult" determinaremos del 0 al 2, en el eje de las x, la posición del insulto en catalán de la primera fila#
#En "insults" determinaremos el número de fila (eje de las y) y del 0 al 3 el insulto que queremos que imprima en x idioma#

    for insult in insults:
        if insult [0] == insult_CATALÀ:
            print(f"En catalán: {insults[0][0]}")
            print(f"En castellano: {insults[1][0]}")
            print(f"En inglés: {insults[2][0]}")
            print(f"En klingon: {insults[3][0]}")

    for insult in insults:
        if insult [1] == insult_CATALÀ:
            print(f"En catalán: {insults[0][1]}")
            print(f"En castellano: {insults[1][1]}")
            print(f"En inglés: {insults[2][1]}")
            print(f"En klingon: {insults[3][1]}")

    for insult in insults:
        if insult [2] == insult_CATALÀ:
            print(f"En catalán: {insults[0][2]}")
            print(f"En castellano: {insults[1][2]}")
            print(f"En inglés: {insults[2][2]}")
            print(f"En klingon: {insults[3][2]}")
except:
    print("Una paraula!!!!")
