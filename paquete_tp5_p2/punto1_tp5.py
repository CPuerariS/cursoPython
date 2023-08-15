def redondear(numero):
    if numero > 3.50:
        return int(numero) + 1
    else:
        return int(numero)
    
resultado= redondear(3.50)
print ("el entero es ", resultado,)

