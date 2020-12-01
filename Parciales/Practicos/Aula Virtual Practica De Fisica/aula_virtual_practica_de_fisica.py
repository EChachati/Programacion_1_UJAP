archivo = open("virtual.txt")

# Informacion para resultados finales
primero_mayor_16 = False
nombre_mayor_16 = "No hay estudiantes con notas mayores a 16 puntos"

nombre_mejor = ""
tiempo_mejor = 9999
nota_mejor = -1
cuantos_mejores = 0

reprobados_con_mas_dos_envios = 0
reprobados = 0

promedio_aprobados_en_2h = 0
aprobados_en_2h = 0

print("{0:10s}    {1:10s}    {2:10s}    {3:10s}    {4:10s}".format("Nombre", "Tiempo", "Envios", "Nota", "Estatus"))
for registro in archivo:
    # Cargando datos del estudiante
    campos = registro.split(",")
    nombre = campos[0]
    hora_inicio, minuto_inicio = int(campos[1]), int(campos[2])
    hora_final, minuto_final = int(campos[3]), int(campos[4])
    envio1, envio2, envio3, envio4 = int(campos[5]), int(campos[6]), int(campos[7]), int(campos[8])

    # Calculando datos Restantes
    duracion = (hora_final * 60 - minuto_final) - (hora_inicio * 60 + minuto_inicio)
    envios = 0
    if envio4 > 0:
        envios += 1
    if envio1 > 0:
        envios += 1
    if envio2 > 0:
        envios += 1
    if envio3 > 0:
        envios += 1
    nota = (envio1 * 0.25) + (envio2 * 0.25) + (envio3 * 0.25) + (envio4 * 0.25)
    estatus = ""
    if nota >= 9.5:
        estatus = "Aprobo Practica"
        if duracion < 120:
            aprobados_en_2h += 1
            promedio_aprobados_en_2h += nota
    else:
        estatus = "Reprobo Practica"
        reprobados += 1
        if envios >= 2:
            reprobados_con_mas_dos_envios += 1

    # Impresion de Datos
    print("{0:10s}    {1:5d}       {2:5d}       {3:8.2f}          {4:10s}".format(nombre, duracion, envios, nota,
                                                                                  estatus))

    # Verificacion para resultados finales
    if nota > 16 and primero_mayor_16 == False:
        nombre_mayor_16 = nombre
        primero_mayor_16 = True

    if nota > nota_mejor:
        nombre_mejor = nombre
        nota_mejor = nota
        tiempo_mejor = duracion
        cuantos_mejores = 1
    elif nota == nota_mejor and duracion < tiempo_mejor:
        nombre_mejor = nombre
        nota_mejor = nota
        tiempo_mejor = duracion
        cuantos_mejores = 1
    elif nota == nota_mejor and duracion == tiempo_mejor:
        cuantos_mejores += 1

    # Calculos finales
porcentaje_reprobados_2 = (reprobados_con_mas_dos_envios * 100) / reprobados
promedio_aprobados_en_2h /= aprobados_en_2h

# Imprimir Resultados finales
print()
print("*************** Resultados Finales ***************")
print()
print("Primer Estudiante con nota mayor a 16 puntos: ", nombre_mayor_16)
print("Estudiante con la mayor nota: ", nombre_mejor)
print("Tiempo con la mejor nota: ", tiempo_mejor)
print("Mejor Nota: ", nota_mejor)
if cuantos_mejores > 1:
    print("Hubo {0:2d} con la mejor nota".format(cuantos_mejores))
print("Porcentaje de reprobados con dos envios: {0:3.1f}".format(porcentaje_reprobados_2))
print("Nota promedio aprobados en menos de 2 horas: {0:2.1f}".format(promedio_aprobados_en_2h))
print()
print("****************************")
print("***** Fin del Programa *****")
print("****************************")
