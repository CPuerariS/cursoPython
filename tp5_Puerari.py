"""1. Escriba una función redondear() que permita redondear un número
decimal de acuerdo al criterio: Si el número es mayor a 3.50, devolver el
entero siguiente (en este caso, 4), si no devolver el entero inmediatamente
anterior (3)

def redondear(numero):
    if numero > 3.50:
        return int(numero) + 1
    else:
        return int(numero)
    
resultado= redondear(3.50)
print ("el entero es ", resultado,)"""


"""2. Coloque el módulo del ejercicio anterior dentro de un paquete. En un
módulo que esté fuera de ese paquete, cree una función de suma de
decimales que redondee el resultado haciendo uso de la función
redondear() del paquete recién creado."""




"""3. Usando el módulo datetime, escribe un programa que muestre la fecha
y hora actuales del sistema."""

"""4. Escriba un programa que devuelva un número par al azar entre 2 y 10
(pista: para comprobar si se pueden generar todos los números, pruebe
ejecutar el programa dentro de un ciclo infinito)."""

"""5. Bola mágica: La bola mágica (Magic 8 ball) es un popular juguete usado
para la adivinación o para buscar consejo. Su mecanismo es muy simple:
ante una pregunta del usuario, la bola responde con una de 8 posibles
respuestas:
- Es seguro que sí
- Las chances son buenas
- Puedes contar con ello
- Pregúntame de nuevo más tarde
- Concéntrate y pregunta de nuevo
- No veo con claridad, intenta de nuevo
- Mi respuesta es no
- Mis fuentes me dicen que no
Escriba una función en Python para simular la bola mágica.

6. Encuentre el tiempo de ejecución de los programas de los ejercicios
anteriores (pista: use el módulo time)
7. (Opcional) Sorteo: Escriba un programa que simule un sorteo donde
toman uno o más papeles al azar de un pozo para elegir los ganadores.
8. (Opcional) Escriba una función que pida al usuario ingresar su fecha de
nacimiento y sea capaz de devolver la cantidad de días desde su
nacimiento hasta hoy.
9. (Opcional) Implemente el programa del ejercicio 6 usando un diccionario."""