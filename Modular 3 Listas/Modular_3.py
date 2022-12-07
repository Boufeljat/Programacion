#EJERCICIO 1
"""
Design a function called charactersInString that has a character string and a character
as input parameters and returns how many times that character appears in the string. It
should do it no matter if the string and character are lower case or upper case characters.
"""
def charactersInString (cadena, caracter):
    contador = 0
    for i in range(len(cadena)):
        if caracter.upper() == cadena[i].upper:
            contador+=1
    return contador
#EJERCICIO 2
"""
Design a function called lowCaseInString that has a string of characters as parameter,
the method should return how many of those characters are lowercase letters.
"""
def lowCaseInString (cadena):
    contador=0
    for i in range(len(cadena)):
        if cadena[i].islower():
            contador+=1
    return contador
#EJERCICIO 3
"""
Design a function called upperCaseInString that has a string of characters as parameter
and the method should return how many are uppercase letters.
"""
def lowCaseInString (cadena):
    contador=0
    for i in range(len(cadena)):
        if cadena[i].isupper():
            contador+=1
    return contador
#EJERCICIO 4
"""
Design a function called numberInString that receives a string of characters as
parameter and returns how many of them are numbers.
"""
def numberInString(cadena):
    contador=0
    for i in range(len(cadena)):
        if cadena[i].isdigit():
            contador+=1
    return contador
#EJERCICIO 5
"""
Design a function called palindrome that has a string of characters as input parameter,
and returns True if it is a palindrome or False in other cases. A word is a palindrome if it
can be read the same from left to right or right to left, ignoring whites. For example:
"anilina" or "Dabale arroz a la zorra el abad" To simplify the problem, you can assume
that simple characters are used, that is, without tildes or diresis.
"""
def palindrome(frase):
    frase = frase.lower() # dabale arroz a la zorra el abad
    frase = frase.replace(" ", "") # dabalearrozalazorraelabad
    a = 0
    b= len(frase) -1
    for i in range(0, len(frase)):
        if frase[a] == frase[b]:
            a+=1
            b-=1
        else:
            return False
    return True
#EJERCICIO 6
"""
Realizar una función que busque una palabra escondida dentro de un texto. Por ejemplo,
si la cadena es “shybaoxlna” y la palabra que queremos buscar es “hola”, entonces si se
encontrará y deberá devolver True, en caso contrario deberá devolver False. Las letras
de la palabra escondida deben aparecer en el orden correcto en la cadena que la oculta:
shybaoxlna ⇒ hola: True
soybahxlna ⇒ hola: False
"""
def contiene_palabra_escondida(frase, palabra_escondida):
    posicion= 0
    for letra in frase:
        if posicion<len(palabra_escondida) and palabra_escondida[posicion]==letra:
            posicion+=1
    return posicion==len(palabra_escondida)
#EJERCICIO 7
"""
Diseñar una función que reciba como parámetro tres cadenas, la primera será una frase
y deberá buscar si existe la palabra que recibe como segundo parámetro y reemplazarla
por la tercera.
"""
def sustituir(frase, palabra_buscar, palabra_sustituta):
    ind_pal_buscar = 0
    resultado, tmp = "", ""

    for i in range(len(frase)):
        if frase[i] == palabra_buscar[ind_pal_buscar]:
            if ind_pal_buscar == len(palabra_buscar) - 1:
                tmp = ""
                resultado += palabra_sustituta
                ind_pal_buscar = 0
            else:
                tmp += frase[i]
                ind_pal_buscar += 1
        else:
            resultado += tmp + frase[i]
            ind_pal_buscar = 0
            tmp = ""

    return resultado
#EJERCICIO 8
"""
Diseñar una función que determine la cantidad de vocales diferentes, que tiene una
palabra o frase introducida por teclado. Por ejemplo, la cadena “Abaco”, devolvería 2.
"""
def contar_vocales(cadena):
    contador=0
    for letra in cadena:
        if letra in "aeiou":
            contador+=1
    return contador
#EJERCICIO 9
"""
Crear una función que, tomando una cadena de texto como entrada, construya y
devuelva otra cadena formada de la siguiente manera: todas las consonantes estarán al
principio y todas las vocales al final de la misma, eliminando los blancos. Por ejemplo,
pasándole la cadena "curso de programacion", una posible solución sería
"crsdprgrmcnuoeoaaio".
"""
def constituir(frase):
    frase= frase.lower() #Convertir las palabras mayúsculas a minúsculas
    frase= frase.replace(" ", "") #cursodeprogramacion
    Test= False
    for letra in frase:
         if letra in "eaiou":
            Test= True
        else:
            Test= False
    return frase

#EJERCICIO 10
"""
Escribir una función que devuelva el número de palabras que hay en una cadena que
recibe como parámetro. Ten en cuenta que entre dos palabras puede haber más de un
blanco. También al principio y al final de la frase puede haber blancos redundantes. Por
ejemplo, si la cadena es “He estudiado mucho”, debe devolver 3.
"""