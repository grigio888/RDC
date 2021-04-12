import pygame, sys
import sqlite3

sys.path.append('C:/Users/Grigio/Desktop/GitHub/RDC')

from modulos.segmentacao import *
from modulos.classes import *

pygame.init()
pygame.mixer.init()

# variaveis:
fundo = ExibirImagem('modulos/setores/a_pagina_inicial/inicio_ext/fundo.png', 1080, 2020, 0, 0)
logo = ExibirImagem('modulos/setores/a_pagina_inicial/inicio_ext/logo.png', 950, 600, 7, 11.5)

janela_inicio = ExibirImagem('modulos/setores/a_pagina_inicial/inicio_ext/janela_inicio.png', 972, 414, 5, 67.5)
texto_inicio = Escrever(janela_inicio.pos_x + 2, janela_inicio.pos_y + 0.9, 'titulo', 'Inicio', 'preto')

texto_login = Escrever(janela_inicio.pos_x + 12.7, janela_inicio.pos_y + 3.9, 'corpo', 'Login:', 'azul')
campo_login = ExibirImagem('modulos/setores/a_pagina_inicial/inicio_ext/campo_de_entrada.png', 714, 50, janela_inicio.pos_x + 12, janela_inicio.pos_y + 6.1)
texto_campo_login = Escrever(janela_inicio.pos_x + 13, janela_inicio.pos_y + 6.5, 'titulo', '', 'preto')
texto_campo_login_escrevendo = False
texto_campo_login_entrada = ''

texto_senha = Escrever(janela_inicio.pos_x + 12.7, janela_inicio.pos_y + 9.2, 'corpo', 'Senha:', 'azul')
campo_senha = ExibirImagem('modulos/setores/a_pagina_inicial/inicio_ext/campo_de_entrada.png', 714, 50, janela_inicio.pos_x + 12, janela_inicio.pos_y + 11.4)
texto_campo_senha = Escrever(janela_inicio.pos_x + 13, janela_inicio.pos_y + 11.8, 'titulo', '', 'preto')
texto_campo_senha_real = Escrever(101, 101, 'corpo', '', 'preto')
texto_campo_senha_escrevendo = False
texto_campo_senha_entrada = ''

botao_entrar = ExibirImagem('modulos/setores/a_pagina_inicial/inicio_ext/botao_pagina_inicial.png', 219, 69, janela_inicio.pos_x + 21.8, janela_inicio.pos_y + 16.2)
texto_entrar = Escrever(botao_entrar.pos_x + 10.2, botao_entrar.pos_y + 0.8, 'botao', 'Entrar', 'preto', 'centro')

botao_sair = ExibirImagem('modulos/setores/a_pagina_inicial/inicio_ext/botao_pagina_inicial.png', 219, 69, janela_inicio.pos_x + 48.3, janela_inicio.pos_y + 16.2)
texto_sair = Escrever(botao_sair.pos_x + 10.2, botao_sair.pos_y + 0.8, 'botao', 'Sair', 'preto', 'centro')

botao_extras = ExibirImagem('modulos/setores/a_pagina_inicial/inicio_ext/botao_extras.png', 69, 69, janela_inicio.pos_x + 81.7, janela_inicio.pos_y + 16.2)



janela_aviso = ExibirImagem('modulos/setores/a_pagina_inicial/inicio_ext/janela_aviso.png', 483, 278, 27.7, 70.5)
texto_aviso = Escrever(janela_aviso.pos_x + 2, janela_aviso.pos_y + 0.9, 'titulo', 'Aviso', 'preto')

texto_do_aviso_1 = Escrever(janela_aviso.pos_x + 22.3, janela_aviso.pos_y + 4.5, 'atributo', 'Login e/ou senha', 'preto', 'centro')
texto_do_aviso_2 = Escrever(janela_aviso.pos_x + 22.3, janela_aviso.pos_y + 6.5, 'atributo', 'estao incorretos.', 'preto', 'centro')

botao_ok_aviso = ExibirImagem('modulos/setores/a_pagina_inicial/inicio_ext/botao_curto.png', 106, 69, janela_aviso.pos_x + 17.5, janela_aviso.pos_y + 9.5)
texto_ok_aviso = Escrever(botao_ok_aviso.pos_x + 5, botao_ok_aviso.pos_y + 0.9, 'corpo', 'OK', 'preto', 'centro')

db_login = FerramentaBancoDeDados('modulos/databases/local_conta.db')

# funcoes:
def musica_menu_inicio():
    if not pygame.mixer.get_busy():
        pygame.mixer.music.load('modulos/som/bgm/login.ogg')
        pygame.mixer.music.play(-1)
        
    elif pygame.mixer.get_busy() == True:
        pass

def desenho_pagina_inicial():
    fundo.desenho()
    logo.desenho()
    
    janela_inicio.desenho()
    texto_inicio.desenho()

    texto_login.desenho()
    campo_login.desenho()
    texto_campo_login.desenho()

    texto_senha.desenho()
    campo_senha.desenho()
    texto_campo_senha.desenho()
    
    botao_entrar.desenho()
    texto_entrar.desenho()
    
    botao_sair.desenho()
    texto_sair.desenho()
    
    botao_extras.desenho()

