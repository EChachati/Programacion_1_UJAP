
"""Elabore el análisis del problema y un programa en lenguaje Python que de respuesta al planteamiento
que a continuación se indica:

La sociedad de Amigos Deja  de Fumar en su preocupación por el alto índice de consumo de cigarrillo realizó una encuesta
entre los fumadores.
Para procesar los datos obtenidos lo contratan a usted para que desarrolle un programa para obtener datos estadísticos
sobre el comportamiento de los fumadores. Los datos de la encuesta se suministran de la siguiente manera

En el primer registro:

    Cantidad de fumadores encuestados

En los registros siguientes:

Nombre del fumador, Género (F: femenino, M: masculino). Cantidad de cigarrillos consumidos al día

Se requiere determinar y escribir lo siguiente:

Los nombres de los fumadores en riesgo de contraer una enfermedad pulmonar.
El porcentaje de fumadores en riesgo de contraer una enfermedad pulmonar.
El género que consume más cigarrillos.
La diferencia en la cantidad de cigarrillos consumidos con respecto al otro género.
Consideraciones:

Se considera que si una persona que fuma más de 5 cigarrillos al día es un fumadores en riesgo de contraer una enfermedad pulmonar."""
# Registro de Variables
n_encuestados = int(input("Ingrese la cantidad de fumadores a encuestar:  "))
nombre = ""
genero = ""  # F o M
cigarrillos_diarios = 0
cigarrillos_m = 0
cigarrillos_f = 0
fumadores_riesgo = 0
nombres_riesgo = "Los Fumadores en riesgo son: "
porcentaje_riesgo = 0
diferencia_entre_generos = 0

# Ciclo
for i in range(n_encuestados):

    # Registrar datos de los encuestados
    print()
    nombre = input("Ingrese nombre de la persona a encuestar:  ")
    genero = input("Ingrese genero de la persona <M> o <F>:  ")
    # Ciclo que se ejecuta en caso de que se ingrese una opcion no valida
    while (genero != "F" and genero != "M"):
        genero = input("Opcion no valida, solo puede colocar <M> o <F>:  ")
    cigarrillos_diarios = int(input("Ingrese la cantidad de cigarrillos diarios:  "))

    # Procesamiento de Datos
    if (genero == "M"):
        cigarrillos_m += cigarrillos_diarios
    else:
        cigarrillos_f += cigarrillos_diarios

    if cigarrillos_diarios > 5:
        fumadores_riesgo += 1
        nombres_riesgo += nombre + ". "

# Calculo e impresión de resultados finales
print()
print("**********Resultados Finales**********")
print()

# Los nombres de los fumadores en riesgo de contraer una enfermedad pulmonar.
print(nombres_riesgo)

# El porcentaje de fumadores en riesgo de contraer una enfermedad pulmonar.
porcentaje_riesgo = (fumadores_riesgo * 100) / n_encuestados
print("Porcentaje de fumadores en riesgo de contraer una enfermedad pulmonar:  " + str(porcentaje_riesgo) + "%")

# El género que consume más cigarrillos.
# La diferencia en la cantidad de cigarrillos consumidos con respecto al otro género.
if cigarrillos_m > cigarrillos_f:
    print("El genero que consume más cigarrillos es el genero Masculino")
    diferencia_entre_generos = cigarrillos_m - cigarrillos_f
    print("El género Masculino consume " + str(diferencia_entre_generos) + " cigarrillos más respecto al género Femenino")
elif cigarrillos_f > cigarrillos_m:
    print("El genero que consume más cigarrillos es el genero Femenino")
    diferencia_entre_generos = cigarrillos_f - cigarrillos_m
    print("El género Femenino consume " + str(diferencia_entre_generos) + " cigarrillos más respecto al genero Masculino")
else:
    print("Ambos generos consumen la misma cantidad de cigarrillos")
    diferencia_entre_generos = 0
