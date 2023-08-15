#1- Escribir un programa que abra un archivo, lea todas sus líneas y cuente cuantas
#líneas existen en el mismo
#with open(r"C:\Users\pc\Desktop\curso Python\archivo.txt", "r") as file:
#    linea=file.readlines()
#    cantidadlineas=len(linea)
#    print("la cantidad de lineas es: ", cantidadlineas)

#2- Utilizar Python para escribir un archivo de texto que tenga 11 líneas, en cada una
#escribir lo que deseen y cerrar el archivo. Luego mostrar el contenido del archivo.

#file=open(r"escribe11.txt", "w")
#for i in range (11):
#    file.write ("hola" +"\n") #\n= salto de linea

#3- [Escribir una función] que cuente cuantos caracteres existen dentro del archivo
#creado en el punto anterior

#def contador(ruta):
#    file=open(ruta, "r")
#    contenido=file.read()
#    cantidad_caracteres=len(contenido)
#    file.close()
#    return cantidad_caracteres
#print(contador("escribe11.txt"))

#4- Escriba un programa que pida al usuario su nombre. Cuando este lo ingrese,
#muestre un mensaje de bienvenida en la pantalla, y agregue una línea donde
#registre la visita del usuario a un archivo llamado libro_invitados.txt. Asegúrese de
#que cada registro figure en una nueva línea, y de que cada nueva entrada sea
#grabada en el mismo archivo, incluso entre múltiples ejecuciones del programa
#(No hay problema con los repetidos)

#usuario=input("ingrese su nombre: ")
#while True:
#    print("bienvenido!")
#    file=open(r"libro_invitados.txt", "w")
#    file.write("nuevo registro"+"\n")
#    break





