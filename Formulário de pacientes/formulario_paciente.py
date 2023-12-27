from datetime import date

nome = input("Nome completo: ")
email = input("Email: ")
cpf = input("CPF: ")
rg = input("RG: ")
tel = input("Telefone: ")
data_nasc= input('data de nascimento(AA-MM-DD): ').split('-')
ano_nasc = int(data_nasc[0])
mes_nasc = int(data_nasc[1])
dia_nasc = int(data_nasc[2])
#calculando a idade
data_atual = date.today()
data_atual = str(data_atual).split('-')
ano_atual = int(data_atual[0])
mes_atual = int(data_atual[1])
dia_atual = int(data_atual[2])

idade = ano_atual - ano_nasc

if mes_nasc > mes_atual or (mes_nasc == mes_atual and dia_nasc > dia_atual):
    idade = ano_atual - ano_nasc - 1


with open('pacientes.txt', 'a') as arquivo:
    arquivo.write('Nome completo: ' + nome + '\n')
    arquivo.write('Email: ' + email +'\n')
    arquivo.write('CPF ' + cpf +'\n')
    arquivo.write('RG: ' + rg +'\n')
    arquivo.write('Telefone: ' + tel +'\n')
    arquivo.write('Idade: ' + str(idade) +'\n')
    if idade >= 65:
        arquivo.write('<-- Paciente de risco!!! --> \n' )
    arquivo.write('/ ------ \n' * 10 )
    arquivo.write('\n')