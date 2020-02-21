# -*- coding: utf-8 -*-

class Carro:
	def __init__(self):
		self.peso = 1000.0

	def definirPeso(self, peso):
		self.peso = peso

	def obterPeso(self):
		return str(self.peso) + ' Kg'


"""
Método INIT da classe: O método init é um método especial para classes. O init é um método construtor, ele inicializa o estado de um objeto. O método init é invocado a cada nova instância de uma classe é criada. Na verdade não estamos apenas definindo o método init mais sobrescrevendo o init da classe base.
Refer: https://wiki.python.org.br/ProgramacaoOrientadaObjetoPython#A5._Classes
"""