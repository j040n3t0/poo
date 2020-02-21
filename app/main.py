# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
import compromisso, entrevistador

if __name__ == '__main__':
	obj_entrevistador = entrevistador.Entrevistador()
	obj_compromisso = compromisso.Compromisso()

	obj_entrevistador.nome = "João Neto"
	obj_compromisso.horainicio = "2020-02-20 23:45:00"
	tempo_reuniao = 15
	hora_fim = obj_compromisso.horainicio + timedelta(minutes=tempo_reuniao)
	print(hora_fim)


	print(obj_entrevistador.nome)
	print(obj_compromisso.horainicio)
