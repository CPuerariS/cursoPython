#1) Escribir una clase llamada Rectángulo que contenga una base y una altura, y que contenga un método que devuelva el área
#del rectángulo.

#class Rectangulo():
#    def __init__ (self, base, altura):
#        self.base= base
#        self.altura= altura

#    def area_r(self):
#        area= self.base* self.altura
#        print ("el area del rectangulo es: ", area)

#rectangulito= Rectangulo(10, 5)
#rectangulito.area_r()

#2) Modelar una clase Mate que describa el funcionamiento de la conocida bebida tradicional argentina. La clase debe contener
#como miembros:
#o Un atributo para la cantidad de cebadas restantes hasta que se lava el mate (representada por un número).
#o Un atributo para el estado (lleno o vacío).
#o Un atributo n, que indica la cantidad máxima de cebadas.

#o Un método cebar, que llena el mate con agua. Si se intenta cebar con el mate lleno, se debe lanzar una
#excepción que imprima el mensaje ¡Cuidado! ¡Te quemaste!
#o Un método beber, que vacía el mate y le resta una cebada disponible. Si se intenta beber un mate vacío, se
#debe lanzar una excepción que imprima el mensaje: ¡El mate está vacío!
#o Es posible seguir cebando y bebiendo el mate aunque no haya cebadas disponibles. En ese caso la cantidad
#de cebadas restantes se mantendrá en 0, y cada vez que se intente beber se debe imprimir un mensaje de aviso:
#“Advertencia: el mate está lavado.” pero no se debe lanzar una excepción.

#class Mate():
#    def __init__(self, cantidad_cebadas, estado, cant_max_ceb):
#        self.cantidad_cebadas= cantidad_cebadas
#        self.estado= estado
#        self.cant_max_ceb= cant_max_ceb

#    def cebar(self):
#        if self.estado == "lleno":
#            print("¡Cuidado! ¡Te quemaste!")
#        else:
#            self.estado== "lleno"
#            self.cantidad_cebadas==self.cant_max_ceb
#            print("te cebo")

#    def beber(self):
#        if self.estado == "lleno":
#            self.estado == "vacio"
#            self.cantidad_cebadas -=1
#        else:
#            raise Exception("¡El mate está vacío!")
        
#    def __str__(self):
#        return f"Estado: {self.estado}, Cebadas restantes: {self.cantidad_cebadas}"
    
#matecito= Mate (3, "lleno", 3)
#print(matecito)
#matecito.cebar()
#print(matecito)
#matecito.beber()
#print(matecito)
#matecito.beber()
#print(matecito)
#matecito.cebar()
#print(matecito)

#3) Botella y Sacacorchos
# Escribir una clase Corcho, que contenga un atributo bodega (cadena con el nombre de la bodega).
# Escribir una clase Botella que contenga un atributo corcho con una referencia al corcho que la tapa, o None si está
#destapada.
# Escribir una clase Sacacorchos que tenga un método destapar que le reciba una botella, le saque el corcho y se guarde
#una referencia al corcho sacado. Debe lanzar una excepción en el caso en que la botella ya esté destapada, o si el
#sacacorchos ya contiene un corcho.
# Agregar un método limpiar, que saque el corcho del sacacorchos, o lance una excepción en el caso en el que no haya
#un corcho.

#class Corcho:
#    def __init__(self, bodega):
#        self.bodega = bodega

#class Botella:
#    def __init__(self, corcho=None):
#        self.corcho = corcho

#class Sacacorchos:
#    def __init__(self):
#        self.corcho_extraido = None

#    def destapar(self, botella):
#        if botella.corcho is None:
#            raise Exception("La botella ya está destapada.")
        
#        if self.corcho_extraido is not None:
#            raise Exception("El sacacorchos ya contiene un corcho.")
        
#        self.corcho_extraido = botella.corcho
#        botella.corcho = None
#        print("¡Botella destapada!")

#    def limpiar(self):
#        if self.corcho_extraido is None:
#            raise Exception("No hay corcho en el sacacorchos.")

#corcho1 = Corcho("Bodega A")
#botella1 = Botella(corcho1)

#sacacorchos = Sacacorchos()

#sacacorchos.destapar(botella1)
#print("Corcho extraído:", sacacorchos.corcho_extraido.bodega)

#try:
#    sacacorchos.destapar(botella1)
#except Exception as uh:
#    print(uh)

#try:
#    sacacorchos.limpiar()
#except Exception as uh:
#    print(uh)

#4) Una heladería es un tipo especial de restaurante. Cree una clase Restaurante, cuyo método __init__() guarde dos atributos:
#restaurante_nombre y tipo_comida. Cree un método describir_restaurante() que muestre estas piezas de información, y un
#método abrir_restaurante() que muestre un mensaje indicando que el restaurante ahora está abierto. Luego cree una clase
#Heladeria que herede de Restaurante, y agregue a los existentes un atributo llamado sabores que almacene una lista de los
#sabores de helado disponibles. Escriba también un método que muestre estos valores, cree una instancia de la clase y llame
#al método.

#class Restaurante():
#    def __init__(self, restaurante_nombre, tipo_comida):
#        self.restaurante_nombre = restaurante_nombre
#        self.tipo_comida = tipo_comida

#    def describir_restaurante(self):
#        print("Restaurante", self.restaurante_nombre)
#        print("Tipo de comida:", self.tipo_comida)

#    def abrir_restaurante(self):
#        print(self.restaurante_nombre, " ahora está abierto!")

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

