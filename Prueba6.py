#Crear una clase gato que contenga 5 atributos (Nombre, Color de pelo, color de
#ojos, cansancio y hambre) y 4 métodos (Comer, Dormir, Jugar, Acariciar). Luego
#instanciar 3 objetos de la clase gato con distintos atributos y utilizar sus
#Metodos.

class gato():
    def __init__(self, nombre, colorpelo, colorojos, cansancio, hambre):
        self.nombre=nombre
        self.colorpelo=colorpelo
        self.colorojos=colorojos
        self.cansancio=cansancio
        self.hambre=hambre

    def comer(self):
        print(self.nombre, "tiene hambre, alimentlo")

    def dormir(self):
        print("el gato tiene: ", self.cansancio, ", necesita dormir!")

    def jugar(self):
        print ("momento de jugar")

    def acariciar(self):
        print ("prr")

gato("jorge","negro","amarillos", 10, 10)




        






