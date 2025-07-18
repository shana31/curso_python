# -*- coding: utf-8 -*-
"""Exercici_estructura_cadena.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FzX__Kb_xAkjrLeXg558ksF62FkUgJaW

- Hacer ejercicios: **1,2,6,12**
- subcadena 1, 2
- hacer :  4,7,8,9,10 11, 14, 15
"""

'''
1-Invertir el valor d'una cadena:
a)Assignar a una variable una cadena de text qualsevol, després crear una altra variable de text
buida on haurem de fer el procés per passar els valors de e l'anterior cadena però invertida.
b) Mostrar els caràcters d'una cadena en ordre invers
'''

# método 1
cadena = "mi casa es de color azul"
cadena2 = ''

for palabra in cadena:
  #for car in palabra:
    cadena2 = palabra + cadena2
print(cadena2)

# método 2
cadena = "mi casa es de color azul"
cadena2 = ''
for posicio in range(len(cadena)):
  #for letra in cadena[posicio]:
    cadena2 = cadena[posicio] + cadena2
print(cadena2)

# método 3
cadena = "mi casa es de color azul"
cadena2 = ''

for fila in range(len(cadena)):
  #for columna in range(len(cadena[fila])):
    cadena2 =  cadena[fila] + cadena2
print(cadena2)

'''
2-Comptar lletres:
Comptar el número de vegades que surt la lletra 'a' dins d'una cadena de text.
'''

# método 1

cadena = "amo de tu casa y amo de mi casa"
contador = 0
for letra in range(len(cadena)):
  if cadena[letra] in 'a':
#if cadena[letra] == 'a':
    contador += 1
print(contador)

#método 2

cadena = "amo de tu casa y amo de mi casa"
contador = 0
for letra in cadena:
  if letra in 'a':
 # if letra == 'a':
    contador +=1
print(contador)

#método 3
cadena = "amo de tu casa y amo de mi casa"
contador = 0
for fila in range(len(cadena)):
  if cadena[fila] == 'a':
    contador += 1
print(contador)

'''
6-Dissenya un programa que demani una paraula i l'escrigui per pantalla tantes vegades com la seva
 longitud:
exemple:
Exemple:

'''
#método 1
cadena = input("Entra una paraula: ")
for posicio in range(len(cadena)):
  print(cadena)

#método 2

cadena = input("Entra una paraula: ")

for letra in cadena:
  print(cadena)

#método 3
cadena = input("Entra una paraula: ")

for fila in range(len(cadena)):
  print(cadena)

'''
12.  Escriu un programa que rebi 2 cadenes i ens digui si la primera cadena està dins de l'altra.
user-bash$ python 11trobarcadena.py 'el' 'la casa no estaba'    --> Treu per pantalla: La
cadena 'el' NO està dins de 'la casa no estaba'
user-bash$ python 11trobarcadena.py 'el' 'l
'''


cadena1 = input("escriu 1ª cadena : ")
cadena2 = input("Escriu 2ª cadena: ")

if cadena2 in cadena1:
  print("la cadena2 está en la cadena1")
else:
  print('no está en la cadena 1')

#ejercicio subcadena

'''
Subcadena 1- Dissenya un programa que tregui tots els prefixes d'una cadena que rebem per paràmetre.
Per exemple la cadena "Fedora" treu per pantalla:
F
Fe
Fed
Fedo
Fedor
Fedora

'''
cadena = input("entra una palabra: ")
cadena2 = ''
for letra in cadena:
  cadena2 = cadena2 + letra
  print(cadena2)

#ejercicio subcadena
'''
2- Dissenya un programa que rebi per paràmetre una cadena i tregui per pantalla totes les
subcadenes de longitud 3.
Per exemple la cadena "planes" treu per pantalla:
pla
lan
ane
nes
'''
cadena = "planes"
cadena2 = ''

for pos in range(len(cadena)):

  cadena2 =  cadena2 + cadena[:3]

  print(cadena2)

'''
4-Comptar paraules:
Compta el número de paraules que hi ha dins d'una cadena de text que
li passeu per paràmetre (les paraules sempre estan separades per un o més espais en blanc)
Nota: Exemple de com passar un paràmetre amb espais
'''

cadena = input("Entra una frase : ")

paraula = cadena.split()

numero_paraules = len(paraula)

print(f"En la frase: {cadena} hay {numero_paraules} palabras")

''' 7- Dissenya un programa que rebi per input una frase qualsevol i compti les vocals.
Ens ha d'indicar per pantalla quina és la vocal més abundant i la vocal menys abundant.
Nota: Si una vocal no apareix té 0 coincidències i per tant és la menys abundant.
Per exemple:
user-bash$ python 6contavocals.py 'la porta esta tancada'
La a és la vocal més abundant amb 6 coincidències
La i és la vocal que és repeteix menys vegades amb 0 coincidències
'''

cadena = input("Entra una frase: ")

contador_a = 0
contador_u = 0
contador_i = 0
contador_o = 0
contador_e = 0


for car in cadena:
  if car == 'a':
    contador_a = contador_a + 1
  elif car == 'e':
    contador_e = contador_e + 1
  elif car == 'i':
    contador_i = contador_i + 1
  elif car == 'o':
    contador_o = contador_o + 1
  elif car == 'u':
    contador_u = contador_u + 1


maxi = max(contador_a,contador_u, contador_o, contador_i, contador_e)
mini = min(contador_a,contador_u, contador_o, contador_i, contador_e)

if maxi == contador_a:
  print("la a es la vocal mas abundante con", maxi, "coincidencias")
elif maxi == contador_u:
  print("la u es la vocal mas abundante con", maxi, "coincidencias")
elif maxi == contador_i:
  print("la i es la vocal mas abundante con", maxi, "coincidencias")
elif maxi == contador_o:
  print("la o es la vocal mas abundante con", maxi, "coincidencias")
else:
  print("la e es la vocal mas abundante con", maxi, "coincidencias")

if mini == contador_a:
  print("la a es la vocal menos abundante con", mini, "coincidencias")
elif mini == contador_u:
  print("la u es la vocal menos abundante con", mini, "coincidencias")
elif mini == contador_i:
  print("la i es la vocal menos abundante con", mini, "coincidencias")
elif mini == contador_o:
  print("la o es la vocal menos abundante con", mini, "coincidencias")
else:
  print("la e es la vocal menos abundante con", mini, "coincidencias")

'''
8- Escriu un programa que rebi per paràmetre una frase i reescrigui la frase afegint BONICA
PARAULA després de cada paraula
Exemple:
user-bash$ python 7reescriu.py 'la porta'
la BONICA PARAULA porta BONICA PARAULA
'''
cadena = input("Entra una frase: ")

nova_cad = cadena.split()

for car in nova_cad:
  print(f" {car} BONICA PARAULA " , end = "")

'''
9- Escriu un programa que rebi per paràmetre una frase i reescrigui la frase afegint la seva longitud
després de cada paraula
Exemple:
user-bash$ python 7reescriulen.py 'la porta tancaràs'
la2
porta5
tancaràs8'
'''

cadena = input("Escriu una frase: ")
n_cad = cadena.split()
for car in n_cad:
  print(f"{car}{len(car)}")

'''
10- Fes el mateix que el exercici 8 però escriu les paraules en la mateixa línia:
Exemple:
user-bash$ python 7reescriulen.py 'la porta contaràs'
la2 porta5 contaràs8'
'''
cadena = input("Escriu una frase: ")
nova_cad = cadena.split()

for car in nova_cad:
  print(f"{car}{len(car)} ", end ="")