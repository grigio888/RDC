import pygame, sys
import sqlite3

sys.path.append('C:/Users/Grigio/Desktop/GitHub/RDC')

from modulos.segmentacao import *
from modulos.classes import *

pygame.init

# variaveis:
janela_extras = ExibirImagem('modulos/setores/a_pagina_inicial/extras_ext/janela_extras.png', 920, 539, 7.4, 64.7)
texto_extras = Escrever(janela_extras.pos_x + 2, janela_extras.pos_y + 0.9, 'titulo', 'Extras', 'preto')

botao_criar_conta = ExibirImagem('modulos/setores/a_pagina_inicial/extras_ext/botao_medio.png', 314, 69, janela_extras.pos_x + 6.9, janela_extras.pos_y + 4.2)
texto_criar_conta = Escrever(botao_criar_conta.pos_x + 14.3, botao_criar_conta.pos_y + 0.9, 'corpo', 'Criar Conta', 'preto', 'centro')

botao_ok_extras = ExibirImagem('modulos/setores/a_pagina_inicial/extras_ext/botao_ok.png', 106, 69, janela_extras.pos_x + 72.9, janela_extras.pos_y + 22.2)
texto_ok_extras = Escrever(botao_ok_extras.pos_x + 5, botao_ok_extras.pos_y + 0.9, 'corpo', 'OK', 'preto', 'centro')

versao_aplicativo = Escrever(janela_extras.pos_x + 2.9, janela_extras.pos_y + 24.3, 'titulo', 'versao: 0.0.1a', 'cinza')



texto_criar_conta_titulo = Escrever(janela_extras.pos_x + 2, janela_extras.pos_y + 0.9, 'titulo', 'Criar conta', 'preto')

texto_login_extras = Escrever(janela_extras.pos_x + 10.2, janela_extras.pos_y + 4.5, 'corpo', 'Login:', 'preto')
campo_login_extras = ExibirImagem('modulos/setores/a_pagina_inicial/inicio_ext/campo_de_entrada.png', 714, 50, texto_login_extras.pos_x - 0.7, texto_login_extras.pos_y + 2.3)
texto_campo_login_extras = Escrever(campo_login_extras.pos_x + 1, campo_login_extras.pos_y + 0.4, 'titulo', '', 'preto')
texto_campo_login_extras_escrevendo = False
texto_campo_login_extras_entrada = ''

texto_email_extras = Escrever(janela_extras.pos_x + 10.2, janela_extras.pos_y + 9.8, 'corpo', 'Email:', 'preto')
campo_email_extras = ExibirImagem('modulos/setores/a_pagina_inicial/inicio_ext/campo_de_entrada.png', 714, 50, texto_email_extras.pos_x - 0.7, texto_email_extras.pos_y + 2.3)
texto_campo_email_extras = Escrever(campo_email_extras.pos_x + 1, campo_email_extras.pos_y + 0.4, 'titulo', '', 'preto')
texto_campo_email_extras_escrevendo = False
texto_campo_email_extras_entrada = ''

texto_senha_extras = Escrever(janela_extras.pos_x + 10.2, janela_extras.pos_y + 15.2, 'corpo', 'Senha:', 'preto')
campo_senha_extras = ExibirImagem('modulos/setores/a_pagina_inicial/inicio_ext/campo_de_entrada.png', 714, 50, texto_senha_extras.pos_x - 0.7, texto_senha_extras.pos_y + 2.3)
texto_campo_senha_extras = Escrever(campo_senha_extras.pos_x + 1, campo_senha_extras.pos_y + 0.4, 'titulo', '', 'preto')
texto_campo_senha_extras_real = Escrever(campo_senha_extras.pos_x + 1, campo_senha_extras.pos_y + 0.4, 'titulo', '', 'preto')
texto_campo_senha_extras_escrevendo = False
texto_campo_senha_extras_entrada = ''

