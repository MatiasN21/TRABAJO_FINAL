class Restaurante:
    def __init__(self, restaurante_nombre, tipo_comida):
        self.restaurante_nombre = restaurante_nombre
        self.tipo_comida = tipo_comida

    def describir_restaurante(self):
        print(f"Restaurante {self.restaurante_nombre}, especializado en comida {self.tipo_comida}.")

    def abrir_restaurante(self):
        print(f"El restaurante {self.restaurante_nombre} ahora está abierto.")


class Heladeria(Restaurante):
    def __init__(self, restaurante_nombre, tipo_comida, sabores):
        super().__init__(restaurante_nombre, tipo_comida)
        self.sabores = sabores

    def mostrar_sabores(self):
        print("Los sabores de helado disponibles son:")
        for sabor in self.sabores:
            print(f"- {sabor}")