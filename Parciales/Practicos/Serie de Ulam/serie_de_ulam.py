"""Enunciado:
Crear una aplicación Python la cual tenga como entrada dos valores enteros, los cuales define el inicio y el fin de un
intervalo numérico, usaremos cada valor del intervalo para generar su serie de Ulam, mostraremos cada término de la
serie por pantalla, condicionado a lo siguiente: si la serie no excede los 15 términos se mostrara completa, en caso
contrario solo se mostraran los primeros 15 términos, el hecho de que la serie se muestre o no completa se debe indicar
con un mensaje al final de la misma, ver figura.
"""

initial_value = 2 #int(input("Ingrese el valor inicial -> "))
final_value = 7 #int(input("Ingrese el valor final -> "))
mas_pares = initial_value
cant_pares = 0

print("Primeros 15 terminos de la serie de Ulam de los numeros: ")

for i in range(initial_value, final_value):
    terms = 0
    ant = i
    resultado = str(i)
    cont_pares = 0
    while terms < 15 and ant != 1:
        if ant % 2 == 0:
            ant /= 2
            cont_pares += 1
        else: ant = (ant*3) +1
        resultado += " " + str(int(ant))
        terms += 1
    if terms == 15: resultado += " Solo 15 Terminos"
    else: resultado += " Serie Completa"
    print(resultado)
    if cont_pares > cant_pares:
        cant_pares = cont_pares
        mas_pares = i

print("Salida Final\nLa serie con mayor cantidad de pares es la serie del :", mas_pares, "\n\nFin del programa")