# Declaracion de variables
K = cambio = digito = temp = cont = cont_izquierda = 0
tamano_mitad = 0
mitad_derecha = 0
n_digitos_par = True

# Inicializar variables
K = int(input("Ingrese el valor de K (minimo tres numeros) = "))
temp = K

# Contar digitos
while temp > 0:
    cont += 1
    temp //= 10

# comprobar que el valor sea valido
if (cont < 3):
    print("valor K no valido. Intente de nuevo, reinicie el programa")
else: # Es valido

    # Calculamos el tamaño de la mitad
    tamano_mitad = cont // 2

    # Comprobamos si tiene numero de digitos impar
    if cont % 2 == 1:
        n_digitos_par = False

    # Buscamos la mitad derecha
    temp = K
    for a in range(tamano_mitad):
        digito = temp % 10
        temp = temp // 10
        mitad_derecha += digito * 10**(a+1)
        #print("md = ", mitad_derecha)

    # Si el numero es impar se añade el digito de el medio
    if n_digitos_par == False:
        digito = temp % 10
        temp = temp // 10
        cambio = mitad_derecha + digito
    # De se par se elimina el 0 adicional
    else:
        cambio = mitad_derecha // 10

    # Buscamos la mitad Izquierda
    mitad_izquierda = temp

    # Contar digitos de mitad izquierda
    while temp > 0:
        cont_izquierda += 1
        temp //= 10

    # Añadimos los 0 para la mitad izquierda
    cambio *= 10**cont_izquierda

    # Añadimos la mitad izquierda
    cambio += mitad_izquierda

    # Imprimimos el resultado final
    print("Numero con el cambio: ", cambio)


# declaracion de variables y asignacion de valor inicial de K
k = int(input("Ingrese un numero entero con al menos tres(3) digitos -> "))
n_digitos = digito = n_final = 0
aux = inicial = k

# Verificar la cantidad de digitos de K
while aux > 0:
    aux //= 10
    n_digitos += 1

# En caso de que no tenga al menos tres digitos emite un mensaje de error y te pide ingresar de nuevo el valor de K
# Repite el proceso hasta que K sea valido
while n_digitos < 3:
    print("Numero no valido intente de nuevo.")
    print()
    k = int(input("Ingrese un numero entero con al menos tres(3) digitos -> "))
    inicial = k
    aux = k
    while aux > 0:
        aux = aux // 10
        n_digitos += 1

# Se descompone K por digitos y se añaden a n_final, solo lo hace con la mitad derecha
for i in range(n_digitos // 2):
    digito = k % 10
    k //= 10
    n_final += digito * 10**i

# Si la cantidad de digitos es impar se añade el numero del medio como se pide en enunciado
if n_digitos % 2 == 1:
    n_final *= 10
    digito = k % 10
    k //= 10
    n_final += digito

# Se Añade la mitad Izquierda a n_final, verificando el numero de digitos actual de K para añadirlo
aux = k
n_digitos = 0
while aux > 0:
    aux //= 10
    n_digitos += 1
n_final *= (10**n_digitos)
n_final += k

print()
print(" K = ", inicial, " -> Numero con el cambio: ", n_final)