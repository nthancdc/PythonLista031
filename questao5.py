'''
Fazer um programa que pergunte o salário de um funcionário e apresente este salário com um aumento de 15%
'''

salariobruto = float(input("Quanto que é o seu salário?"))
acrescimo = salariobruto + (15 * salariobruto) / 100

print("Então o valor do seu salário com um aumento de 15% seria: R$",acrescimo)
