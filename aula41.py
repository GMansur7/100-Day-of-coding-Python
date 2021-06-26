#list = ["a","b","c","d"]
import random, time

dados = input("Give me everybody's names, separated by a comma: ")

dados_tratados = dados.split(", ")
#print(dados_tratados)

n = len(dados_tratados)
while 1:
	número = random.randint(0, n -1)
	nome = dados_tratados[número]
	print(f"{nome} paga a conta")
	time.sleep(0.1)