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
    n_digitos = 0
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