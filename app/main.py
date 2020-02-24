# -*- coding: utf-8 -*-

import os
#from datetime import datetime, timedelta
import datetime
import compromisso, entrevistador

os.system("cls")

if __name__ == '__main__':
	obj_entrevistador = entrevistador.Entrevistador()
	obj_compromisso = compromisso.Compromisso()

	start_date = input("Informe o horario do compromisso: (dd/mm/aa hh:mm) ")
	howlong = input("Informe o tempo de duração do compromisso em minutos: ")
	#start_date = "10/10/20 16:16"

	date_1 = datetime.datetime.strptime(start_date, "%d/%m/%y %H:%M")
	end_date = date_1 + datetime.timedelta(minutes=int(howlong))

	print(f'\n\n {end_date} \n\n')

	# obj_entrevistador.nome = "João Neto"
	# obj_compromisso.horainicio = "2020/02/20 23:45:00"
	# tempo_reuniao = 15
	# hora_fim = obj_compromisso.horainicio + timedelta(minutes=tempo_reuniao)
	# print(hora_fim)


	# print(obj_entrevistador.nome)
	# print(obj_compromisso.horainicio)
