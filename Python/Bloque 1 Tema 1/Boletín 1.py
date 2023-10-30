# EJERCICIO 1
a = 7 >=27 and not (7 <= 2) # False
print(a) 

b = 24 > 5 and 10 <= 10 or 10 == 5  # True
print(b)

c = (10>=15 or 23==13) and not(8==8) # False
print(c)

d = not (6/3>3) or 7>7 # True
print(d)

# EJERCICIO 2
a = 27%4 + 15/4 # 6.75
print(a)

b = 37/4**2-2 # 0.3125
print(b)

c = 9*2/3*10*3 # 180.0
print(c)

d= (7*3-4*4)**2/4*2 #12.5
print(d)


#EJERCICIO 3

precio = float(input("Introduzca un precio: "))
print(precio >= 60 and precio <= 420)

numero = int(input("Introduzca un número: "))
print(numero % 2 != 0)

saldo = int(input("Introduzca el saldo: "))
dineroSacar = int(input("Introduzca el importe que quieres sacar: "))
print((saldo >= dineroSacar) and saldo >= 0)

hora = int(input("Introduzca la hora: "))
minutos = int(input("Introduzca los minutos: "))
print((minutos >= 0 and minutos <= 59) and (hora >= 0 and hora <= 23))

estadoCivil = input("Introduzca su estado civil (Soltero, Casado, Viudo, Divorciado): ")
print(estadoCivil != "Soltero" and estadoCivil != "Casado" and estadoCivil != "Viudo" and estadoCivil != "Divorciado"
        and estadoCivil != "S" and estadoCivil != "C" and estadoCivil != "V" and estadoCivil != "D")

#EJERCICIO 4

cantidad = float(input("Introduzca la cantidad: "))
print(not(cantidad > 300 or cantidad < 0))

edad = int(input("Introduzca la edad: "))
print(not(edad >= 16 and edad <= 22))

respuesta = input("Introduzca una respuesta (S/N): ")
print(not (respuesta == "S" or respuesta == "N" or respuesta == "s" or respuesta == "n"))


numero = int(input("Introduzca un número: "))
print(numero %7 != 0 and numero %3 != 0)