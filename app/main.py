# -*- coding: utf-8 -*-

import os
import compromisso, entrevistador

os.system("cls")
listEntrevistador = []
dictObjetos = {}

if __name__ == '__main__':

	compromissos = compromisso.Compromisso()

	def addEntrevistador():
		nome = input("Informe o nome: ")
		listEntrevistador.append(nome)
		dictObjetos[nome] = entrevistador.Entrevistador()
		dictObjetos[nome].definirNome(nome)
		return print(f'Entrevistador {nome} adicionado!')
	
	def showEntrevistador():
		return "January"

	def addCompromisso(nome):
		compromissos.agendarCompromisso(dictObjetos[nome].nome)
		return print(f'Compromisso adicionado para o entrevistador {nome}!') 

	def showCompromisso():
		return "January"

	def agenda(argument):
		switcher = {
			1: addEntrevistador,
			2: showEntrevistador,
			3: addCompromisso,
			4: showCompromisso,
		}
		# Get the function from switcher dictionary
		func = switcher.get(argument, lambda: "Argumento inválido!!")
		# Execute the function
		print(func())

	while True:
		print("Selecione ao nº da opção... \n \
1: addEntrevistador \n \
2: showEntrevistador \n \
3: addCompromisso \n \
4: showCompromisso \n \
5: stop \n\n")
		opt = input()
		if opt == "5":
			break 
		else:
			agenda(int(opt))












	# Imprimir os tipos dos objetos
	# for i in listEntrevistador:
	# 	print(type(i))








	# pessoa = entrevistador.Entrevistador()
	# compromissos = compromisso.Compromisso()

	# while True:
	# 	opt = input("Inserir nova pessoa? (y/n) ")
	# 	if opt == "y":
	# 		pessoa.definirNome()
	# 	else:
	# 		break
	
	#compromissos.agendarCompromisso(pessoa.nome)
	
	# print("Segue a lista de entrevistadores...")
	# if not pessoa.nomeList:
	# 	print("Ops... Lista de entrevistadores vazia!\n\n")
	# else:
	# 	for i in pessoa.nomeList:
	# 		print(f'> {i}')
	# 		print("\n\nFIM DO SCRIPT\n\n")
	
	
	
	#pessoa1.retornaNome()

	#obj_entrevistador = entrevistador.Entrevistador()
	#obj_compromisso = compromisso.Compromisso()

	# obj_entrevistador.nome = "João Neto"
	# obj_compromisso.horainicio = "2020/02/20 23:45:00"
	# tempo_reuniao = 15
	# hora_fim = obj_compromisso.horainicio + timedelta(minutes=tempo_reuniao)
	# print(hora_fim)

	# print(obj_entrevistador.nome)
	# print(obj_compromisso.horainicio)