botao_cancelar_extras = ExibirImagem('modulos/setores/a_pagina_inicial/extras_ext/botao_medio.png', 229, 69, janela_extras.pos_x + 15.5, janela_extras.pos_y + 22.3)
texto_cancelar_extras = Escrever(botao_cancelar_extras.pos_x + 10.5, botao_cancelar_extras.pos_y + 0.9, 'corpo', 'Cancelar', 'preto', 'centro')

botao_confirmar_extras = ExibirImagem('modulos/setores/a_pagina_inicial/extras_ext/botao_medio.png', 229, 69, janela_extras.pos_x + 48.5, janela_extras.pos_y + 22.3)
texto_confirmar_extras = Escrever(botao_confirmar_extras.pos_x + 10.5, botao_confirmar_extras.pos_y + 0.9, 'corpo', 'Confirma', 'preto', 'centro')



janela_aviso_extras = ExibirImagem('modulos/setores/a_pagina_inicial/extras_ext/janela_aviso_extras.png', 605, 327, 22.1, 70)
texto_aviso_extras = Escrever(janela_aviso_extras.pos_x + 2, janela_aviso_extras.pos_y + 0.9, 'titulo', 'Confirmacao', 'preto')

texto_central_aviso_1 = Escrever(janela_aviso_extras.pos_x + 27.9, janela_aviso_extras.pos_y + 3.7, 'corpo', 'Confirme a senha:', 'preto', 'centro')
campo_confirmacao_senha_aviso = ExibirImagem('modulos/setores/a_pagina_inicial/extras_ext/campo_senha.png', 536, 50, janela_aviso_extras.pos_x + 3.2, janela_aviso_extras.pos_y + 6.9)
texto_campo_confirmacao_senha_aviso = Escrever(campo_confirmacao_senha_aviso.pos_x + 1, campo_confirmacao_senha_aviso.pos_y + 0.4, 'titulo', '', 'preto')
texto_campo_confirmacao_senha_aviso_real = Escrever(campo_confirmacao_senha_aviso.pos_x + 1, campo_confirmacao_senha_aviso.pos_y + 0.4, 'titulo', '', 'preto')
texto_campo_confirmacao_senha_aviso_escrevendo = False
texto_campo_confirmacao_senha_aviso_entrada = ''

botao_nao_aviso_extras = ExibirImagem('modulos/setores/a_pagina_inicial/extras_ext/botao_ok.png', 106, 69, janela_aviso_extras.pos_x + 12.9, janela_aviso_extras.pos_y + 11.9)
texto_nao_aviso_extras = Escrever(botao_nao_aviso_extras.pos_x + 5, botao_nao_aviso_extras.pos_y + 0.9, 'corpo', 'Nao', 'preto', 'centro')

botao_ok_aviso_extras = ExibirImagem('modulos/setores/a_pagina_inicial/extras_ext/botao_ok.png', 106, 69, janela_aviso_extras.pos_x + 32.9, janela_aviso_extras.pos_y + 11.9)
texto_ok_aviso_extras = Escrever(botao_ok_aviso_extras.pos_x + 5, botao_ok_aviso_extras.pos_y + 0.9, 'corpo', 'OK', 'preto', 'centro')

texto_aviso_login_extras = Escrever(janela_aviso_extras.pos_x + 2, janela_aviso_extras.pos_y + 0.9, 'titulo', 'Aviso', 'preto')
texto_central_aviso_login_1 = Escrever(janela_aviso_extras.pos_x + 27.9, janela_aviso_extras.pos_y + 4.7, 'corpo', 'Este login ja', 'preto', 'centro')
texto_central_aviso_email_1 = Escrever(janela_aviso_extras.pos_x + 27.9, janela_aviso_extras.pos_y + 4.7, 'corpo', 'Este email ja', 'preto', 'centro')
texto_central_aviso_2 = Escrever(janela_aviso_extras.pos_x + 27.9, janela_aviso_extras.pos_y + 6.7, 'corpo', 'existe.', 'preto', 'centro')
botao_ok_aviso_login_extras = ExibirImagem('modulos/setores/a_pagina_inicial/extras_ext/botao_ok.png', 106, 69, janela_aviso_extras.pos_x + 23.2, janela_aviso_extras.pos_y + 11.9)
texto_ok_aviso_login_extras = Escrever(botao_ok_aviso_login_extras.pos_x + 5, botao_ok_aviso_login_extras.pos_y + 0.9, 'corpo', 'OK', 'preto', 'centro')

