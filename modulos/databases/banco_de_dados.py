import sqlite3

def executando_acao_db(database, acao, comando):

    conectante = sqlite3.connect(database)
    cursor = conectante.cursor()

    acao = acao.lower()

    if acao == 'create' or acao == 'insert' or acao == 'update' or acao == 'delete':
        cursor.execute(comando)
        conectante.commit()
        conectante.close()

    if acao == 'select':
        cursor.execute(comando)
        dados_de_saida = cursor.fetchall()
        conectante.commit()
        conectante.close()
        return dados_de_saida

    print("Comando " + acao.upper() + " executado.")

class FerramentaBancoDeDados():
	
	def __init__(self, database):
		self.database = database
		self.resultado = 0

	def executar(self, comando):
		login = sqlite3.connect(self.database) #Loga
		cursor = login.cursor() #Aponta
		executar = (comando) #Recebe comando
		cursor.execute(executar) #Executa comando
		login.commit() #Commit
		login.close() #Encerra conexão

	def ler(self, comando):
		login = sqlite3.connect(self.database) #Loga
		cursor = login.cursor() #Aponta
		executar = (comando) #Recebe comando
		cursor.execute(executar) #Executa comando
		self.resultado = cursor.fetchall() #Lê o cursor
		login.close() #Encerra conexão

if __name__ == "__main__":

    #database = 'modulos/databases/local_conta.db'
    #tabela = 'info_conta'
    #executando_acao_db(database, 'create', 'CREATE TABLE ' + tabela +' (login_FK text, no_char int, score int, zeny int, foreign key(login_FK) references login(login))')
    #executando_acao_db(database, 'insert', 'INSERT INTO ' + tabela + ' VALUES ("condiporta7", 0, 0, 1000)')
    
    #print('\n')
    #variavel_1 = executando_acao_db(database, 'select', "SELECT rowid, name FROM sqlite_master WHERE type='table'")
    #print('Tabelas na database: '+database)
    #for item in variavel_1:
    #    print(item)

    #print('\n')
    #for item in variavel_1:
    #    print('Itens na tabela: ' + str(item[1]))
    #    variavel_2 = executando_acao_db(database, 'select', 'SELECT rowid, * FROM ' + str(item[1]))
    #    for item in variavel_2:
    #        print(item)
    #    print('\n')

    #login = 'grigio888'
    #senha = 'kiju1475'
    #print(executando_acao_db(database, 'select', 'SELECT login, senha FROM login WHERE login = "'+login+'" and senha = "'+senha+'"'))
    #print(executando_acao_db(database, 'select', 'SELECT login.login, opcoes.bgm_vol, info_conta.zeny FROM ((' + tabela + ' INNER JOIN opcoes ON login.login = opcoes.login_FK) inner join info_conta on login.login = info_conta.login_FK)'))

    db_login = FerramentaBancoDeDados('modulos/databases/local_conta.db')

    comando_1 = ('CREATE TABLE personagens (login_FK text, criado int, nome text, cabelo int, classe int, for int, agi int, vit int, inte int, des int, sor int, foreign key (login_FK) references login (login))')
    comando_2 = ('insert into personagens values ("condiporta7", 0, "padrao", 0, 0, 0, 0, 0, 0, 0, 0)')
    #db_login.executar(comando_2)

    db_login.ler('SELECT rowid, name FROM sqlite_master WHERE type="table"')
    for item in db_login.resultado:
        print(item)
        db_login.ler('select * from "'+str(item[1])+'"')
        for item in db_login.resultado:
            print(item)

    rodando = False
    while rodando:
        print('Ferramenta auxiliadora - Banco de Dados')
        setor = 'inserir_db'

        while setor == 'inserir_db':
            database = input('Insira o nome do banco de dados: ')
            setor = 'verificar_db'

        while setor == 'verificar_db':
            try:
                conectante = sqlite3.connect(database)
                conectante.close()
                print('Conectado com sucesso.')
                setor = 'receber_acao'

            except:
                print(Exception)
                print('Retornando ao menu inicial.')
                setor = 'inserir_db'

        while setor == 'receber_acao':
            print(executando_acao_db(database, 'select', "SELECT rowid, name FROM sqlite_master WHERE type='table'"))
            print('Insira a query SQL a ser executada:\n')
            comando = input('')
            setor = 'tratando_acao'

        while setor == 'tratando_acao':
            p_comando = comando.split()[0]
            executando_acao_db(database, p_comando, comando)
