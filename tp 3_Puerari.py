#1) Meter los números del 1 al 20 en una lista y mostrarla en pantalla. Hacer lo mismo
#para un rango de números indicado por un usuario.

#  a)
#lista=[]
#for elemento in range (1,21):
#    lista.append (elemento)
#print ("lista de 1 al 20: ", lista)

#  b)
#inicio = int(input("ingrese desde que numero se tomara en cuenta: "))
#fin = int(input("ingrese hasta que numero se tomara en cuenta: "))
#lista=[]
#while inicio<=fin:
#    lista.append (inicio)
#    inicio+= 1
#print ("lista: ", lista)

#2) Pide un número y guarda en una lista su tabla de multiplicar hasta el 10. Por
#ejemplo, si pide el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50

#lista=[]
#numero= int(input("ingrese un numero: "))
#for elemento in range(1,11):
#    lista.append (numero*elemento)
#print ("tabla de multiplicar hasta el 10: ", lista)

#3) Pide una cadena (string) por teclado, mete los caracteres en una lista sin repetir
#caracteres.

#cadena = input("Ingrese caracteres: ")
#lista = []
#
#for caracter in cadena:
#    if caracter not in lista:
#        lista.append(caracter)
#print("Lista de caracteres ingresados:", lista)

#4) Pide una cadena (string) por teclado, mete los caracteres en una lista sin espacios.

#cadena = input("Ingrese caracteres: ")
#lista = []
#for caracter in cadena:
#    if caracter != ' ':
#        lista.append(caracter)
#print("Lista de caracteres ingresados:", lista)

#5) Crea una tupla con números, pide un numero por teclado e indica cuantas veces se
#repite.

#t = (1, 2, 3, 4, 5)
#numero = int(input("ingrese un numero: "))
#repeticiones=0
#for elemento in t:
#    if elemento == t:
#        repeticiones +=1
#if repeticiones>0:
#    print ("el numero", numero, "se repite", repeticiones, "veces")
#else:
#    print ("el numero ingresado no se repite :)")

#6) Crea una tupla con los meses del año, pedir números al usuario. Si el numero esta
#entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino
#muestra un mensaje de error. El programa termina cuando el usuario introduce un
#cero

#t = ("enero", "febrero", "marzo", "abril", "mayo", "junio" ,"julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
#while True:
#    numero = int(input("Ingrese un número: "))
#    if numero == 0:
#        break
#    if numero in range(1, 13):
#        mes = t[numero-1]
#        print("El número", numero, "corresponde al mes de", mes)
#    else:
#        print("Ocurrió un error.")
#print("Programa finalizado.")

#7) Crea una tupla con números e indica el número con mayor valor y el que menor
#tenga.
#t = (5, 1, 2, 3, 4, 6)
#mayor = max(t)
#menor = min(t)
#print("El número con mayor valor es:", mayor)
#print("El número con menor valor es:", menor)

#8) (Opcional)Escribir un programa que vaya solicitando al usuario que ingrese
#nombres. - Si el nombre se encuentra en la agenda (implementada con un
#diccionario), debe mostrar el teléfono y, opcionalmente, permitir modificarlo si no
#es correcto. - Si el nombre no se encuentra, debe permitir ingresar el teléfono
#correspondiente. El usuario puede utilizar la cadena "*", para salir del programa


#9) Opcional: Pide números y mételos en una lista, cuando el usuario meta un 0 ya
#dejaremos de insertar. Por último, muestra los números ordenados de menor a
#mayor.


#10) Opcional: Lo mismo que el anterior, pero ordenando de mayor a menor.


#11) Opcional: Codificador Morse: Desarrolle un programa en Python que permita al
#usuario escribir un mensaje y convertirlo a código Morse. La codificación Morse se
#presenta en la siguiente tabla:
#Muestre el mensaje codificado de manera tal que haya una letra en Morse por línea, y separe
#las palabras con dos líneas en blanco. Por ejemplo, ‘hola mundo’ se mostraría:
#.... --- .-.. .- / -- ..- -. -.. ---
#Ayuda de tiempo:
#Tracutor_Morse = {"a":".-","b": "-...","c":"-.-.","d":"-
#..","e":".","f":"..-.",
#"g":"--.","h":"....","i":"..","j":".---","k":"-.-
#","l":".-..",
#"m":"--","n":"-.","o":"---","p":".--.","q":"--.-
#","r":".-.",
#"s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-
#..-","y":"-.--",
#"z":"--.."}