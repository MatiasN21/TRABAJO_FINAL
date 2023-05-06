'''1)Escriba una función que muestre todos los números primos entre 1 y un número n que es
ingresado por parámetro'''

# def numeros_primos(n):
#     lista_primos = []
#     for num in range(2, n+1):
#         if all(num % i != 0 for i in range(2, int(num**0.5)+1)):
#             lista_primos.append(num)
#     return lista_primos

# print(numeros_primos(20))


'''2) Escriba una función que le pida al usuario ingresar condimentos para un sándwich, hasta
que el usuario ingrese ‘salir’. Cada vez que se ingrese un condimento, muestre un mensaje
avisando que ya se agregó el condimento al sándwich. Escriba versiones diferentes del
programa de acuerdo a estos criterios:
• Use un test condicional en el ciclo while para detener la ejecución.
• Use un test condicional dentro del ciclo para decidir si continuar la ejecución.'''

'''TEST CONDICIONAL EN CICLO WHILE'''

# def armar_sandwich_1():
#     condimento = ''
#     while condimento != 'salir':
#         condimento = input("Ingrese un condimento para su sándwich (o 'salir' para terminar): ")
#         if condimento != 'salir':
#             print(f"Se ha agregado {condimento} a su sándwich.")

# armar_sandwich_1()     


'''TEST CONDICIONAL DENTRO DEL CICLO '''

# def armar_sandwich_2():
#     while True:
#         condimento = input("Ingrese un condimento para su sándwich (o 'salir' para terminar): ")
#         if condimento == 'salir':
#             break
#         print(f"Se ha agregado {condimento} a su sándwich.")

# armar_sandwich_2()        

'''3) 
A) Remera: Escriba una función “hacer_remera()” que tome como parámetros un
tamaño y el mensaje que debería ir impreso en la remera. La función debe mostrar un mensaje
describiendo el tamaño de la remera y el mensaje impreso en ella. Llame la función una vez
usando argumentos por posición. Llámela una segunda vez usando argumentos por clave.'''


# def hacer_remera(tamaño, mensaje):
#     print(f"Se ha creado una remera de tamaño {tamaño} con el mensaje '{mensaje}'.")

# hacer_remera('S', 'Viva la vida loca')

# hacer_remera(mensaje='viva la vida loca', tamaño='S' )

'''B) Remeras Grandes: Modifique la “funcion hacer_remera()” para que el tamaño por
defecto sea ‘L’ y el mensaje, ‘Me gusta Python’. Haga un par de remeras, la primera con los
valores por defecto, y la segunda con valores diferentes.'''

# def hacer_remera(tamaño='L', mensaje='Me gusta Python'):
#     print(f"Se ha creado una remera de tamaño {tamaño} con el mensaje '{mensaje}'.")

# hacer_remera()    

# hacer_remera('M', 'Me gusta el Java')

'''4) Serie de Fibonacci: Escriba una función fibonacci(n) que devuelva los n primeros numeros
de la serie de Fibonacci. En esta serie, los primeros dos números son 0 y 1, y cada sucesivo
número es la suma de los dos números inmediatamente anteriores (ejemplo: 0,1,1,2,3,5,8, …). '''

# def fibonacci(n):
#     fib = [0, 1]
#     while len(fib) < n:
#      fib.append(fib[-1] + fib[-2])
#     return fib[:n]

# print (fibonacci(10))

'''5) Calculadora más inteligente: Modifique el ejercicio 9 del primer practico para que
la calculadora sea capaz de devolver el resultado solamente de una operación especificada por
el usuario. Por ejemplo, si el usuario ingresa dos numeros x, y, y luego ingresa ‘1’, la
calculadora devuelve la suma entre los numeros x,y; si ingresa ‘2’, devuelve la resta, etc.'''

# def calcular():
#     x = float(input("Ingrese el primer número: "))
#     y = float(input("Ingrese el segundo número: "))
#     operacion = int(input("Ingrese el número de la operación que desea realizar:\n1 - Suma\n2 - Resta\n3 - Multiplicación\n4 - División\n"))

#     if operacion == 1:
#         resultado = x + y
#         print("El resultado de la suma es:", resultado)
#     elif operacion == 2:
#         resultado = x - y
#         print("El resultado de la resta es:", resultado)
#     elif operacion == 3:
#         resultado = x * y
#         print("El resultado de la multiplicación es:", resultado)
#     elif operacion == 4:
#         if y == 0:
#             print("No se puede dividir por cero.")
#         else:
#             resultado = x / y
#             print("El resultado de la división es:", resultado)
#     else:
#         print("Operación inválida. Por favor, ingrese un número entre 1 y 4.")


# calcular()

'''6) (Opcional) Conversión imperial: Desarrollar un programa en Python que pueda convertir
gramos a libras, centímetros a pulgadas y kilómetros a millas. El programa debe permitir la
conversión en ambos sentidos. 1.60934 Km = 1 milla 0.393701 pulgadas = 1 cm 0.00220462
libras = 1 gramo '''

# def convertir_medida(valor, medida):
#     if medida == "gramos":
#         libras = valor * 0.00220462
#         return f"{valor} gramos son {libras:.4f} libras"
#     elif medida == "libras":
#         gramos = valor / 0.00220462
#         return f"{valor} libras son {gramos:.4f} gramos"
#     elif medida == "centimetros":
#         pulgadas = valor * 0.393701
#         return f"{valor} centímetros son {pulgadas:.4f} pulgadas"
#     elif medida == "pulgadas":
#         centimetros = valor / 0.393701
#         return f"{valor} pulgadas son {centimetros:.4f} centímetros"
#     elif medida == "kilometros":
#         millas = valor / 1.60934
#         return f"{valor} kilómetros son {millas:.4f} millas"
#     elif medida == "millas":
#         kilometros = valor * 1.60934
#         return f"{valor} millas son {kilometros:.4f} kilómetros"
#     else:
#         return "Medida no válida"
     

    
'''Ejemplo'''

# valor=float(input('Ingrese valor a combertir: '))
# print(convertir_medida(valor, "gramos"))
# print(convertir_medida(valor, "libras")) 
# print(convertir_medida(valor, "centimetros"))
# print(convertir_medida(valor, "pulgadas")) 
# print(convertir_medida(valor, "kilometros")) 
# print(convertir_medida(valor, "millas")) 
#
