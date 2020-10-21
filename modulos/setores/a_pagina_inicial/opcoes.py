import pygame
import sys

sys.path.append('D:/Vini/Projetos/004 - RDC')

from modulos.segmentacao import *
from modulos.classes import *
from modulos.setores.a_pagina_inicial.inicio import *
from modulos.setores.a_pagina_inicial.opcoes import *

pygame.init()
pygame.mixer.init()

# variaveis:
janela_opcoes = JanelaOpcoes(7.4, 64)
texto_opcoes = Escrever(9.4, 64.9, 'titulo', 'Opcoes', 'preto')

caixa_confirmadora_bgm = CaixaConfirmadora(11.3, 68.6)
texto_bgm = Escrever(20, 68.6, 'corpo', 'BGM', 'preto')
barra_intensidade_seta_menor_bgm = BDISetas(32, 68.3, 'menor')
barra_intensidade_esteira_bgm = BDIEsteira(35.3, 68.6)
barra_intensidade_seta_maior_bgm = BDISetas(85.5, 68.3, 'maior')
esfera_marcadora_bgm = EsferaMarcadora(50, 68.7)

caixa_confirmadora_sfx = CaixaConfirmadora(11.3, 72.6)
texto_sfx = Escrever(20, 72.6, 'corpo', 'SFX', 'preto')
barra_intensidade_seta_menor_sfx = BDISetas(32, 72.2, 'menor')
barra_intensidade_esteira_sfx = BDIEsteira(35.3, 72.6)
barra_intensidade_seta_maior_sfx = BDISetas(85.5, 72.2, 'maior')
esfera_marcadora_sfx = EsferaMarcadora(50, 72.7)

caixa_confirmadora_efeitos = CaixaConfirmadora(11.3, 78.1)
texto_efeitos = Escrever(20, 78.1, 'corpo', 'Efeitos', 'preto')

botao_ok = Botao(80.5, 84.8, 'curto')
texto_ok = Escrever(83.4, 85.6, 'corpo', 'OK', 'preto')

