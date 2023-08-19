#9) Restaurante importado: Escriba un programa que esté en otro archivo que la clase Restaurante del ejercicio 4, e impórtela
#al módulo actual. Cree una instancia de Restaurante y llame a alguno de sus métodos para asegurarse que la importación
#funcionó.

class Restaurante():
    def __init__(self, restaurante_nombre, tipo_comida):
        self.restaurante_nombre = restaurante_nombre
        self.tipo_comida = tipo_comida

    def describir_restaurante(self):
        print("Restaurante", self.restaurante_nombre)
        print("Tipo de comida:", self.tipo_comida)

    def abrir_restaurante(self):
        print(self.restaurante_nombre, " ahora está abierto!")

#class Heladeria(Restaurante):
#    def __init__(self, restaurante_nombre, tipo_comida, sabores):
#        Restaurante.__init__(self, restaurante_nombre, tipo_comida)
#        self.sabores = sabores

#    def mostrar_sabores(self):
#        print("Sabores de helado disponibles:")
#        for sabor in self.sabores:
#            print("- " + sabor)

#sabores_heladeria = ["Sambayon", "Cereza", "Mascarpone", "Banana Split"]
#heladeria = Heladeria("KnDs", "Heladería", sabores_heladeria)
#heladeria.describir_restaurante()
#heladeria.mostrar_sabores()
#heladeria.abrir_restaurante()