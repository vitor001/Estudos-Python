import smtplib
import ssl

de = 'emaildeexemplo@gmail.com'
senha = 'vitor123'
para = 'vitor.augusto.vitor@gmail.com'
msg = ''' Olá, mundo!

E-mail de teste enviado pelo python

'''
context = ssl.create_default_context()
with smtplib.SMTP('smtp.gmail.com', 587) as conexao:
    conexao.ehlo()
    conexao.starttls(context=context)
    conexao.login(de, senha)
    conexao.sendmail(de, para, msg)
