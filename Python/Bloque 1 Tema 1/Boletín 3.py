"""
    1. Realizar un programa que lea un número entero por teclado e informe de si
        el número es par o impar (el cero se considera par).
"""

numero = int(input("Introduzca un número: "))
if numero % 2 == 0:
    print("El número introducido es par")
else:
    print("El número introducido es impar")

"""
    2. Realizar un programa que solicite dos números por teclado e imprima en
        pantalla si son iguales, el primero mayor que el segundo o el primero más
        pequeño que el segundo
"""

numero1 = int(input("Introduzca el número 1: "))
numero2 = int(input("Introduzca el número 2: "))

if (numero1 == numero2):
    print("Los números introducidos son iguales")
elif (numero1 > numero2):
    print("El primero mayor que el segundo")
else:
    print("El primero más pequeño que el segundo")

"""
    3. Realizar un programa que lea un número por teclado. El programa debe
        imprimir en pantalla un mensaje con “El número xx es múltiplo de 2” o un
        mensaje con “El número xx es múltiplo de 3”. Si es múltiplo de 2 y de 3
        deben aparecer los dos mensajes. Si no es múltiplo de ninguno de los dos
        el programa finaliza sin mostrar ningún mensaje
"""

numero = int(input("Introduzca un número: "))
if numero % 2 == 0 and numero % 3 == 0:
    print("El número ", numero, "es múltiplo de 2")
    print("El número ", numero, "es múltiplo de 3")
elif numero % 2 == 0:
    print("El número", numero, "es múltiplo de 2")
elif numero % 3 == 0: 
    print("El número ", numero, "es múltiplo de 3")

"""
    4. Realizar un programa que lea la edad de una persona menor a 100 años e
        informe de si es un niño (0-12 años), un adolescente (13-17), un joven (18-
        29) o un adulto.
"""

edad = int(input("Introduzca su edad: "))
if (edad > 100 or edad < 0):
    print("La edad introducida es incorrecta")
elif (edad > 0 and edad <= 12):
    print("Eres un niño")
elif (edad >= 13 and edad <= 17):
    print("Eres un adolescente")
elif (edad >= 18 and edad <= 29):
    print("Eres un adulto")

"""
    5. Realizar un programa que solicite 4 números e imprima la media de los
        números. También debe imprimir aquellos números que son superiores a la
        media.
"""

numero1 = int(input("Introduzca el número 1: "))
numero2 = int(input("Introduzca el número 2: "))
numero3 = int(input("Introduzca el número 3: "))
numero4 = int(input("Introduzca el número 4: "))

media = (numero1 + numero2 + numero3 + numero4) / 4

print("La media de los números introducidos es:", media)
if (numero1 > media):
    print("El número 1 es mayor que la media")
elif (numero2 > media):
    print("El número 2 es mayor que la media")
elif (numero3 > media):
    print("El número 3 es mayor que la media")
elif (numero4 > media):
    print("El número 4 es mayor que la media")

"""
    6. Realizar un programa que solicite un carácter por teclado e informe por
        pantalla si el carácter es una vocal o no lo es. Si es una vocal mostrará el
        mensaje “Es la primera vocal (A)” o “Es la segunda vocal (E)”, etc.
"""

caracter = input("Introduzca un carácter: ")
if (caracter == "A"):
    print("Es la primera vocal(A)")
elif (caracter == "E"):
    print("Es la segunda vocal(E)")
elif (caracter == "I"):
    print("Es la tercera vocal(I)")
elif (caracter == "O"):
    print("Es la cuarta vocal(O)")
elif (caracter == "U"):
    print("Es la quinta vocal(U)")
else:
    print("El carácter introducido no es una vocal")

"""
    7. Realizar un programa que lea el estado civil de una persona (S-Soltero, C- Casado, V-Viudo y D-Divorciado) y su edad. Después debe mostrar por
        pantalla el porcentaje de retención que debe aplicársele de acuerdo con las
        siguientes reglas:
             A los solteros o divorciados menores de 35 años, un 12%
             Todas las personas mayores de 50 años, un 8.5%
             A los viudos o casados menores de 35 años, un 11.3%
             Al resto de casos se le aplica un 10.5%
"""

estadoCivil = input("Introduzca su estado civil (Soltero, Casado, Viudo, Divorciado): ")
edad = int(input("Introduzca su edad: "))

