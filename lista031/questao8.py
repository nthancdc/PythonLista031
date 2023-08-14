'''Fazer um programa que calcule e apresente a quantidade de litros que um automóvel gastará em uma viagem. O programa deve coletar as seguintes informações: Distância a percorrer na viagem, em quilômetros; qual é o valor do consumo médio do automóvel, em quilômetros por litro
'''

distancia = float(input("Qual é a distância da viagem em Km?"))
consumo = float(input("Quantos Km o seu automóvel anda com um litro?"))

litros = distancia / consumo

print("Então a quantidade de litros gasta na sua viagem foi de:",litros,"litros")
