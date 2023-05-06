'''1) Escribir una clase llamada Rectángulo que contenga una base y una altura, y que contenga un método que devuelva el área
del rectángulo.'''

# class Rectangulo:
#     def __init__(self, base, altura):
#         self.base=base
#         self.altura=altura

#     def Area(self):
#         return self.base * self.altura

             
# rectangulo1=Rectangulo(base=int(input('ingrese base: ')), altura=int(input('ingrese altura: ')))
# area_rectangulo= rectangulo1.Area()
# print(f'El area del rectangulo es {area_rectangulo}')

'''2) Modelar una clase Mate que describa el funcionamiento de la conocida bebida tradicional argentina. La clase debe contener
como miembros:
o Un atributo para la cantidad de cebadas restantes hasta que se lava el mate (representada por un número).
o Un atributo para el estado (lleno o vacío).
o Un atributo n, que indica la cantidad máxima de cebadas.
o Un método cebar, que llena el mate con agua. Si se intenta cebar con el mate lleno, se debe lanzar una
excepción que imprima el mensaje ¡Cuidado! ¡Te quemaste!
o Un método beber, que vacía el mate y le resta una cebada disponible. Si se intenta beber un mate vacío, se
debe lanzar una excepción que imprima el mensaje: ¡El mate está vacío!
o Es posible seguir cebando y bebiendo el mate aunque no haya cebadas disponibles. En ese caso la cantidad
de cebadas restantes se mantendrá en 0, y cada vez que se intente beber se debe imprimir un mensaje de aviso:
“Advertencia: el mate está lavado.” pero no se debe lanzar una excepción.'''

# class Mate:
#     def __init__(self, n):
#         self.cebadas_restantes = n
#         self.lleno=True

#     def Cebar(self):
#         if self.lleno:
#             raise Exception('¡Cuidado! ¡Te quemaste!')
#         else:
#             self.lleno = True

#     def Beber(self):
#         if self.cebadas_restantes <=0:
#             print("Advertencia:El mate está lavado")
#         elif not self.lleno:
#             raise Exception("El mate está vacío")
#         else:
#             self.lleno = False
#             self.cebadas_restantes -= 1

 

#     def Estado(self):
#         if self.lleno:
#             return(f'El mate está lleno, quedan {self.cebadas_restantes} cebadas disponibles')
#         elif self.cebadas_restantes <= 0:
#             return("El mate está lavado")
#         else:
#             return("El mate está vacío")
        


# mi_mate = Mate(6)

# print(mi_mate.Estado())

# try:
#     mi_mate.Cebar()
#     print(mi_mate.Estado())
# except Exception as e:
#     print(e)

# try:
#     mi_mate.Beber()
#     print(mi_mate.Estado())
# except Exception as e:
#     print(e)

# try:
#     mi_mate.Cebar()
#     print(mi_mate.Estado())
# except Exception as e:
#     print(e)

# while mi_mate.cebadas_restantes > 0 and mi_mate.lleno:
#     try:
#         mi_mate.Beber()
#         print(mi_mate.Estado())
#     except Exception as e:
#         print(e)

# try:
#     mi_mate.Beber()
#     print(mi_mate.Estado())
# except Exception as e:
#     print(e)

'''3) Botella y Sacacorchos
 Escribir una clase Corcho, que contenga un atributo bodega (cadena con el nombre de la bodega).
 Escribir una clase Botella que contenga un atributo corcho con una referencia al corcho que la tapa, o None si está
destapada.
 Escribir una clase Sacacorchos que tenga un método destapar que le reciba una botella, le saque el corcho y se guarde
una referencia al corcho sacado. Debe lanzar una excepción en el caso en que la botella ya esté destapada, o si el
sacacorchos ya contiene un corcho.
 Agregar un método limpiar, que saque el corcho del sacacorchos, o lance una excepción en el caso en el que no haya
un corcho'''

# class Corcho:
#     def __init__(self, bodega):
#         self.bodega = bodega

# class Botella:
#     def __init__(self, corcho=None):
#         self.corcho = corcho
    
#     def destapar(self, sacacorchos):
#         if self.corcho is not None:
#             raise Exception("La botella ya está destapada")
#         if sacacorchos.corcho is not None:
#             raise Exception("El sacacorchos ya tiene un corcho")
#         corcho = Corcho("Bodega X")
#         self.corcho = corcho
#         sacacorchos.corcho = corcho
    
#     def tapar(self, sacacorchos):
#         if self.corcho is None:
#             raise Exception("La botella ya está destapada")
#         if sacacorchos.corcho is None:
#             raise Exception("El sacacorchos no tiene un corcho")
#         self.corcho = None
#         sacacorchos.corcho = None

# class Sacacorchos:
#     def __init__(self):
#         self.corcho = None
    
#     def destapar(self, botella):
#         botella.destapar(self)
    
