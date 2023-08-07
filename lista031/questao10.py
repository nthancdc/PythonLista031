'''
Fazer um algoritmo que efetue o cálculo do valor de uma prestação em atraso, utilizando a fórmula prestação	=	valor	+	(valor	x	(taxa	:	100)	x	tempo	em	dias).

Perguntar ao usuário:
- valor normal da prestação
- taxa de juros
- tempo em dias

Resposta:
- valor da prestação em atraso
'''

valor = float(input("Qual foi o valor da prestação?"))
taxa = float(input("Qual é o valor da taxa de juros?"))
tempo = float(input("Quantos dias a prestação está atrasada?"))

prestacao = valor + (valor * (taxa / 100) * tempo)

print("O valor da prestação em atraso, foi de: R$",prestacao)