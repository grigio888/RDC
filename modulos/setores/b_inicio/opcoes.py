import pygame, sys
import sqlite3

sys.path.append('C:/Users/Grigio/Desktop/GitHub/RDC')

from modulos.classes import *
from modulos.segmentacao import *
from modulos.setores.a_pagina_inicial.inicio import texto_campo_login, db_login

# conectando ao banco de dados:
dados_do_banco_opcoes = db_login.ler(f'select * from opcoes where login_FK = "{texto_campo_login.frase}"')

# variaveis:
janela_opcoes = ExibirImagem('modulos/setores/b_inicio/opcoes_ext/janela_opcoes.png', 920, 539, 7.4, 66.6)
texto_opcoes = Escrever(janela_opcoes.pos_x + 2, janela_opcoes.pos_y + 0.9, 'titulo', 'Opcoes', 'preto')

caixa_confirmadora_bgm = ExibirImagemInterativa('modulos/setores/b_inicio/opcoes_ext/caixa_marcada.png', 'modulos/setores/b_inicio/opcoes_ext/caixa_nao_marcada.png', bool(dados_do_banco_opcoes[0][1]), 35, 35, 11.3, 71.6)#, )
texto_bgm = Escrever(20, 71.6, 'corpo', 'BGM', 'preto')
barra_intensidade_seta_menor_bgm = ExibirImagem('modulos/setores/b_inicio/opcoes_ext/barra_intensidade_menor.png', 35, 46, 32.1, 71.2)
barra_intensidade_esteira_bgm = ExibirImagem('modulos/setores/b_inicio/opcoes_ext/barra_intensidade_esteira.png', 542, 32, 35.3, 71.6)
barra_intensidade_seta_maior_bgm = ExibirImagem('modulos/setores/b_inicio/opcoes_ext/barra_intensidade_maior.png', 35, 46, 85.5, 71.2)
esfera_marcadora_bgm = ExibirImagem('modulos/setores/b_inicio/opcoes_ext/esfera_marcadora.png', 27, 32, 50, 71.6)
esfera_marcadora_bgm_volume = 20

caixa_confirmadora_sfx = ExibirImagemInterativa('modulos/setores/b_inicio/opcoes_ext/caixa_marcada.png', 'modulos/setores/b_inicio/opcoes_ext/caixa_nao_marcada.png', bool(dados_do_banco_opcoes[0][3]), 35, 35, 11.3, 75.9)#, dados_do_banco_opcoes[0][3])
texto_sfx = Escrever(20, 75.9, 'corpo', 'SFX', 'preto')
barra_intensidade_seta_menor_sfx = ExibirImagem('modulos/setores/b_inicio/opcoes_ext/barra_intensidade_menor.png', 35, 46, 32.1, 75.5)
barra_intensidade_esteira_sfx = ExibirImagem('modulos/setores/b_inicio/opcoes_ext/barra_intensidade_esteira.png', 542, 32, 35.3, 75.9)
barra_intensidade_seta_maior_sfx = ExibirImagem('modulos/setores/b_inicio/opcoes_ext/barra_intensidade_maior.png', 35, 46, 85.5, 75.5)
esfera_marcadora_sfx = ExibirImagem('modulos/setores/b_inicio/opcoes_ext/esfera_marcadora.png', 27, 32, 50, 75.9)
esfera_marcadora_sfx_volume = 20

caixa_confirmadora_efeitos = ExibirImagemInterativa('modulos/setores/b_inicio/opcoes_ext/caixa_marcada.png', 'modulos/setores/b_inicio/opcoes_ext/caixa_nao_marcada.png', bool(dados_do_banco_opcoes[0][5]), 35, 35, 11.3, 81.8)#, dados_do_banco_opcoes[0][5])
texto_efeitos = Escrever(20, 81.8, 'corpo', 'Efeitos', 'preto')

botao_ok = ExibirImagem('modulos/setores/b_inicio/opcoes_ext/botao_curto.png', 106, 69, 80.5, 88.6)
texto_ok = Escrever(83.4, 89.5, 'corpo', 'OK', 'preto')



janela_confirmacao = ExibirImagem('modulos/setores/b_inicio/opcoes_ext/janela_opcoes_confirmar.png', 605, 327, 22.1, 72)
texto_confirmacao = Escrever(24.1, 73, 'titulo', 'Confirmar', 'preto')

texto_corpo_confirmacao_1 = Escrever(50, 77, 'corpo', 'Deseja confirmar as', 'preto', 'centro')
texto_corpo_confirmacao_2 = Escrever(50, 79, 'corpo', 'alteracoes?', 'preto', 'centro')

botao_nao_confirmacao = ExibirImagem('modulos/setores/b_inicio/opcoes_ext/botao_curto.png', 106, 69, 35, 83.5)
texto_nao_confirmacao = Escrever(40, 84.4, 'corpo', 'Nao', 'preto', 'centro')

botao_ok_confirmacao = ExibirImagem('modulos/setores/b_inicio/opcoes_ext/botao_curto.png', 106, 69, 55, 83.5)
texto_ok_confirmacao = Escrever(60, 84.4, 'corpo', 'OK', 'preto', 'centro')