#     def limpiar(self):
#         if self.corcho is None:
#             raise Exception("El sacacorchos no tiene un corcho")
#         self.corcho = None

# corcho = Corcho("Bodega A")

# botella = Botella(corcho)

# sacacorchos = Sacacorchos()

# try:
#     sacacorchos.destapar(botella)
#     print("Botella destapada!")
# except Exception as e:
#     print(e)

# try:
#     sacacorchos.destapar(botella)
# except Exception as e:
#     print(e)

# try:
#     sacacorchos.limpiar()
#     print("Corcho limpiado!")
# except Exception as e:
#     print(e)

# try:
#     sacacorchos.limpiar()
# except Exception as e:
#     print(e)        


'''4) Una heladería es un tipo especial de restaurante. Cree una clase Restaurante, cuyo método __init__() guarde dos atributos:
restaurante_nombre y tipo_comida. Cree un método describir_restaurante() que muestre estas piezas de información, y un
método abrir_restaurante() que muestre un mensaje indicando que el restaurante ahora está abierto. Luego cree una clase
Heladeria que herede de Restaurante, y agregue a los existentes un atributo llamado sabores que almacene una lista de los
sabores de helado disponibles. Escriba también un método que muestre estos valores, cree una instancia de la clase y llame
al método. '''

# class Restaurante:
#     def __init__(self, restaurante_nombre, tipo_comida):
#         self.restaurante_nombre = restaurante_nombre
#         self.tipo_comida = tipo_comida

#     def describir_restaurante(self):
#         print(f"Restaurante {self.restaurante_nombre}, especializado en comida {self.tipo_comida}.")

#     def abrir_restaurante(self):
#         print(f"El restaurante {self.restaurante_nombre} ahora está abierto.")


# class Heladeria(Restaurante):
#     def __init__(self, restaurante_nombre, tipo_comida, sabores):
#         super().__init__(restaurante_nombre, tipo_comida)
#         self.sabores = sabores

#     def mostrar_sabores(self):
#         print("Los sabores de helado disponibles son:")
#         for sabor in self.sabores:
#             print(f"- {sabor}")


# mi_heladeria = Heladeria("La Gran Heladería", "helados", ["chocolate", "vainilla", "frutilla"])
# mi_heladeria.describir_restaurante()
# mi_heladeria.abrir_restaurante()
# mi_heladeria.mostrar_sabores()

'''5) Escribir una clase Personaje que contenga los atributos vida, posicion y velocidad, y los métodos recibir_ataque, que
reduzca la vida según una cantidad recibida y lance una excepción si la vida pasa a ser menor o igual que cero, y mover
que reciba una dirección y se mueva en esa dirección la cantidad indicada por velocidad.
 Escribir una clase Soldado que herede de Personaje, y agregue el atributo ataque y el método atacar, que reciba otro
personaje, al que le debe hacer el daño indicado por el atributo ataque.
 Escribir una clase Campesino que herede de Personaje, y agregue el atributo cosecha y el método cosechar, que
devuelva la cantidad cosechada'''

# class Personaje:
#     def __init__(self, vida, posicion, velocidad):
#         self.vida = vida
#         self.posicion = posicion
#         self.velocidad = velocidad
    
#     def recibir_ataque(self, cantidad):
#         self.vida -= cantidad
#         if self.vida <= 0:
#             raise Exception("El personaje ha muerto")
    
#     def mover(self, direccion):
#         if direccion == "arriba":
#             self.posicion[1] += self.velocidad
#         elif direccion == "abajo":
#             self.posicion[1] -= self.velocidad
#         elif direccion == "izquierda":
#             self.posicion[0] -= self.velocidad
#         elif direccion == "derecha":
#             self.posicion[0] += self.velocidad


# class Soldado(Personaje):
#     def __init__(self, vida, posicion, velocidad, ataque):
#         super().__init__(vida, posicion, velocidad)
#         self.ataque = ataque
    
#     def atacar(self, personaje):
#         personaje.recibir_ataque(self.ataque)


# class Campesino(Personaje):
#     def __init__(self, vida, posicion, velocidad, cosecha):
#         super().__init__(vida, posicion, velocidad)
#         self.cosecha = cosecha
    
#     def cosechar(self):
#         return self.cosecha
    

# "EJEMPLO"

# # Crear un soldado
# soldado = Soldado(vida=100, posicion=[0, 0], velocidad=10, ataque=20)

# # Crear un campesino
# campesino = Campesino(vida=50, posicion=[10, 10], velocidad=5, cosecha=30)

# # Mover al soldado y atacar al campesino
# soldado.mover("derecha")
# soldado.mover("arriba")
# soldado.atacar(campesino)

# # Cosechar con el campesino
# cantidad_cosechada = campesino.cosechar()

# print(f"Cantidad de cosecha obtenida: {cantidad_cosechada}")