# funcoes:
def desenho_pagina_opcoes():
    janela_opcoes.desenho()
    texto_opcoes.desenho()

    caixa_confirmadora_bgm.desenho()
    texto_bgm.desenho()
    barra_intensidade_seta_menor_bgm.desenho()
    barra_intensidade_esteira_bgm.desenho()
    barra_intensidade_seta_maior_bgm.desenho()
    esfera_marcadora_bgm.desenho()

    caixa_confirmadora_sfx.desenho()
    texto_sfx.desenho()
    barra_intensidade_seta_menor_sfx.desenho()
    barra_intensidade_esteira_sfx.desenho()
    barra_intensidade_seta_maior_sfx.desenho()
    esfera_marcadora_sfx.desenho()

    caixa_confirmadora_efeitos.desenho()
    texto_efeitos.desenho()

    botao_ok.desenho()
    texto_ok.desenho()

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

            # interacao com o mouse
            if pygame.mouse.get_pos()[0] >= caixa_confirmadora_bgm.porcentagem_pos_x:
                if pygame.mouse.get_pos()[1] >= caixa_confirmadora_bgm.porcentagem_pos_y:
                    if pygame.mouse.get_pos()[0] <= caixa_confirmadora_bgm.porcentagem_pos_x + caixa_confirmadora_bgm.largura_transformada:
                        if pygame.mouse.get_pos()[1] <= caixa_confirmadora_bgm.porcentagem_pos_y + caixa_confirmadora_bgm.altura_transformada:
                            if pygame.mouse.get_pressed()[0]:
                                caixa_confirmadora_bgm.mudanca_de_estado(1)
                                caixa_confirmadora_bgm.automatico()
            if pygame.mouse.get_pos()[0] >= barra_intensidade_seta_menor_bgm.porcentagem_pos_x:
                if pygame.mouse.get_pos()[1] >= barra_intensidade_seta_menor_bgm.porcentagem_pos_y:
                    if pygame.mouse.get_pos()[0] <= barra_intensidade_seta_menor_bgm.porcentagem_pos_x + barra_intensidade_seta_menor_bgm.largura_transformada:
                        if pygame.mouse.get_pos()[1] <= barra_intensidade_seta_menor_bgm.porcentagem_pos_y + barra_intensidade_seta_menor_bgm.altura_transformada:
                            if pygame.mouse.get_pressed()[0]:
                                if esfera_marcadora_bgm.porcentagem_pos_x >= barra_intensidade_esteira_bgm.porcentagem_pos_x + 10:
                                    esfera_marcadora_bgm.pos_x -= 0.5
                                    esfera_marcadora_bgm.automatico()
            if pygame.mouse.get_pos()[0] >= barra_intensidade_esteira_bgm.porcentagem_pos_x:
                if pygame.mouse.get_pos()[1] >= barra_intensidade_esteira_bgm.porcentagem_pos_y:
                    if pygame.mouse.get_pos()[0] <= barra_intensidade_esteira_bgm.porcentagem_pos_x + barra_intensidade_esteira_bgm.largura_transformada - barra_intensidade_seta_maior_bgm.largura_transformada:
                        if pygame.mouse.get_pos()[1] <= barra_intensidade_esteira_bgm.porcentagem_pos_y + barra_intensidade_esteira_bgm.altura_transformada:
                            if pygame.mouse.get_pressed()[0]:
                                lugar_mouse = capturar_posicao_mouse()
                                esfera_marcadora_bgm.pos_x = lugar_mouse[0]
                                esfera_marcadora_bgm.automatico()
            if pygame.mouse.get_pos()[0] >= barra_intensidade_seta_maior_bgm.porcentagem_pos_x:
                if pygame.mouse.get_pos()[1] >= barra_intensidade_seta_maior_bgm.porcentagem_pos_y:
                    if pygame.mouse.get_pos()[0] <= barra_intensidade_seta_maior_bgm.porcentagem_pos_x + barra_intensidade_seta_maior_bgm.largura_transformada:
                        if pygame.mouse.get_pos()[1] <= barra_intensidade_seta_maior_bgm.porcentagem_pos_y + barra_intensidade_seta_maior_bgm.altura_transformada:
                            if pygame.mouse.get_pressed()[0]:
                                if esfera_marcadora_bgm.porcentagem_pos_x <= barra_intensidade_esteira_bgm.porcentagem_pos_x + barra_intensidade_esteira_bgm.largura_transformada - barra_intensidade_seta_maior_bgm.largura_transformada:
                                    esfera_marcadora_bgm.pos_x += 0.5
                                    esfera_marcadora_bgm.automatico()

            if pygame.mouse.get_pos()[0] >= caixa_confirmadora_sfx.porcentagem_pos_x:
                if pygame.mouse.get_pos()[1] >= caixa_confirmadora_sfx.porcentagem_pos_y:
                    if pygame.mouse.get_pos()[0] <= caixa_confirmadora_sfx.porcentagem_pos_x + caixa_confirmadora_sfx.largura_transformada:
                        if pygame.mouse.get_pos()[1] <= caixa_confirmadora_sfx.porcentagem_pos_y + caixa_confirmadora_sfx.altura_transformada:
                            if pygame.mouse.get_pressed()[0]:
                                caixa_confirmadora_sfx.mudanca_de_estado(1)
                                caixa_confirmadora_sfx.automatico()
            if pygame.mouse.get_pos()[0] >= barra_intensidade_seta_menor_sfx.porcentagem_pos_x:
                if pygame.mouse.get_pos()[1] >= barra_intensidade_seta_menor_sfx.porcentagem_pos_y:
                    if pygame.mouse.get_pos()[0] <= barra_intensidade_seta_menor_sfx.porcentagem_pos_x + barra_intensidade_seta_menor_sfx.largura_transformada:
                        if pygame.mouse.get_pos()[1] <= barra_intensidade_seta_menor_sfx.porcentagem_pos_y + barra_intensidade_seta_menor_sfx.altura_transformada:
                            if pygame.mouse.get_pressed()[0]:
                                if esfera_marcadora_sfx.porcentagem_pos_x >= barra_intensidade_esteira_sfx.porcentagem_pos_x:
                                    esfera_marcadora_sfx.pos_x -= 0.5
                                    esfera_marcadora_sfx.automatico()
            if pygame.mouse.get_pos()[0] >= barra_intensidade_esteira_sfx.porcentagem_pos_x:
                if pygame.mouse.get_pos()[1] >= barra_intensidade_esteira_sfx.porcentagem_pos_y:
                    if pygame.mouse.get_pos()[0] <= barra_intensidade_esteira_sfx.porcentagem_pos_x + barra_intensidade_esteira_sfx.largura_transformada - barra_intensidade_seta_maior_sfx.largura_transformada:
                        if pygame.mouse.get_pos()[1] <= barra_intensidade_esteira_sfx.porcentagem_pos_y + barra_intensidade_esteira_sfx.altura_transformada:
                            if pygame.mouse.get_pressed()[0]:
                                lugar_mouse = capturar_posicao_mouse()
                                esfera_marcadora_sfx.pos_x = lugar_mouse[0]
                                esfera_marcadora_sfx.automatico()
            if pygame.mouse.get_pos()[0] >= barra_intensidade_seta_maior_sfx.porcentagem_pos_x:
                if pygame.mouse.get_pos()[1] >= barra_intensidade_seta_maior_sfx.porcentagem_pos_y:
                    if pygame.mouse.get_pos()[0] <= barra_intensidade_seta_maior_sfx.porcentagem_pos_x + barra_intensidade_seta_maior_sfx.largura_transformada:
                        if pygame.mouse.get_pos()[1] <= barra_intensidade_seta_maior_sfx.porcentagem_pos_y + barra_intensidade_seta_maior_sfx.altura_transformada:
                            if pygame.mouse.get_pressed()[0]:
                                if esfera_marcadora_sfx.porcentagem_pos_x <= barra_intensidade_esteira_sfx.porcentagem_pos_x + barra_intensidade_esteira_sfx.largura_transformada - barra_intensidade_seta_maior_sfx.largura_transformada:
                                    esfera_marcadora_sfx.pos_x += 0.5
                                    esfera_marcadora_sfx.automatico()

            if pygame.mouse.get_pos()[0] >= caixa_confirmadora_efeitos.porcentagem_pos_x:
                if pygame.mouse.get_pos()[1] >= caixa_confirmadora_efeitos.porcentagem_pos_y:
                    if pygame.mouse.get_pos()[0] <= caixa_confirmadora_efeitos.porcentagem_pos_x + caixa_confirmadora_efeitos.largura_transformada:
                        if pygame.mouse.get_pos()[1] <= caixa_confirmadora_efeitos.porcentagem_pos_y + caixa_confirmadora_efeitos.altura_transformada:
                            if pygame.mouse.get_pressed()[0]:
                                caixa_confirmadora_efeitos.mudanca_de_estado(1)
                                caixa_confirmadora_efeitos.automatico()

            if pygame.mouse.get_pos()[0] >= botao_ok.porcentagem_pos_x:
                if pygame.mouse.get_pos()[1] >= botao_ok.porcentagem_pos_y:
                    if pygame.mouse.get_pos()[0] <= botao_ok.porcentagem_pos_x + botao_ok.largura_transformada:
                        if pygame.mouse.get_pos()[1] <= botao_ok.porcentagem_pos_y + botao_ok.altura_transformada:
                            if pygame.mouse.get_pressed()[0]:
                                som_clique.play()

            # desenhando elementos na tela
            desenho_pagina_inicial()
            desenho_pagina_opcoes()

            # atualizacao da tela
            pygame.display.update()
            relogio_de_atualizacao.tick(ponteiro)