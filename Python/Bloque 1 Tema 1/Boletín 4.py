import math
"""
    1. Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
"""
"""
    2. Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.
"""
"""
GradoFahrenheit = int(input("Introduzca un número en grado Fahrenheit: "))
GradoCelsius = ((GradoFahrenheit - 32) *5/9)
print("El valor introducido en grado Celsius es: ", GradoCelsius, "ºC")
"""
"""
cateto1 = int(input("Introduzca el cateto 1: "))
cateto2 = int(input("Introduzca el cateto 2: "))

hipotenusa = math.sqrt(cateto1**2 + cateto2**2)

print("La hipotenusa es: ", hipotenusa)
"""

"""
    3. Calcular la media de tres números pedidos por teclado
"""
"""
numero1 = int(input("Introduzca el número 1: "))
numero2 = int(input("Introduzca el número 2: "))
numero3 = int(input("Introduzca el número 3: "))

media = (numero1 + numero2 + numero3) / 3

print("La media de los números introducidos es: ", media)
"""
"""
    4. Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber 
        cuanto deberá pagar finalmente por su compra.
"""
"""
totalCompra = float(input("Introduzca el total de la compra: "))
totalDescontado = (totalCompra - (totalCompra * 0.15))
print("Finalmente el cliente tiene que pagar: ", totalDescontado)
"""
"""
    5. Pide al usuario dos números y muestra la "distancia" entre ellos (el valor absoluto de su 
        diferencia, de modo que el resultado sea siempre positivo).
"""
"""
numero1 = int(input("Introduzca el número 1: "))
numero2 = int(input("Introduzca el número 2: "))

if numero1 > numero2:
    print("La distancia de los números introducidos es: " , numero1 - numero2)
elif numero2 > numero1:
    print("La distancia de los números introducidos es: ", numero2 - numero1)
elif numero1 == numero2:
    print("La distancia de los números introducidos es: ", numero1 - numero2)
"""
"""
    6. Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano. 
        Calcula y muestra la distancia entre ellos.
"""
"""
x1 = int(input("Introduzca un valor de x1: "))
x2 = int(input("Introduzca un valor de x2: "))
y1 = int(input("Introduzca un valor de y1: "))
y2 = int(input("Introduzca un valor de y2: "))

distancia = math.sqrt(((x2 - x1)**2) + ((y2 - x1)**2))
print("La distancia es: ", distancia)
"""
"""
    7. Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica. 
        Python no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿cómo se 
        puede calcular?
"""
"""
numero = float(input("Introduzca un número: "))
RaizCuadrada = math.sqrt(numero)
RaizCubica = (numero ** (1/3))
print("La raíz cuadrada del número:", numero, "es:", RaizCuadrada)
print("La raíz cúbica del número:", numero, "es:", RaizCubica)
"""
"""
    8. Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de 
        pedirnos cuantas monedas tenemos de 2e, 1e, 50 céntimos, 20 céntimos o 10 céntimos).
"""
"""
Moneda2E = int(input("Cúantas monedas tienes de 2€: "))
Moneda1E = int(input("Cúantas monedas tienes de 1€: "))
Moneda50C = int(input("Cúantas monedas tienes de 50 céntimos: "))
Moneda20C = int(input("Cúantas monedas tienes de 20 céntimos: "))
Moneda10C = int(input("Cúantas monedas tienes de 10 céntimos: "))

totalMoneda2E = (Moneda2E * 2)
totalMoneda1E = (Moneda1E * 1)
totalMoneda50C = (Moneda50C * 0.50)
totalMoneda20C = (Moneda50C * 0.20)
totalMoneda10C = (Moneda50C * 0.10)

total = (totalMoneda2E + totalMoneda1E + totalMoneda50C + totalMoneda20C + totalMoneda10C)
print("El dinero que tienes es:", total)
"""
"""
    9. Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el 
        exponente. Pueden ocurrir tres cosas:
            ◦ El exponente sea positivo, sólo tienes que imprimir la potencia.
            ◦ El exponente sea 0, el resultado es 1.
            ◦ El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.
"""
"""
base = int(input("Introduzca la base: "))
exponente = int(input("Introduzca el exponente: "))
potencia = (base)**exponente
if (exponente > 0):
    print("La potencia es:", potencia)
elif (exponente == 0):
    print("La potencia es:", potencia)
else:
    exponente_positivo = abs(exponente)
    print("La potencia es:", 1/(base ** exponente_positivo))
"""
"""
    10. Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los 
    lados de un triángulo. El programa debe determinar que tipo de triangulo es, teniendo en 
    cuenta los siguiente:
        ◦ Si se cumple Pitágoras entonces es triángulo rectángulo
        ◦ Si sólo dos lados del triángulo son iguales entonces es isósceles.
        ◦ Si los 3 lados son iguales entonces es equilátero.
        ◦ Si no se cumple ninguna de las condiciones anteriores, es escaleno.
"""
"""
A = int(input("Introduzca el primer lado A: "))
B = int(input("Introduzca el primer lado B: "))
C = int(input("Introduzca el primer lado C: "))

if (A**2 + B**2 == C**2 or A**2 + C**2 == B**2 or C**2 + B**2 == A**2):
    print("Es un tríangulo rectángulo")
else:
    if (A == B == C):
        print("Es equilátero")
    elif (A == B or C == A or C == B):
        print("Es isósceles")
    else:
        print("Escaleno")
"""
"""
    11. Escribir un programa que lea un año indicar si es bisiesto. Nota: un año es bisiesto si es un 
        número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible 
        por 400.
"""
"""
anyo = int(input("Introduzca un año: "))
if (anyo % 4 == 0):
    if(anyo % 100 == 0):
        if(anyo % 400 == 0):
            print("Es un año bisiesto")
        else:
            print("No es un año bisiesto")
    else:
        print("Es un año bisiesto")
else:
    print("No es un año bisiesto")
"""
"""
    12. La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, la cual
        se clasifica en tipos A y B, y además en tamaños 1 y 2. Cuando se realiza la venta del 
        producto, ésta es de un solo tipo y tamaño, se requiere determinar cuánto recibirá un 
        productor por la uva que entrega en un embarque, considerando lo siguiente: si es de tipo A, 
        se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de 
        tamaño 2. Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos 
        cuando es de tamaño 2. Realice un algoritmo para determinar la ganancia obtenida.
"""
tipo_uva = input("Ingrese el tipo de uva (A o B): ")
tamaño_uva = int(input("Ingrese el tamaño de uva (1 o 2): "))

