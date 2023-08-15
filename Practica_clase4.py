"""▪ 1. Escriba una función que muestre todos los números primos entre 1 y un número n que
es ingresado por parámetro."""

"""def esprimo(numero):
    for k in range (2,numero-1):
        if numero%k==0:
            return False
    return True

def modulo(n):
    for i in range(1,n):
        if esprimo(i):
            print (i, end=" ")

modulo(15)"""

""" 2. Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si
la dirección es válida o no, valiéndose de una función para decidirlo. Una dirección se
considerará válida si contiene el símbolo "@".
▪ (find) →"""
 
"""def pedirmail():
    email= input("ingrese su mail: ")
    if email.find("@")!=-1:
      print ("mail valido")
    else: 
      print ("error")

pedirmail()"""


#3. Definir una función que muestre el factorial de un número

"""numero=int(input("ingrese un nuemero: "))
def factorial():
    while numero:
        resultado= numero* numero<numero
    print(resultado)"""

def factorial(numero):
    factorial=numero
    for i in range(1,numero):
        factorial = factorial*i
    print (f"el factorial de {numero} es {factorial}")
    
factorial()