if (estadoCivil == "Soltero" or estadoCivil == "Divorciado") and edad < 35:
    print("Porcentaje de retención es 12%")
elif (estadoCivil == "Viudo" or estadoCivil == "Casado") and edad < 35:
    print("Porcentaje de retención es 10.5%")
elif edad >= 50:
    print("Porcentaje de retención es 8.5%")
else:
    print("Porcentaje de retención es 10.5%")

"""
    8. Realizar un programa que lea por teclado dos marcaciones de un reloj
        digital (horas, minutos, segundos) comprendidas entre las 0:0:0 y las
        23:59:59 e informe cual de ellas es mayor.
        Ejemplo:
            Hora 1: 12:35:37
            Hora 2: 12:38:36
            “Hora 2 es mayor”
"""

hora1 = int(input("Introduzca la hora 1: "))
minuto1 = int(input("Introduzca los minutos 1: "))
segundo1 = int(input("Introduzca los segundos 1: "))

hora2 = int(input("Introduzca la hora 2: "))
minuto2 = int(input("Introduzca los minutos 2: "))
segundo2 = int(input("Introduzca los segundos 2: "))

if (hora1 >= 0 and hora1 <= 23 and minuto1 >= 0 and minuto1 <= 59 and segundo1 >= 0 and segundo1 <= 59
    and hora2 >= 0 and hora2 <= 23 and minuto2 >= 0 and minuto2 <= 59 and segundo2 >= 0 and segundo2 <= 59):
    if hora1 > hora2:
        print("Hora 1 es Mayor")
    elif hora1 < hora2:
        print("Hora 2 es mayor")
    elif hora1 == hora2:
        if(minuto1 > minuto2):
            print("Hora 1 es mayor")
        elif (minuto1 < minuto2):
            print("Hora 2 es mayor")
        elif (minuto1 == minuto2):
            if (segundo1 > segundo2):
                print("Hora 1 es mayor")
            elif (segundo1 < segundo2):
                print("Hora 2 es mayor")
            else:
                print("Hora 1 y Hora 2 son iguales")
else:
    print("Los datos Introducidos son incorrectos")

"""
    9. En un establecimiento en rebajas, hay 3 tipos de productos (A, B y C). El
    porcentaje de rebaja que se aplicará sobre el precio original del producto se
    calcula de la siguiente forma:
         Si el producto es de tipo A, independientemente de su precio se
            aplica un 7% de descuento.
         Si el producto es de tipo C o bien el precio es inferior a 500€ se
            aplicará un porcentaje del 12% de descuento.
         En el resto de casos se aplica un 9% de descuento.
    Realizar un programa que solicite los datos necesarios (tipo de producto y
        precio original) y calcule el precio rebajado. Debe comprobarse que los
        datos de entrada son correctos, y si no lo son mostrar un mensaje de error.
"""

tipoProducto = input("Introduzca el tipo de producto (A, B, C): ")
precioOriginal = float(input("Introduzca el precio original: "))

if tipoProducto != "A" and tipoProducto != "B" and tipoProducto != "C":
    print("Los datos introducidos son incorrectos")
else:
    if tipoProducto == "A":
        precioRebajado = precioOriginal - (precioOriginal * 0.07)
        print("El precio rebajado es:", precioRebajado)
    elif tipoProducto == "C" or precioOriginal < 500:
        precioRebajado = precioOriginal - (precioOriginal * 0.12)
        print("El precio rebajado es:", precioRebajado)
    else:
        precioRebajado = precioOriginal - (precioOriginal * 0.09)
        print("El precio rebajado es:", precioRebajado)

"""
    10. Realizar un programa que lea un carácter y dos números enteros por
        teclado. Si el carácter leído es un operador aritmético, calcular la operación
        correspondiente, si es cualquier otro debe mostrar un error
"""
caracter = input("Introduzca un caracter: ")
numero1 = int(input("Introduzca el número 1: "))
numero2 = int(input("Introduzca el número 2: "))

if (caracter == "-"):
    print("El resultado del numero 1 menos el numero 2", numero1 - numero2)
    print("El resultado del numero 2 menos el numero 1", numero2 - numero1)
elif (caracter == "+"):
    print(numero1 + numero2)
elif (caracter == "*"):
    print(numero1 * numero2)
elif (caracter == "/"):
    print(numero1 / numero2)
elif (caracter == "//"):
    print(numero1 // numero2)
elif (caracter == "%"):
    print(numero1 % numero2)
else:
    print("Error")