peso_uva = float(input("Ingrese el peso de la uva en kilogramos: "))

precio_inicial = 0 
if tipo_uva == "A":
    if tamaño_uva == 1:
        precio_inicial = 1.0  
    elif tamaño_uva == 2:
        precio_inicial = 1.1 
elif tipo_uva == "B":
    if tamaño_uva == 1:
        precio_inicial = 0.7 
    elif tamaño_uva == 2:
        precio_inicial = 0.6 

ganancia = precio_inicial * peso_uva

print("La ganancia obtenida por el productor es de", ganancia, "euros.")


"""
    13. El director de una escuela está organizando un viaje de estudios, y requiere determinar 
        cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el 
        servicio. La forma de cobrar es la siguiente: si son 100 alumnos o más, el costo por cada 
        alumno es de 65 euros; de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, 
        y si son menos de 30, el costo de la renta del autobús es de 4000 euros, sin importar el 
        número de alumnos. Realice un algoritmo que permita determinar el pago a la compañía de 
        autobuses y lo que debe pagar cada alumno por el viaje.
"""
numero_alumnos = int(input("Ingrese el número de alumnos: "))

costo_por_alumno = 0
costo_total_viaje = 0

if numero_alumnos >= 100:
    costo_por_alumno = 65
    costo_total_viaje = numero_alumnos * costo_por_alumno
elif 50 <= numero_alumnos <= 99:
    costo_por_alumno = 70
    costo_total_viaje = numero_alumnos * costo_por_alumno
elif 30 <= numero_alumnos <= 49:
    costo_por_alumno = 95
    costo_total_viaje = numero_alumnos * costo_por_alumno
else:
    costo_total_viaje = 4000

costo_por_alumno = costo_total_viaje / numero_alumnos

print("El costo por alumno es de", costo_por_alumno, "euros.")
print("El costo total del viaje para la compañía de autobuses es de", costo_total_viaje, "euros.")


"""
    14. La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro 
        es por el tiempo que ésta dura, de tal forma que los primeros cinco minutos cuestan 1 euro, 
        los siguientes tres, 80 céntimos, los siguientes dos minutos, 70 céntimos, y a partir del 
        décimo minuto, 50 céntimos. Además, se carga un impuesto de 3 % cuando es domingo, y si
        es otro día, en turno de mañana, 15 %, y en turno de tarde, 10 %. Realice un algoritmo para 
        determinar cuánto debe pagar por cada concepto una persona que realiza una llamada.
"""
duracion_llamada = float(input("Ingrese la duración de la llamada en minutos: "))
dia_semana = input("Ingrese el día de la semana (Domingo u otro): ")
turno = input("Ingrese el turno de la llamada (Mañana o Tarde): ")

costo_llamada = 0
impuesto = 0
costo_total = 0

if duracion_llamada <= 5:
    costo_llamada = 1.00
elif 6 <= duracion_llamada <= 8:
    costo_llamada = 1.00 + 0.80 * (duracion_llamada - 5)
elif 9 <= duracion_llamada <= 10:
    costo_llamada = 1.00 + 0.80 * 3 + 0.70 * (duracion_llamada - 8)
else:
    costo_llamada = 1.00 + 0.80 * 3 + 0.70 * 2 + 0.50 * (duracion_llamada - 10)

if dia_semana == "Domingo":
    impuesto = 0.03 * costo_llamada
else:
    if turno == "Mañana":
        impuesto = 0.15 * costo_llamada
    else:
        impuesto = 0.10 * costo_llamada

costo_total = costo_llamada + impuesto

print("El costo de la llamada es de", costo_llamada, "euros.")
print("El impuesto es de", impuesto, "euros.")
print("El costo total es de", costo_total, "euros.")

"""
    15. Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día 
        correspondiente. Si introducimos otro número nos da un error.
"""
"""
dia = int(input("Introduzca un número del día(1/7): "))
if (dia >= 1 and dia <= 7):
    if (dia == 1):
        print("Lunes")
    elif (dia == 2):
        print("Martes")
    elif (dia == 3):
        print("Miercoles")
    elif (dia == 4):
        print("Jueves")
    elif (dia == 5):
        print("Viernes")
    elif (dia == 6):
        print("Sábado")
    elif (dia == 7):
        print("Domingo")
else:
    print("El día introducida no es válida")
"""
"""
    16. Escribe un programa que pida un número entero entre uno y doce e imprima el número de 
        días que tiene el mes correspondiente.
"""
"""
numero = int(input("Introduzca un número entre 1 y 12: "))
if (numero >= 1 and numero<= 12):
    if(numero == 1 or numero == 3 or numero == 5 or numero == 7 or numero == 8 or numero == 10 or numero == 12):
        print("31 Días")
    elif (numero == 2):
        print("29 Si es un año bisiesto")
        print("28 Si no es un año bisiesto")
    else:
        print("30 Días")
else:
    print("El número introducido no válido")
"""
