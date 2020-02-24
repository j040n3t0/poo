# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

class Compromisso:
	def __init__(self):
		pass

	def agendarCompromisso(self, nome):
		if nome:
			start_date = input("Informe o horario do compromisso: (dd/mm/aa hh:mm) ")
			howlong = input("Informe o tempo de duração do compromisso em minutos: ")
			date_1 = datetime.strptime(start_date, "%d/%m/%y %H:%M")
			end_date = date_1 + timedelta(minutes=int(howlong))

			print(f'\n\nOla {nome} seu compromisso inicia {start_date} e termina às {end_date}!! \n\n')
		else:
			return "Necessário cadastrar a pessoa!"

















	# def definirPeso(self, peso):
	# 	self.peso = peso

	# def obterPeso(self):
	# 	return str(self.peso) + ' Kg'


"""
Método INIT da classe: O método init é um método especial para classes. O init é um método construtor, ele inicializa o estado de um objeto. O método init é invocado a cada nova instância de uma classe é criada. Na verdade não estamos apenas definindo o método init mais sobrescrevendo o init da classe base.
Refer: https://wiki.python.org.br/ProgramacaoOrientadaObjetoPython#A5._Classes
"""