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

#1. Para cada uno de los siguientes casos, distinga el tipo de error y describa por qué
#se da:
#▪ print(5/0): El error es ZeroDivisionError, que es cuando un nuero es dividio por cero
#▪ print 3: El error es SyntaxError,  En Python, la función print() debe tener paréntesis 
#alrededor de los argumentos que se van a imprimir. Debería ser print(3)
#▪ int(‘hola’): El error es ValueError, ya que un scring no puede ser expresado como int
#▪ res = 3 + ‘5’: El error es TypeError, y sucede porque no se puede sumar un string con un int.



        