# funcoes:
def interacao_opcoes_mouse():
    if mouse_colidindo(barra_intensidade_seta_menor_bgm):
        if mouse_clicando():
            if esfera_marcadora_bgm.porcentagem_pos_x >= barra_intensidade_esteira_bgm.porcentagem_pos_x + 10:
                esfera_marcadora_bgm.pos_x -= 0.5
                esfera_marcadora_bgm.automatico()
    if mouse_colidindo(barra_intensidade_esteira_bgm):
        if mouse_clicando():
            esfera_marcadora_bgm.pos_x = pygame.mouse.get_pos()[0]
            esfera_marcadora_bgm.automatico()
    if mouse_colidindo(barra_intensidade_seta_maior_bgm):
        if mouse_clicando():
            if esfera_marcadora_bgm.porcentagem_pos_x <= barra_intensidade_esteira_bgm.porcentagem_pos_x + barra_intensidade_esteira_bgm.largura_transformada - barra_intensidade_seta_maior_bgm.largura_transformada:
                esfera_marcadora_bgm.pos_x += 0.5
                esfera_marcadora_bgm.automatico()


    if mouse_colidindo(barra_intensidade_seta_menor_sfx):
        if mouse_clicando():
            if esfera_marcadora_sfx.porcentagem_pos_x >= barra_intensidade_esteira_sfx.porcentagem_pos_x:
                esfera_marcadora_sfx.pos_x -= 0.5
                esfera_marcadora_sfx.automatico()
    if mouse_colidindo(barra_intensidade_esteira_sfx):
        if mouse_clicando():
            esfera_marcadora_sfx.pos_x = pygame.mouse.get_pos()[0]
            esfera_marcadora_sfx.automatico()
    if mouse_colidindo(barra_intensidade_seta_maior_sfx):
        if mouse_clicando():
            if esfera_marcadora_sfx.porcentagem_pos_x <= barra_intensidade_esteira_sfx.porcentagem_pos_x + barra_intensidade_esteira_sfx.largura_transformada - barra_intensidade_seta_maior_sfx.largura_transformada:
                esfera_marcadora_sfx.pos_x += 0.5
                esfera_marcadora_sfx.automatico()

def desenho_pagina_opcoes():
    janela_opcoes.desenho()
    texto_opcoes.desenho()

    caixa_confirmadora_bgm.desenho()
    texto_bgm.desenho()
    barra_intensidade_esteira_bgm.desenho()
    esfera_marcadora_bgm.desenho()
    barra_intensidade_seta_menor_bgm.desenho()
    barra_intensidade_seta_maior_bgm.desenho()

    caixa_confirmadora_sfx.desenho()
    texto_sfx.desenho()
    barra_intensidade_esteira_sfx.desenho()
    esfera_marcadora_sfx.desenho()
    barra_intensidade_seta_menor_sfx.desenho()
    barra_intensidade_seta_maior_sfx.desenho()

    caixa_confirmadora_efeitos.desenho()
    texto_efeitos.desenho()

    botao_ok.desenho()
    texto_ok.desenho()

def desenho_janela_confirmacao():
    janela_confirmacao.desenho()
    texto_confirmacao.desenho()

    texto_corpo_confirmacao_1.desenho()
    texto_corpo_confirmacao_2.desenho()

    botao_nao_confirmacao.desenho()
    texto_nao_confirmacao.desenho()

    botao_ok_confirmacao.desenho()
    texto_ok_confirmacao.desenho()

def gravando_alteracoes_db():
    comando = (f'update opcoes set bgm_cx = "{caixa_confirmadora_bgm.estado_int}", bgm_vol = "{esfera_marcadora_bgm_volume}", sfx_cx = "{caixa_confirmadora_sfx.estado_int}", sfx_vol = "{esfera_marcadora_sfx_volume}", fx_cx = "{caixa_confirmadora_efeitos.estado_int}" where login_FK = "{texto_campo_login.frase}"')
    db_login.executar(comando)

if __name__ == '__main__':

    pygame.init()
    pygame.mixer.init()

    rodando = True
    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                setor = 'landing'
                subsetor = 'caiu'

            # interacao com o mouse
            if mouse_colidindo(caixa_confirmadora_bgm):
                if mouse_clicando():
                    caixa_confirmadora_bgm.mudanca_de_estado()
                    caixa_confirmadora_bgm.automatico()
            if mouse_colidindo(caixa_confirmadora_sfx):
                if mouse_clicando():
                    caixa_confirmadora_sfx.mudanca_de_estado()
                    caixa_confirmadora_sfx.automatico()
            if mouse_colidindo(caixa_confirmadora_efeitos):
                if mouse_clicando():
                    caixa_confirmadora_efeitos.mudanca_de_estado()
                    caixa_confirmadora_efeitos.automatico()

            if mouse_colidindo(botao_ok):
                if mouse_clicando():
                    gravando_alteracoes_db()
                    subsetor = 'caiu'

            if mouse_colidindo(botao_nao_confirmacao):
                if mouse_clicando():
                    subsetor = 'caiu'
            if mouse_colidindo(botao_ok_confirmacao):
                if mouse_clicando():
                    gravando_alteracoes_db()
                    subsetor = 'caiu'

        interacao_opcoes_mouse()

        # desenhando elementos na tela
        desenho_landing_page()
        desenho_pagina_opcoes()
        mouse.desenho()

        # atualizacao da tela
        atualizacao_da_tela()