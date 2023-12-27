from datetime import date

data_atual = date.today()
data_atual = str(data_atual).split('-')
ano_atual = int(data_atual[0])
mes_atual = int(data_atual[1])
dia_atual = int(data_atual[2])

data_nasc= input('digite a data de nascimento(AA-MM-DD): ').split('-')
ano_nasc = int(data_nasc[0])
mes_nasc = int(data_nasc[1])
dia_nasc = int(data_nasc[2])

idade = ano_atual - ano_nasc

if mes_nasc > mes_atual or (mes_nasc == mes_atual and dia_nasc > dia_atual):
    idade = ano_atual - ano_nasc - 1

print('A idade é: ', str(idade))