texto_central_aviso_conf_1 = Escrever(janela_aviso_extras.pos_x + 27.9, janela_aviso_extras.pos_y + 4.7, 'corpo', 'Cadastro concluido', 'preto', 'centro')
texto_central_aviso_conf_2 = Escrever(janela_aviso_extras.pos_x + 27.9, janela_aviso_extras.pos_y + 6.7, 'corpo', 'com sucesso.', 'preto', 'centro')

# funcoes:
def desenho_pagina_extras():
    janela_extras.desenho()
    texto_extras.desenho()

    botao_criar_conta.desenho()
    texto_criar_conta.desenho()

    botao_ok_extras.desenho()
    texto_ok_extras.desenho()

    versao_aplicativo.desenho()



def desenho_pagina_criar_conta():
    janela_extras.desenho()
    texto_criar_conta_titulo.desenho()

    texto_login_extras.desenho()
    campo_login_extras.desenho()
    texto_campo_login_extras.desenho()

    texto_email_extras.desenho()
    campo_email_extras.desenho()
    texto_campo_email_extras.desenho()

    texto_senha_extras.desenho()
    campo_senha_extras.desenho()
    texto_campo_senha_extras.desenho()

    botao_cancelar_extras.desenho()
    texto_cancelar_extras.desenho()

    botao_confirmar_extras.desenho()
    texto_confirmar_extras.desenho()

def entrando_criar_conta():
    texto_campo_login_extras.frase = ''
    texto_campo_email_extras.frase = ''
    texto_campo_senha_extras.frase = ''
    texto_campo_senha_extras_real.frase = ''