#5) Escribir una clase Personaje que contenga los atributos vida, posicion y velocidad, y los métodos recibir_ataque, que
#reduzca la vida según una cantidad recibida y lance una excepción si la vida pasa a ser menor o igual que cero, y mover
#que reciba una dirección y se mueva en esa dirección la cantidad indicada por velocidad.
# Escribir una clase Soldado que herede de Personaje, y agregue el atributo ataque y el método atacar, que reciba otro
#personaje, al que le debe hacer el daño indicado por el atributo ataque.
# Escribir una clase Campesino que herede de Personaje, y agregue el atributo cosecha y el método cosechar, que
#devuelva la cantidad cosechada

#class Personaje():
#    def __init__(self, vida, posicion, velocidad):
#        self.vida = vida
#        self.posicion = posicion
#        self.velocidad = velocidad

#    def recibir_ataque(self, daño):
#        self.vida -= daño
#        if self.vida<=0:
#            raise Exception ("Moriste")
        
#    def mover(self, direccion):
#        distancia = self.velocidad
#        if direccion == "izquierda":
#            self.posicion -= distancia
#        elif direccion == "derecha":
#            self.posicion += distancia
#        else:
#            print("Dirección no válida")

#class Soldado(Personaje):
#    def __init__(self, vida, posicion, velocidad, ataque):
#        super().__init__(vida, posicion, velocidad)
#        self.ataque = ataque

#    def atacar(self, npc):
#        npc.recibir_ataque(self.ataque)
#        print("el soldado ataca a ", npc, "ahora tiene ", npc.vida, " de vida")

#class Campesino(Personaje):
#    def __init__(self, vida, posicion, velocidad, cosecha):
#        super().__init__(vida, posicion, velocidad)
#        self.cosecha = cosecha

#    def cosechar(self):
#        print(f"El campesino ha cosechado {self.cosecha} unidades.")

#soldado = Soldado(100, 0, 10, 20)
#campesino = Campesino(50, 0, 5, 10)
#campesino.mover("derecha")
#campesino.cosechar()
#soldado.mover("izquierda")
#soldado.atacar(campesino)

#6) Usuarios: Cree una clase Usuario. Cree también dos atributos nombre y apellido, así como otros atributos que típicamente
#se guardan en un perfil de usuario. Escriba un método describir_usuario() que muestre un resumen de la información del
#usuario. Escriba otro método saludar_usuario() que muestre un saludo personalizado al usuario.
#Cree varias instancias que representen distintos usuarios y llame ambos métodos para cada uno.

#class Usuario:
#    def __init__(self, nombre, apellido, edad, correo):
#        self.nombre = nombre
#        self.apellido = apellido
#        self.edad = edad
#        self.correo = correo

#    def describir_usuario(self):
#        print(f"Nombre: {self.nombre}")
#        print(f"Apellido: {self.apellido}")
#        print(f"Edad: {self.edad}")
#        print(f"Correo: {self.correo}")

#    def saludar_usuario(self):
#        print(f"Hola, {self.nombre} {self.apellido}. ¡Bienvenido/a! :)")

#usuario1 = Usuario("Jose", "Johnson", 25, "jojo@ejemplo.com")
#usuario2 = Usuario("María", "González", 30, "mariagg@ejemplo.com")

#usuario1.describir_usuario()
#usuario1.saludar_usuario()
#print("  ")
#usuario2.describir_usuario()
#usuario2.saludar_usuario()

#7) Admin: Un administrador es un tipo de usuario con privilegios especiales. Cree una clase Admin que herede de la clase
#Usuario del ejercicio anterior y agréguele un atributo privilegios que almacene una lista de strings tales como “puede
#postear en el foro”, “puede borrar un post”, “puede banear usuario”, etc. Escriba un método mostrar_privilegios() que
#muestre el conjunto de privilegios del administrador, cree una instancia de la clase y llame al método.

#class Admin(Usuario):
#    def __init__(self, nombre, apellido, edad, correo, privilegios):
#        super().__init__(nombre, apellido, edad, correo)
#        self.privilegios = privilegios

#    def mostrar_privilegios(self):
#        print("Privilegios del administrador:")
#        for privilegio in self.privilegios:
#            print("- " + privilegio)

#privilegios_admin = ["Puede postear en el foro", "Puede borrar un post", "Puede banear usuarios"]
#admin = Admin("El", "Admin", 40, "admin@example.com", privilegios_admin)

#admin.describir_usuario()
#admin.saludar_usuario()
#admin.mostrar_privilegios()

#8) Privilegios: Escriba una clase Privilegios. La clase debería tener un atributo, privilegios, que almacene una lista de strings
#con los privilegios de manera similar a la del ejercicio 7. Mueva el método mostrar_privilegios() de ese ejercicio a esta
#clase, y haga que una instancia de esta clase sea un atributo de la clase Admin. Cree una nueva instancia de Admin y use
#l método para mostrar privilegios.

#class Privilegios():
#    def __init__(self, privilegios):
#        self.privilegios = privilegios

#    def mostrar_privilegios(self):
#        print("Privilegios:")
#        for privilegio in self.privilegios:
#            print("- " + privilegio)

#class Admin(Usuario):
#    def __init__(self, nombre, apellido, edad, correo, privilegios):
#        super().__init__(nombre, apellido, edad, correo)
#        self.privilegios = Privilegios(privilegios)

#9) Restaurante importado: Escriba un programa que esté en otro archivo que la clase Restaurante del ejercicio 4, e impórtela
#al módulo actual. Cree una instancia de Restaurante y llame a alguno de sus métodos para asegurarse que la importación
#funcionó.

from Restaurante_ej9_tp6 import Restaurante
mi_restaurante = Restaurante("Hungry people", "Comida internacional")
mi_restaurante.describir_restaurante()
mi_restaurante.abrir_restaurante()

#10) (Opcional): Repita el ejercicio anterior pero esta vez importando la clase Heladeria. ¿Qué se necesita para que funcione la
#importación?