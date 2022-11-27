#Ejercicio 1
"""
Design a method called computeFactorial that receives a positive integer and
returns the factorial for that number. If the number is negative the method should
return None.
"""
def factorial(n): 
    resultado = 1   
    for i in range(2, n+1):
        resultado *= i
    return resultado
numero = int(input("Ingrese un número: "))
print(f"Factorial of {numero} is {factorial(numero)}")
"""
#Ejercicio 2
"""
Design a method called isLeapYear that receives a number and returns False for
common years and True for leap years. You may know that a year is considered to
be a leap year if it is divisible by 4, unless it is also divisible by 100. A year is not a
leap year if it is divisible by 100 unless it is also divisible by 400.
"""
def is_leap(year):
    leap = False
    if year%4==0 and (year%100==0) and year%400==0:
        leap=True
    elif not(year%4==0) and not(year%100==0) and not(year%400==0):
        leap=False
    else:
        leap=False
        
    return leap

year = int(input())

#Ejercicio 3
"""
Design a method called computeDaysInMonth that returns the number of days for
the month and year that are received as arguments. You may use the method
leapYear above. If the values are not valid the method should return -1.
"""
mes=11
año=2022
def ComputeDaysInMonth (mes, año):
    diasTotales=0
    meses=[31,28,31,30,31,30,31,31,30,31,30,31]
    if mes>12 or mes<1 or año<1:
        diasTotales=-1
    else:
        if isLeapYear(number)==False and mes==2:
            diasTotales=29
        else:
            diasTotales=meses[mes-1]
    return diasTotales
print(ComputeDaysInMonth(mes, año))
#Ejercicio 4
"""
Design a method called getDayOfWeek that receives a list containing three integers
(day, month and year) and returns the day of the week for that date (Monday,
Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday).
You can use the following algorithm to get a number between 0 (Sunday) and 6
(Saturday) corresponding to the day in the week for a given date:
a = (14 - month) / 12
y = year – a
m = month + 12 * a – 2
d = (day + y + y/4 - y/100 + y/400 + (31*m)/12) mod 7
"""
def dayofweek(d, m, y):
    t = [ 0, 3, 2, 5, 0, 3,
          5, 1, 4, 6, 2, 4 ]
    y -= m < 3
    return (( y + int(y / 4) - int(y / 100)
             + int(y / 400) + t[m - 1] + d) % 7)
 
# Driver Code
day = dayofweek(30, 8, 2010)
print(day)
#Ejercicio 5
"""
Design a method called powerIt that receives two integers and raises the first
number to the second. You may use the product or recursion and check the values. If
no exponent is provided the first number is raised to 0.
"""
def power(x, y):
    temp = 0
    if(y == 0):
        return 1
    temp = power(x, int(y / 2))
    if (y % 2 == 0)
    return temp * temp
    else
    return x * temp * temp
#Ejercicio 6
"""
Design a method called getNumberOfDigits that receives one number (it can be
real, integer, positive or negative) and should return the number of digits it contains. If
the parameter is not valid the method should return None. Extend this function to
other numeric systems (hexadecimal, decimal, binary, octal).
"""
num = int(input("Please type in a number:"))
n=0
while num>n:
    a = num%10
    num -= a
    num = num/10
    print(a)
    n = n + 1   
print(n)
#Ejercicio 7
"""
 Design a method called isPrime that receives one integer positive number greater
than 0 as parameter. The method should return True if the number is prime or False if
not prime. If the parameter is not valid the method should return None.
"""
num = 11
# If given number is greater than 1
if num > 1:
    # Iterate from 2 to n / 2
    for i in range(2, int(num/2)+1):
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
#Ejercicio 8
"""
 Design a method called solveSecondOrderEquation that receives three integer
positive numbers corresponding to the coefficients of a second order equation
(ax
2+bx+c=0) and computes its possible solutions. If the parameters are not valid the
method should return None.
"""
# import complex math module
import cmath
  
a = 1
b = 4
c = 2
  
# calculating  the discriminant
dis = (b**2) - (4 * a*c)
  
# find two results
ans1 = (-b-cmath.sqrt(dis))/(2 * a)
ans2 = (-b + cmath.sqrt(dis))/(2 * a)
  
# printing the results
print('The roots are')
print(ans1)
print(ans2)
#Ejercicio 9
"""
Design a method called getPrimeDivisors that receives a positive number as a
parameter and returns a list containing its prime divisors. If the parameter is not valid
the method should return None.
"""
def primeFactors(n):
 
    c = 2
    while(n > 1):
 
        if(n % c == 0):
            print(c, end=" ")
            n = n / c
        else:
            c = c + 1
 
# Driver code
n = 315
primeFactors(n)
#Ejercicio 10
"""
Design a method called isFriendNumber that receives two positive numbers and
returns True if the numbers are friends, False otherwise. Two numbers are
considered to be friends if the sum of its divisors, except the given number, is equal
to the second and vice versa.
"""
num1 = int(input())
num2 = int(input())
sum1 = 0
sum2 = 0
for i in range(1,num1):
    if(num1 % i == 0):
        sum1 = sum1 + i
for i in range(1,num2):
    if(num2 % i == 0):
        sum2 = sum2 + i
if(sum1 == num1 and sum2 == num2):
    print(“Friendly Pair”)