def escrever_login_email_senha_extras(event):
    
    global texto_campo_login_extras_escrevendo, texto_campo_email_extras_escrevendo, texto_campo_senha_extras_escrevendo, texto_campo_login_extras_entrada, texto_campo_email_extras_entrada, texto_campo_senha_extras_entrada

    if event.type == pygame.MOUSEBUTTONDOWN:
        if pygame.mouse.get_pos()[0] >= campo_login_extras.porcentagem_pos_x:
            if pygame.mouse.get_pos()[1] >= campo_login_extras.porcentagem_pos_y:
                if pygame.mouse.get_pos()[0] <= campo_login_extras.porcentagem_pos_x + campo_login_extras.largura_transformada:
                    if pygame.mouse.get_pos()[1] <= campo_login_extras.porcentagem_pos_y + campo_login_extras.altura_transformada:
                        texto_campo_login_extras_escrevendo = True
                        if texto_campo_login_extras_escrevendo == texto_campo_email_extras_escrevendo:
                            texto_campo_email_extras_escrevendo = False

                        if texto_campo_login_extras_escrevendo == texto_campo_senha_extras_escrevendo:
                            texto_campo_senha_extras_escrevendo = False

        if pygame.mouse.get_pos()[0] >= campo_email_extras.porcentagem_pos_x:
            if pygame.mouse.get_pos()[1] >= campo_email_extras.porcentagem_pos_y:
                if pygame.mouse.get_pos()[0] <= campo_email_extras.porcentagem_pos_x + campo_email_extras.largura_transformada:
                    if pygame.mouse.get_pos()[1] <= campo_email_extras.porcentagem_pos_y + campo_email_extras.altura_transformada:
                        texto_campo_email_extras_escrevendo = True
                        if texto_campo_email_extras_escrevendo == texto_campo_login_extras_escrevendo:
                            texto_campo_login_extras_escrevendo = False

                        if texto_campo_email_extras_escrevendo == texto_campo_senha_extras_escrevendo:
                            texto_campo_senha_extras_escrevendo = False

        if pygame.mouse.get_pos()[0] >= campo_senha_extras.porcentagem_pos_x:
            if pygame.mouse.get_pos()[1] >= campo_senha_extras.porcentagem_pos_y:
                if pygame.mouse.get_pos()[0] <= campo_senha_extras.porcentagem_pos_x + campo_senha_extras.largura_transformada:
                    if pygame.mouse.get_pos()[1] <= campo_senha_extras.porcentagem_pos_y + campo_senha_extras.altura_transformada:
                        texto_campo_senha_extras_escrevendo = True
                        if texto_campo_senha_extras_escrevendo == texto_campo_login_extras_escrevendo:
                            texto_campo_login_extras_escrevendo = False

                        if texto_campo_senha_extras_escrevendo == texto_campo_email_extras_escrevendo:
                            texto_campo_email_extras_escrevendo = False
        else:
            texto_campo_login_extras_escrevendo = False
            texto_campo_email_extras_escrevendo = False
            texto_campo_senha_extras_escrevendo = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
            if texto_campo_login_extras_escrevendo:
                texto_campo_login_extras_escrevendo = False

            if texto_campo_email_extras_escrevendo:
                texto_campo_email_extras_escrevendo = False

            if texto_campo_senha_extras_escrevendo:
                texto_campo_senha_extras_escrevendo = False

        elif event.key == pygame.K_BACKSPACE:
            if texto_campo_login_extras_escrevendo:
                texto_campo_login_extras.frase = texto_campo_login_extras.frase[:-1]

            if texto_campo_email_extras_escrevendo:
                texto_campo_email_extras.frase = texto_campo_email_extras.frase[:-1]

            if texto_campo_senha_extras_escrevendo:
                texto_campo_senha_extras_real.frase = texto_campo_senha_extras_real.frase[:-1]

        else:
            if texto_campo_login_extras_escrevendo:
                texto_campo_login_extras.frase += event.unicode

            if texto_campo_email_extras_escrevendo:
                texto_campo_email_extras.frase += event.unicode

            if texto_campo_senha_extras_escrevendo:
                texto_campo_senha_extras_real.frase += event.unicode
                
    if len(texto_campo_senha_extras.frase) > len(texto_campo_senha_extras_real.frase):
        texto_campo_senha_extras.frase = texto_campo_senha_extras.frase [:-1]

    elif len(texto_campo_senha_extras.frase) < len(texto_campo_senha_extras_real.frase):
        texto_campo_senha_extras.frase += '*'

def verificando_duplicidade_cadastro():

    global texto_campo_login_extras, texto_campo_email_extras

    comando = (f'select login from login where login = "{texto_campo_login_extras.frase}"')
    comparador_login = db_login.ler(comando)
    comando = (f'select email from login where email = "{texto_campo_email_extras.frase}"')
    comparador_email = db_login.ler(comando)

    if len(comparador_login) == 1: return 'login duplicado'
    elif len(comparador_login) == 0 and len(comparador_email) == 1: return 'email duplicado'
    else: return 'ok'



def desenho_pagina_aviso_extras(setor):
    janela_aviso_extras.desenho()
    
    if setor == 'ok':
        texto_aviso_extras.desenho()

        texto_central_aviso_1.desenho()
        campo_confirmacao_senha_aviso.desenho()
        texto_campo_confirmacao_senha_aviso.desenho()

        botao_nao_aviso_extras.desenho()
        texto_nao_aviso_extras.desenho()

        botao_ok_aviso_extras.desenho()
        texto_ok_aviso_extras.desenho()

    elif setor == 'login duplicado' or setor == 'email duplicado':

        texto_aviso_login_extras.desenho()
        if setor == 'login duplicado':
            texto_central_aviso_login_1.desenho()
        if setor == 'email duplicado':
            texto_central_aviso_email_1.desenho()
        texto_central_aviso_2.desenho()
        
        botao_ok_aviso_login_extras.desenho()
        texto_ok_aviso_login_extras.desenho()

    elif setor == 'cadastro concluido':

        texto_aviso_extras.desenho()

        texto_central_aviso_conf_1.desenho()
        texto_central_aviso_conf_2.desenho()
        
        botao_ok_aviso_login_extras.desenho()
        texto_ok_aviso_login_extras.desenho()


