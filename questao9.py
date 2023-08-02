'''
Fazer um algoritmo que pergunte 1 número e apresente:
a)	O próprio número
b)	O quadrado deste número
c)	A raiz quadrada deste número
'''
import math

numero = float(input("Me diga um número:"))
quadrado = math.pow(numero,2)
raiz = 	math.sqrt(numero)

print("O seu número é:",numero)
print("O quadrado seu número é:",quadrado)
print("E a raiz quadrada do seu número é:",raiz)