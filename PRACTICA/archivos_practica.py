'''1- Escribir un programa que abra un archivo, lea todas sus líneas y cuente cuantas
líneas existen en el mismo'''

# file=open('texto.txt', 'r')
# file1=file.readlines()
# print(file1)
# lineas=len(file1)
# print(lineas)


'''2- Utilizar Python para escribir un archivo de texto que tenga 11 líneas, en cada una
escribir lo que deseen y cerrar el archivo. Luego mostrar el contenido del archivo.'''

# with open('texto2.txt', 'w',) as f:
#     for i in range(11):
#         linea=input(f'Escriba la linea {i}: ') + '\n'
#         f.write(linea)
     
'''3- [Escribir una función] que cuente cuantos caracteres existen dentro del archivo
creado en el punto anterior'''

# def ContarCaracteres(Archivo):
#     f=open(Archivo, 'r')
#     lineas=f.readlines()
#     contador=0
#     for linea in lineas:
#         linea=linea.strip()
#         contador += len(linea)
#     f.close()
#     return contador
# print(ContarCaracteres('texto2.txt'))    
    

'''▪ 4- Escriba un programa que pida al usuario su nombre. Cuando este lo ingrese,
muestre un mensaje de bienvenida en la pantalla, y agregue una línea donde
registre la visita del usuario a un archivo llamado libro_invitados.txt. Asegúrese de
que cada registro figure en una nueva línea, y de que cada nueva entrada sea
grabada en el mismo archivo, incluso entre múltiples ejecuciones del programa
(No hay problema con los repetidos)''' 

# with open('libro_invitados.txt', 'a') as f:
#     usuario=input('Ingrese su nomnbre:') + '\n'
#     print('Bienvenido', usuario )
#     f.write(usuario)


'''5- Escribir un programa que copie los contenidos de un archivo A y los vuelque en un
archivo B'''

# with open('libro_invitados.txt', 'r') as archivo_A:
#     contenido=archivo_A.read()
# with open('texto.txt', 'w') as archivo_B:
#     archivo_B.write(contenido)




  
