'''
Elaborar um programa que pergunte quatro valores inteiros e apresente 2 resultados:  a) Resultado de suas adições
b) Resultado de suas multiplicações
'''

num1 = int(input("Me diga um número:"))
num2 = int(input("Me diga um outro número:"))
num3 = int(input("Me diga mais um número:"))
num4 = int(input("Me diga somente mais um número:"))

soma = num1 + num2 + num3 + num4
produto = num1 * num2 * num3 * num4

print("O resultado da soma destes números é:",soma)
print("O resultado das multiplicações destes números é:",produto)2