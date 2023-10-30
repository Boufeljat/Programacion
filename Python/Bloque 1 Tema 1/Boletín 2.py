#EJERCICIO 1

sueldo_bruto = int(input("Introduzca el sueldo bruto: "))
sueldo_neto = int(input("Introduzca el sueldo neto: "))
print(sueldo_bruto * 0.22 == sueldo_neto)

dia = int(input("Introduzca un día: "))
print(dia >= 1 and dia <= 31)

num1 = int(input("Introduzca el número 1: "))
num2 = int(input("Introduzca el número 2: "))
print(num1 %3 == 0 and num2 %3 == 0)

nota = float(input("Introduzca la nota: "))
print(nota >= 5 and nota <= 10)

nota1 = float(input("Introduzca la nota 1: "))
nota2 = float(input("Introduzca la nota 2: "))
nota3 = float(input("Introduzca la nota 3: "))

print((nota1 + nota2 + nota3) /3 >= 5 and (nota1 + nota2 + nota3) /3 <= 10)


#EJERCICIO 2

nota1 = float(input("Introduzca la nota 1: "))
nota2 = float(input("Introduzca la nota 2: "))
nota3 = float(input("Introduzca la nota 3: "))

print((nota1 < 5 or nota2 < 5 and nota3 < 5))

saldo = float(input("Introduzca el salario: "))
descubierto = int(input("Introduzca el numero de veces que has descubierto: "))
print(not(saldo < 1000 or descubierto > 5))

asignaturasAprobadas = int(input("Introduzca el número de las asignaturas aprobadas: "))
asignaturasCurso = int(input("Introduzca el número de las asignaturas del curso: "))
print(not(asignaturasAprobadas < asignaturasCurso * 0.33))


mes = int(input("Introduzca el mes: "))
dia = int(input("Introduzca el dia: "))
print((mes == 1 and (dia >= 1 and dia <= 31)) or (mes == 2 and (dia >= 2 and dia <= 28)) or (mes == 3 and (dia >= 1 and dia <= 31)) or (mes == 4 and (dia >= 1 and dia <= 30)) 
        or (mes == 5 and (dia >= 1 and dia <= 31)) or (mes == 6 and (dia >= 1 and dia <= 30)) or (mes == 7 and (dia >= 1 and dia <= 31)) or (mes == 8 and (dia >= 1 and dia <= 31)) 
        or (mes == 9 and (dia >= 1 and dia <= 30)) or (mes == 10 and (dia >= 1 and dia <= 31)) or (mes == 11 and (dia >= 1 and dia <= 30)) or (mes == 12 and (dia >= 1 and dia <= 31)))

#EJERCICIO 3

"Llueve = T"
"haceSol = F"
"haceFrio = F"

resultado = (llueve and not haceSol and not haceFrio) or (not llueve and haceSol and not haceFrio) or (not llueve and not haceSol and haceFrio)


#EJERCICIO 4
"""1. No me gusta programar y voy a dedicar al menos diez horas a la semana a programar."""
"""2. No me gusta programar o voy a dedicar al menos diez horas a la semana a programar."""
"""3. No no me gusta programar."""
"""4. No me gusta programar o no voy a dedicar al menos diez horas a la semana a programar."""
"""5. Ni me gusta programar ni voy a dedicar al menos diez horas a la semana a programar."""
"""6. No me gusta programar y no voy a dedicar al menos diez horas a la semana a programar."""

