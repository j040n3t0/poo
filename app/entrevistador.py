# -*- coding: utf-8 -*-

class Entrevistador:
    def __init__(self, nome):
        self.__nome = nome
        self.__agenda = None

    @property
    def nome(self):
        return self.__nome

    @property
    def agenda(self):
        return self.__agenda

    @agenda.setter
    def agenda(self, agenda):
        self.__agenda = agenda







"""
class Entrevistador:
	#nomeList = []

	#def __init__(self):
	#	pass

	def definirNome(self, nome):
		self.nome = nome
		#self.nome = input("Informe seu nome.: ")
		#Entrevistador.nomeList.append(self.nome)

	def retornaNome(self):
		return print(f"Seu nome é {self.nome}")




"""
#"""
#Método INIT da classe: O método init é um método especial para classes. O init é um método construtor, ele inicializa o estado de um objeto. O método init é invocado a cada nova instância de uma classe é criada. Na verdade não estamos apenas definindo o método init mais sobrescrevendo o init da classe base.
#Refer: https://wiki.python.org.br/ProgramacaoOrientadaObjetoPython#A5._Classes
# """