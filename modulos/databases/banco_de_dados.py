import sqlite3

class FerramentaBancoDeDados():
	
	def __init__(self, database):
		self.database = database
		self.resultado = 0

	def executar(self, comando, *_args):
		login = sqlite3.connect(self.database) #Loga
		cursor = login.cursor() #Aponta
		executar = (comando) #Recebe comando
		cursor.execute(executar, _args) #Executa comando
		login.commit() #Commit
		login.close() #Encerra conexão

	def ler(self, comando):
		login = sqlite3.connect(self.database) #Loga
		cursor = login.cursor() #Aponta
		executar = (comando) #Recebe comando
		cursor.execute(executar) #Executa comando
		self.resultado = cursor.fetchall() #Lê o cursor
		login.close() #Encerra conexão
		return self.resultado


if __name__ == "__main__":

    db_login = FerramentaBancoDeDados('modulos/databases/local_conta.db')

    comando_1 = ('CREATE TABLE personagens (login_FK text, criado int, nome text, cabelo int, classe int, for int, agi int, vit int, inte int, des int, sor int, foreign key (login_FK) references login (login))')
    comando_2 = ('insert into personagens values ("condiporta7", 0, "padrao", 0, 0, 0, 0, 0, 0, 0, 0)')
    comando_3 = ('update opcoes set bgm_cx = %s where login_FK = %s')
    comando_4 = ('delete from info_conta where rowid = "4"')
    comando_5 = ('select criado from login inner join personagens on login.login = personagens.login_FK where login = "grigio888"')
    comando_6 = ('select name from sqlite_master where type = "table" and name = "personagens"')
    comando = ('update opcoes set bgm_cx = %s where login_FK = "grigio888"')


    
    print(db_login.ler('show table "personagens"'))


    comando_loop = ('SELECT rowid, name FROM sqlite_master WHERE type="table"')
    for item in db_login.ler(comando_loop):
        print('\n' + str(item))
        comando_loop2 = (f'select rowid, * from "{item[1]}"')
        for item in db_login.ler(comando_loop2):
            print(item)