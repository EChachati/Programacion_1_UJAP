
lista = [1231, 2343, 2242, 31236520, 43457, 1241, 1245]
lista_primos = lista
suma_primos = 0
primo_mayor = 0
for i in range(len(lista)):
    mayor_digito = 0
    menor_digito = 10
    cant_digitos = dig_2 = suma_dig = cant_dig_primos = 0
    # Primo
    for j in range(2, lista[i]):
        primo = "Si"
        if lista[i] % j == 0:
            primo = "No"
        if primo == "Si" and lista[i] > primo_mayor:
            primo_mayor = lista[i]

    # Suma Primos
    suma_primos += lista_primos[i]

    # Verificar digitos
    n = lista[i]
    while n > 0:
        dig = n % 10
        n //= 10
        cant_digitos += 1
        if dig == 2:
            dig_2 += 1
        if dig > mayor_digito and dig % 2 == 0:
            mayor_digito = dig
        if dig < menor_digito and dig % 2 == 1:
            menor_digito = dig
        suma_dig += dig

        cant_dig_primos += 1
        for k in range(2, dig):
            if (dig % k == 0):
                cant_dig_primos -= 1
                break
    prop_dig_2 = (dig_2 * 1) / cant_digitos
    prom_dig = suma_dig / cant_digitos
    prop_dig_prim = (cant_dig_primos * 1) / cant_digitos
    print("""Resultado De {0:5d}
    El Numero es Primo : {1:2}
    Suma de Numeros Primos Actual :  {2:6d}
    Proporcion de Digitos igual a 2 : {3:2.2f}
    Promedio Suma de Todos los Digitos : {4:1.2f}
    Mayor Digito Par : {5:1d}
    Menor Digito Impar : {6:1d}
    Proporcion Digitos Primos : {7:2.2f}
    Primo Mayor : {8:10d}
    """.format(lista[i], primo, suma_primos, prop_dig_2, prom_dig, mayor_digito, menor_digito, prop_dig_prim,
               primo_mayor))