'''6) Usuarios: Cree una clase Usuario. Cree también dos atributos nombre y apellido, así como otros atributos que típicamente
se guardan en un perfil de usuario. Escriba un método describir_usuario() que muestre un resumen de la información del
usuario. Escriba otro método saludar_usuario() que muestre un saludo personalizado al usuario.
Cree varias instancias que representen distintos usuarios y llame ambos métodos para cada uno.'''

# class Usuario:
#     def __init__(self, nombre, apellido, edad, correo_electronico, ciudad, pais):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#         self.correo_electronico = correo_electronico
#         self.ciudad = ciudad
#         self.pais = pais
        
#     def describir_usuario(self):
#         print(f"Nombre: {self.nombre}")
#         print(f"Apellido: {self.apellido}")
#         print(f"Edad: {self.edad}")
#         print(f"Correo electrónico: {self.correo_electronico}")
#         print(f"Ciudad: {self.ciudad}")
#         print(f"País: {self.pais}")
        
#     def saludar_usuario(self):
#         print(f"Hola, {self.nombre}! ¡Bienvenido de nuevo a nuestra plataforma!")


        
# usuario1 = Usuario("Matias", "Nasser", 21, "matiasnicolasnasser01@gmail.com", "Salta", "Argentina")
# usuario2 = Usuario("Maria", "Nasser", 15, "marivalenasser@egmail.com", "Buenos Aires", "Argentina")
# usuario3 = Usuario("Pedro", "Guzman", 35, "pedro.guzman@gmail.com", "Rio de Janeiro", "Brasil")

# usuario1.describir_usuario()
# usuario1.saludar_usuario()

# usuario2.describir_usuario()
# usuario2.saludar_usuario()

# usuario3.describir_usuario()
# usuario3.saludar_usuario()


'''7) Admin: Un administrador es un tipo de usuario con privilegios especiales. Cree una clase Admin que herede de la clase
Usuario del ejercicio anterior y agréguele un atributo privilegios que almacene una lista de strings tales como “puede
postear en el foro”, “puede borrar un post”, “puede banear usuario”, etc. Escriba un método mostrar_privilegios() que
muestre el conjunto de privilegios del administrador, cree una instancia de la clase y llame al método.'''


# class Admin(Usuario):
#     def __init__(self, nombre, apellido, edad, correo_electronico, ciudad, pais, privilegios):
#         super().__init__(nombre, apellido, edad, correo_electronico, ciudad, pais)
#         self.privilegios = privilegios
        
#     def mostrar_privilegios(self):
#         print(f"Los privilegios del administrador {self.nombre} {self.apellido} son: ")
#         for privilegio in self.privilegios:
#             print(privilegio)

# admin1 = Admin("Matias", "Nasser", 21, "matiasnicolasnasser@gmail.com", "Salta", "Argentina", ["puede postear en el foro", "puede borrar un post", "puede banear usuario"])
# admin1.mostrar_privilegios()            

'''8) Privilegios: Escriba una clase Privilegios. La clase debería tener un atributo, privilegios, que almacene una lista de strings
con los privilegios de manera similar a la del ejercicio 7. Mueva el método mostrar_privilegios() de ese ejercicio a esta
clase, y haga que una instancia de esta clase sea un atributo de la clase Admin. Cree una nueva instancia de Admin y use
el método para mostrar privilegios'''


# class Privilegios:
#     def __init__(self, privilegios):
#         self.privilegios = privilegios
        
#     def mostrar_privilegios(self):
#         print("Los privilegios son: ")
#         for privilegio in self.privilegios:
#             print(privilegio)

# class Admin(Usuario):
#     def __init__(self, nombre, apellido, edad, correo_electronico, ciudad, pais, privilegios):
#         super().__init__(nombre, apellido, edad, correo_electronico, ciudad, pais)
#         self.privilegios = Privilegios(privilegios)
        
#     def mostrar_privilegios(self):
#         self.privilegios.mostrar_privilegios()            


# admin2 = Admin("María", "González", 28, "maria.gonzalez@example.com", "Barcelona", "España", ["puede editar perfiles", "puede eliminar cuentas"])
# admin2.mostrar_privilegios()        


'''9) Restaurante importado: Escriba un programa que esté en otro archivo que la clase Restaurante del ejercicio 4, e impórtela
al módulo actual. Cree una instancia de Restaurante y llame a alguno de sus métodos para asegurarse que la importación
funcionó.'''

# from restaurante import Restaurante
# restaurante1=Restaurante("Las hamburguesas de la abuela", "Rapida")
# restaurante1.describir_restaurante()


'''10) (Opcional): Repita el ejercicio anterior pero esta vez importando la clase Heladeria. ¿Qué se necesita para que funcione la
importación?'''

# from heladeria import Heladeria

# heladeria1 = Heladeria("La Heladería del Pueblo", "Helados", ["dulce de leche", "banana", "menta granizado"])
# heladeria1.describir_restaurante()
# heladeria1.mostrar_sabores()