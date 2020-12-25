import mysql.connector as conector

def lendo_dados():

    texto_campo_login = 'grigio888'
    texto_campo_senha = 'kiju1475'

    login = conector.connect(user='root',
                             password='kiju1475',
                             host='localhost',
                             database='rdc')

    cursor = login.cursor()

    comando = ('select noChar, score, zeny from login join informacoes_da_conta on infos_FK where login = %s and senha = %s')
    cursor.execute(comando, (texto_campo_login, texto_campo_senha))

    variavel_teste = cursor.fetchall()
    print(variavel_teste)
    print('noChar = ' + str(variavel_teste[0][0]))
    print(len(variavel_teste))

    login.close()

def escrever_dados():
    login = conector.connect(user='root',
                             password='kiju1475',
                             host='localhost',
                             database='rdc')

    cursor = login.cursor()

    cursor.execute('update opcoes set bgm_caixa = True')
    cursor.execute('select * from opcoes')

    variavel_teste = cursor.fetchall()
    print(variavel_teste)

    login.commit()
    login.close()


lendo_dados()
#escrever_dados()

# Testando modulo 'time':

from time import gmtime, strftime

tempo = strftime("%S", gmtime())
#print(tempo)

if __name__ == '__main__' :
    pass