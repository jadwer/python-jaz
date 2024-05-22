print("Hola mundo")

# funciones
# f(x) = 2x
# f(3) = 2(3)
# f(3) = 6
# suma(x, y) = x + y
# suma(2, 3) = 2 + 3 = 5

def suma (x, y) :
    suma = x + y
    return suma

primerSuma = suma(2,3)

print("Suma:", primerSuma)

# dato --> | funcion(dato)  | --> resultado --> Cajita[primerSuma]

# Ejercicio 1:
# Escribe una función que multiplique dos números

def multi(x, y) :
    multi = x * y
    return multi

num1 = 2
num2 = 3

print("Multiplicación de", num1, "y", num2,"es :", multi(num1,num2))
# Ejercicio 2:
# Escribe una función que haga el promedio de 5 números

def promedio(numeros) :
    suma = 0
    for numero in range(len(numeros)): # para cada número en el rango(numeros que hay)
        suma = suma + numeros[numero]
    promedio = suma / len(numeros)
    return promedio

lista = [9, 9, 9, 10, 10]

print("El promedio de", lista, "es", promedio(lista))

# suma = 0
# suma = suma + lista[] //loop lista[2, 2, 3]
# 2, 

# Ejercicio: Escribir en el pizarrón 500 veces "Debo de aprender a programar python"
for i in range(500) :
    print (i + 1,": Debo aprender a programar en python")

# Ejercicio 3:
# Escribe una función que haga la suma de dos números complejos
# ejemplo: (3 + i5) + (2 + i3) = (5 + i8)
# sumaComplejos(3,5,2,3)