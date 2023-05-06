'''1. Escriba una función redondear() que permita redondear un número
decimal de acuerdo al criterio: Si el número es mayor a 3.50, devolver el
entero siguiente (en este caso, 4), si no devolver el entero inmediatamente
anterior (3). '''

def redondear(num):
    if num > 3.5:
        return int(num + 1)
    else:
        return int(num)
    
'''EJEMPLO'''

num1=redondear(3.5)
print(num1)

num2=redondear(3.6)
print(num2)


'''2. Coloque el módulo del ejercicio anterior dentro de un paquete. En un
módulo que esté fuera de ese paquete, cree una función de suma de
decimales que redondee el resultado haciendo uso de la función
redondear() del paquete recién creado.'''

