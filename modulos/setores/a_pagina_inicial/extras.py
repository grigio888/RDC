import pygame, sys
import mysql.connector as conectante

sys.path.append('D:/Vini/Projetos/004 - RDC')

from modulos.classes import *
from modulos.segmentacao import som_clique

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

botao_cancelar_extras = ExibirImagem('modulos/setores/a_pagina_inicial/extras_ext/botao_medio.png', 314, 69, janela_extras.pos_x + 15.5, janela_extras.pos_y + 22.3)
texto_cancelar_extras = Escrever(botao_cancelar_extras.pos_x + 14.3, botao_cancelar_extras.pos_y + 0.9, 'corpo', 'Cancelar', 'preto', 'centro')

botao_confirmar_extras = ExibirImagem('modulos/setores/a_pagina_inicial/extras_ext/botao_medio.png', 314, 69, janela_extras.pos_x + 48.5, janela_extras.pos_y + 22.3)
texto_confirmar_extras = Escrever(botao_confirmar_extras.pos_x + 14.3, botao_confirmar_extras.pos_y + 0.9, 'corpo', 'Confirma', 'preto', 'centro')

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
                texto_campo_email_extras.frase = texto_campo_login_extras.frase[:-1]
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

def interacao_confirmacao_mouse_saida(event):
        if pygame.mouse.get_pos()[0] >= botao_ok_extras.porcentagem_pos_x:
            if pygame.mouse.get_pos()[1] >= botao_ok_extras.porcentagem_pos_y:
                if pygame.mouse.get_pos()[0] <= botao_ok_extras.porcentagem_pos_x + botao_ok_extras.largura_transformada:
                    if pygame.mouse.get_pos()[1] <= botao_ok_extras.porcentagem_pos_y + botao_ok_extras.altura_transformada:
                        som_clique.play()
                        return 'caiu'

def gravando_alteracoes_mysql():
    login = conectante.connect(user='root',
                               password='kiju1475',
                               host='localhost',
                               database='rdc')

    cursor = login.cursor()
    comando = ('UPDATE opcoes SET bgm_caixa = %s, bgm_volume = %s, sfx_caixa = %s, sfx_volume = %s, efeitos_caixa = %s where login = %s and senha = %s')

    cursor.execute(comando, (caixa_confirmadora_bgm.estado, esfera_marcadora_bgm_volume, caixa_confirmadora_sfx.estado, esfera_marcadora_sfx_volume, caixa_confirmadora_efeitos.estado, texto_campo_login.frase, texto_campo_senha_real.frase))

    login.commit()
    login.close()

if __name__ == '__main__':

    pass