def escrever_senha_confirmacao_extras(event):
    
    global texto_campo_confirmacao_senha_aviso, texto_campo_confirmacao_senha_aviso_escrevendo
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        if pygame.mouse.get_pos()[0] >= campo_confirmacao_senha_aviso.porcentagem_pos_x:
            if pygame.mouse.get_pos()[1] >= campo_confirmacao_senha_aviso.porcentagem_pos_y:
                if pygame.mouse.get_pos()[0] <= campo_confirmacao_senha_aviso.porcentagem_pos_x + campo_confirmacao_senha_aviso.largura_transformada:
                    if pygame.mouse.get_pos()[1] <= campo_confirmacao_senha_aviso.porcentagem_pos_y + campo_confirmacao_senha_aviso.altura_transformada:
                        texto_campo_confirmacao_senha_aviso_escrevendo = True

        else:
            texto_campo_confirmacao_senha_aviso_escrevendo = False

    if event.type == pygame.KEYDOWN:
        if texto_campo_confirmacao_senha_aviso_escrevendo:
            if event.key == pygame.K_RETURN:
                texto_campo_confirmacao_senha_aviso_escrevendo = False

            elif event.key == pygame.K_BACKSPACE:
                texto_campo_confirmacao_senha_aviso_real.frase = texto_campo_confirmacao_senha_aviso_real.frase[:-1]

            else:
                texto_campo_confirmacao_senha_aviso_real.frase += event.unicode
                
    if len(texto_campo_confirmacao_senha_aviso.frase) > len(texto_campo_confirmacao_senha_aviso_real.frase):
        texto_campo_confirmacao_senha_aviso.frase = texto_campo_confirmacao_senha_aviso.frase [:-1]
    elif len(texto_campo_confirmacao_senha_aviso.frase) < len(texto_campo_confirmacao_senha_aviso_real.frase):
        texto_campo_confirmacao_senha_aviso.frase += '*'

def adicionando_cadastro():

    global texto_campo_login_extras, texto_campo_email_extras, texto_campo_senha_extras_real

    db_login.executar(f'insert into login values ("{texto_campo_login_extras.frase}", "{texto_campo_senha_extras_real.frase}", "{texto_campo_email_extras.frase}")')
    db_login.executar(f'insert into opcoes values ("{texto_campo_login_extras.frase}", 1, 20, 1, 20, 1)"')
    db_login.executar(f'insert into info_conta values ("{texto_campo_login_extras.frase}", 0, 0, 1000)"')
    db_login.executar(f'insert into personagens values ("{texto_campo_login_extras.frase}", 0, "padrao", 0, 0, 0, 0, 0, 0, 0, 0)')

if __name__ == '__main__':

    from modulos.segmentacao import tela_largura, tela_altura, tela_resolucao, tela, game_rodando
    relogio_de_atualizacao = pygame.time.Clock()
    ponteiro = 30

    while game_rodando:

        while subsetor:

            definindo_setor_aviso_extras('login duplicado')

            # definindo evento de saida
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_rodando = False
                    subsetor = False

                # interacao com o mouse


            # desenhando elementos na tela
            desenho_pagina_inicial()
            desenho_pagina_criar_conta()
            desenho_pagina_aviso_extras('login duplicado')

            # atualizacao da tela
            pygame.display.update()
            relogio_de_atualizacao.tick(ponteiro)

            tela_tamanho = pygame.display.get_window_size()