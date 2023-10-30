"""
    1. Diseña un programa para mostrar todos los números entre 1 y 100. Si el número es un múltiplo de 7, debes mostrar el mensaje "El número xx es un múltiplo de 7". 
    Si el número es un múltiplo de 13, debes mostrar el mensaje "El número xx es un múltiplo de 13". Si el número es un múltiplo de 7 y 13, debes mostrar ambos mensajes.
"""
"""
for numero in range(1, 101):
    if (numero % 7 == 0 and numero % 13 == 0):
        print("El número", numero, "es múltiplo de 7 y 13")
    elif (numero % 7 == 0):
        print("El número", numero, "es múltiplo de 7")
    elif (numero % 13 == 0):
        print("El número", numero, "es múltiplo de 13")
"""   
"""
    2. Diseña un programa para leer un número entero entre 0 y 10 y mostrar la tabla de multiplicar. Para solicitar el número, debes mostrar el siguiente mensaje: 
        "Ingresa un número entre 0 y 10". Si el número está fuera de los límites, el programa debe mostrar el mensaje "El número está fuera de los límites". 
        Si el número es válido, deberá mostrar la tabla de multiplicar siguiendo el siguiente formato:
        7*0=0
        7*1=7
        ...
        7*10=70
"""
"""
numero = int(input("Ingresa un número entre 0 y 10: "))
if numero < 0 or numero > 10:
    print("El número está fuera de los límites")
else:
    for i in range(0, 11):
        print(numero, "*", i, "=", numero*i)
"""
"""
    3. Diseña un programa que pregunte cuántos números desea introducir el usuario. Luego, el usuario deberá introducir los números uno por uno, 
    y el programa deberá indicar si cada uno de los números es impar o par. 
    Si el usuario introduce 0 o un número negativo, no es válido y el sistema deberá solicitar otro número. Los mensajes son los siguientes:

        "¿Cuántos números deseas ingresar?" para preguntar por la cantidad de números.
        "Ingresa un número mayor que 0:" para solicitar un número.
        "El número no es válido, debe ser mayor que 0" para informar que el número no es válido.
        "El número XX es impar."
        "El número XX es par."
"""
"""
numeros = int(input("¿Cuántos números deseas ingresar?: "))
for i in range(numeros):
    numero = int(input("Ingresa un número mayor que 0: "))
    while (numero <= 0):
        numero = int(input("El número no es válido, debe ser mayor que 0: "))
    if (numero %2 == 0):
        print("El número", numero, "es par")
    else:
        print("El número", numero, "es impar")
"""
"""
    4. Diseña un programa que lea un número positivo N mayor que 0 y muestre el resultado de la suma de los N números entre 1 y N. 
    Si el número N no es válido, el programa debe solicitarlo nuevamente. Los mensajes son los siguientes:
        "Ingresa un número mayor que 0:"
        "El número no es válido, inténtalo de nuevo."
        "La suma de los primeros N números es XX.
"""
"""
numero = int(input("Ingrese un número mayor que 0: "))
suma = 0
resulatado = 0
while (numero <= 0):
    numero = int(input("El número no es válido, inténtalo de nuevo: "))
for numero in range(1, numero+1):
    suma+=1
    resulatado += suma
print("La suma de los primeros", suma, "números es", resulatado)
"""

"""
    Diseña un programa que solicite números hasta que el usuario introduzca un número negativo. 
    Cuando esto suceda, el programa mostrará cuántos números positivos ha introducido el usuario. 
    Los mensajes son los siguientes:
    "Ingresa un número (negativo para finalizar):"
    "Has ingresado XX números positivos."
"""
numero = int(input("Ingrese un número (negativio para finalizar): "))
contador = 0
while numero > 0:
    numero = int(input("Ingrese un número (negativio para finalizar): "))
    contador+=1 
print("Has ingresado", contador, "números positivos")