def desenho_pagina_aviso():
    janela_aviso.desenho()
    texto_aviso.desenho()

    texto_do_aviso_1.desenho()
    texto_do_aviso_2.desenho()

    botao_ok_aviso.desenho()
    texto_ok_aviso.desenho()

def escrever_login_senha(event):
    
    global texto_campo_login_escrevendo, texto_campo_login_entrada, texto_campo_senha_escrevendo, texto_campo_senha_entrada
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        if pygame.mouse.get_pos()[0] >= campo_login.porcentagem_pos_x:
            if pygame.mouse.get_pos()[1] >= campo_login.porcentagem_pos_y:
                if pygame.mouse.get_pos()[0] <= campo_login.porcentagem_pos_x + campo_login.largura_transformada:
                    if pygame.mouse.get_pos()[1] <= campo_login.porcentagem_pos_y + campo_login.altura_transformada:
                        texto_campo_login_escrevendo = True
                        if texto_campo_login_escrevendo == texto_campo_senha_escrevendo:
                            texto_campo_senha_escrevendo = False

        if pygame.mouse.get_pos()[0] >= campo_senha.porcentagem_pos_x:
            if pygame.mouse.get_pos()[1] >= campo_senha.porcentagem_pos_y:
                if pygame.mouse.get_pos()[0] <= campo_senha.porcentagem_pos_x + campo_senha.largura_transformada:
                    if pygame.mouse.get_pos()[1] <= campo_senha.porcentagem_pos_y + campo_senha.altura_transformada:
                        texto_campo_senha_escrevendo = True
                        if texto_campo_senha_escrevendo == texto_campo_login_escrevendo:
                            texto_campo_login_escrevendo = False
        else:
            texto_campo_login_escrevendo = False
            texto_campo_senha_escrevendo = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
            if texto_campo_login_escrevendo:
                texto_campo_login_escrevendo = False
            if texto_campo_senha_escrevendo:
                texto_campo_senha_escrevendo = False

        elif event.key == pygame.K_BACKSPACE:
            if texto_campo_login_escrevendo:
                texto_campo_login.frase = texto_campo_login.frase[:-1]
            if texto_campo_senha_escrevendo:
                texto_campo_senha_real.frase = texto_campo_senha_real.frase[:-1]
                print(texto_campo_senha_real.frase)
        
        elif event.key == pygame.K_TAB:
            if texto_campo_login_escrevendo:
                texto_campo_login_escrevendo = False
                texto_campo_senha_escrevendo = True
                print('foi 1')
            if texto_campo_senha_escrevendo:
                texto_campo_login_escrevendo = True
                texto_campo_senha_escrevendo = False
                print('foi 2')

        else:
            if texto_campo_login_escrevendo:
                texto_campo_login.frase += event.unicode
            if texto_campo_senha_escrevendo:
                texto_campo_senha_real.frase += event.unicode
                
    if len(texto_campo_senha.frase) > len(texto_campo_senha_real.frase):
        texto_campo_senha.frase = texto_campo_senha.frase [:-1]
    elif len(texto_campo_senha.frase) < len(texto_campo_senha_real.frase):
        texto_campo_senha.frase += '*'

def lendo_login():

    global texto_campo_login, texto_campo_senha_real

    comando = ('select login, senha from login where login = "'+texto_campo_login.frase+'" and senha = "'+texto_campo_senha_real.frase+'"')
    db_login.ler(comando)

    dados = db_login.resultado

    if len(dados) == 1:
        autenticador = True
    else:
        autenticador = False

    return autenticador

if __name__ == '__main__':
    from modulos.segmentacao import tela_largura, tela_altura, tela_resolucao, tela, game_rodando
    relogio_de_atualizacao = pygame.time.Clock()
    ponteiro = 30

    while game_rodando:

        musica_menu_inicio()

        while subsetor:

            # definindo evento de saida
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_rodando = False
                    subsetor = False
                
                escrever_login_senha(event)

                # interacao com o mouse
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] >= botao_entrar.porcentagem_pos_x:
                        if pygame.mouse.get_pos()[1] >= botao_entrar.porcentagem_pos_y:
                            if pygame.mouse.get_pos()[0] <= botao_entrar.porcentagem_pos_x + botao_entrar.largura_transformada:
                                if pygame.mouse.get_pos()[1] <= botao_entrar.porcentagem_pos_y + botao_entrar.altura_transformada:
                                    som_clique.play()

                    if pygame.mouse.get_pos()[0] >= botao_sair.porcentagem_pos_x:
                        if pygame.mouse.get_pos()[1] >= botao_sair.porcentagem_pos_y:
                            if pygame.mouse.get_pos()[0] <= botao_sair.porcentagem_pos_x + botao_sair.largura_transformada:
                                if pygame.mouse.get_pos()[1] <= botao_sair.porcentagem_pos_y + botao_sair.altura_transformada:
                                    som_clique.play()

            # desenhando elementos na tela
            desenho_pagina_inicial()

            # atualizacao da tela
            pygame.display.update()
            relogio_de_atualizacao.tick(ponteiro)

            tela_tamanho = pygame.display.get_window_size()