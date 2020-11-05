import pygame, sys
from modulos.classes import *
from modulos.segmentacao import som_clique

sys.path.append(caminho_raiz_pc)

# variaveis:
janela_opcoes = ExibirImagem('modulos/setores/a_pagina_inicial/opcoes_ext/janela_opcoes.png', 920, 539, 7.4, 66.6)
texto_opcoes = Escrever(9.4, 67.6, 'titulo', 'Opcoes', 'preto')

caixa_confirmadora_bgm = ExibirImagemInterativa('modulos/setores/a_pagina_inicial/opcoes_ext/caixa_marcada.png', 'modulos/setores/a_pagina_inicial/opcoes_ext/caixa_nao_marcada.png', 35, 35, 11.3, 71.6)
texto_bgm = Escrever(20, 71.6, 'corpo', 'BGM', 'preto')
barra_intensidade_seta_menor_bgm = ExibirImagem('modulos/setores/a_pagina_inicial/opcoes_ext/barra_intensidade_menor.png', 35, 46, 32.1, 71.2)
barra_intensidade_esteira_bgm = ExibirImagem('modulos/setores/a_pagina_inicial/opcoes_ext/barra_intensidade_esteira.png', 542, 32, 35.3, 71.6)
barra_intensidade_seta_maior_bgm = ExibirImagem('modulos/setores/a_pagina_inicial/opcoes_ext/barra_intensidade_maior.png', 35, 46, 85.5, 71.2)
esfera_marcadora_bgm = ExibirImagem('modulos/setores/a_pagina_inicial/opcoes_ext/esfera_marcadora.png', 27, 32, 50, 71.6)

caixa_confirmadora_sfx = ExibirImagemInterativa('modulos/setores/a_pagina_inicial/opcoes_ext/caixa_marcada.png', 'modulos/setores/a_pagina_inicial/opcoes_ext/caixa_nao_marcada.png', 35, 35, 11.3, 75.9)
texto_sfx = Escrever(20, 75.9, 'corpo', 'SFX', 'preto')
barra_intensidade_seta_menor_sfx = ExibirImagem('modulos/setores/a_pagina_inicial/opcoes_ext/barra_intensidade_menor.png', 35, 46, 32.1, 75.5)
barra_intensidade_esteira_sfx = ExibirImagem('modulos/setores/a_pagina_inicial/opcoes_ext/barra_intensidade_esteira.png', 542, 32, 35.3, 75.9)
barra_intensidade_seta_maior_sfx = ExibirImagem('modulos/setores/a_pagina_inicial/opcoes_ext/barra_intensidade_maior.png', 35, 46, 85.5, 75.5)
esfera_marcadora_sfx = ExibirImagem('modulos/setores/a_pagina_inicial/opcoes_ext/esfera_marcadora.png', 27, 32, 50, 75.9)


caixa_confirmadora_efeitos = ExibirImagemInterativa('modulos/setores/a_pagina_inicial/opcoes_ext/caixa_marcada.png', 'modulos/setores/a_pagina_inicial/opcoes_ext/caixa_nao_marcada.png', 35, 35, 11.3, 81.8)
texto_efeitos = Escrever(20, 81.8, 'corpo', 'Efeitos', 'preto')

botao_ok = ExibirImagem('modulos/setores/a_pagina_inicial/opcoes_ext/botao_curto.png', 106, 69, 80.5, 88.6)
texto_ok = Escrever(83.4, 89.5, 'corpo', 'OK', 'preto')

# funcoes:
def interacao_mouse_opcoes_pMOUSEBUTTON():
    if pygame.mouse.get_pos()[0] >= caixa_confirmadora_bgm.porcentagem_pos_x:
        if pygame.mouse.get_pos()[1] >= caixa_confirmadora_bgm.porcentagem_pos_y:
            if pygame.mouse.get_pos()[0] <= caixa_confirmadora_bgm.porcentagem_pos_x + caixa_confirmadora_bgm.largura_transformada:
                if pygame.mouse.get_pos()[1] <= caixa_confirmadora_bgm.porcentagem_pos_y + caixa_confirmadora_bgm.altura_transformada:
                    caixa_confirmadora_bgm.mudanca_de_estado(1)
                    caixa_confirmadora_bgm.automatico()
    if pygame.mouse.get_pos()[0] >= caixa_confirmadora_sfx.porcentagem_pos_x:
        if pygame.mouse.get_pos()[1] >= caixa_confirmadora_sfx.porcentagem_pos_y:
            if pygame.mouse.get_pos()[0] <= caixa_confirmadora_sfx.porcentagem_pos_x + caixa_confirmadora_sfx.largura_transformada:
                if pygame.mouse.get_pos()[1] <= caixa_confirmadora_sfx.porcentagem_pos_y + caixa_confirmadora_sfx.altura_transformada:
                    caixa_confirmadora_sfx.mudanca_de_estado(1)
                    caixa_confirmadora_sfx.automatico()
    if pygame.mouse.get_pos()[0] >= caixa_confirmadora_efeitos.porcentagem_pos_x:
        if pygame.mouse.get_pos()[1] >= caixa_confirmadora_efeitos.porcentagem_pos_y:
            if pygame.mouse.get_pos()[0] <= caixa_confirmadora_efeitos.porcentagem_pos_x + caixa_confirmadora_efeitos.largura_transformada:
                if pygame.mouse.get_pos()[1] <= caixa_confirmadora_efeitos.porcentagem_pos_y + caixa_confirmadora_efeitos.altura_transformada:
                    caixa_confirmadora_efeitos.mudanca_de_estado(1)
                    caixa_confirmadora_efeitos.automatico()
    if pygame.mouse.get_pos()[0] >= botao_ok.porcentagem_pos_x:
        if pygame.mouse.get_pos()[1] >= botao_ok.porcentagem_pos_y:
            if pygame.mouse.get_pos()[0] <= botao_ok.porcentagem_pos_x + botao_ok.largura_transformada:
                if pygame.mouse.get_pos()[1] <= botao_ok.porcentagem_pos_y + botao_ok.altura_transformada:
                    som_clique.play()
                    return 'caiu'
    return 'opcoes'

def interacao_mouse_opcoes_pGETPRESSED():
    if pygame.mouse.get_pos()[0] >= barra_intensidade_seta_menor_bgm.porcentagem_pos_x:
        if pygame.mouse.get_pos()[1] >= barra_intensidade_seta_menor_bgm.porcentagem_pos_y:
            if pygame.mouse.get_pos()[0] <= barra_intensidade_seta_menor_bgm.porcentagem_pos_x + barra_intensidade_seta_menor_bgm.largura_transformada:
                if pygame.mouse.get_pos()[1] <= barra_intensidade_seta_menor_bgm.porcentagem_pos_y + barra_intensidade_seta_menor_bgm.altura_transformada:
                    if esfera_marcadora_bgm.porcentagem_pos_x >= barra_intensidade_esteira_bgm.porcentagem_pos_x + 10:
                        esfera_marcadora_bgm.pos_x -= 0.5
                        esfera_marcadora_bgm.automatico()
    if pygame.mouse.get_pos()[0] >= barra_intensidade_esteira_bgm.porcentagem_pos_x:
        if pygame.mouse.get_pos()[1] >= barra_intensidade_esteira_bgm.porcentagem_pos_y:
            if pygame.mouse.get_pos()[0] <= barra_intensidade_esteira_bgm.porcentagem_pos_x + barra_intensidade_esteira_bgm.largura_transformada - barra_intensidade_seta_maior_bgm.largura_transformada:
                if pygame.mouse.get_pos()[1] <= barra_intensidade_esteira_bgm.porcentagem_pos_y + barra_intensidade_esteira_bgm.altura_transformada:
                    lugar_mouse = capturar_posicao_mouse()
                    esfera_marcadora_bgm.pos_x = lugar_mouse[0]
                    esfera_marcadora_bgm.automatico()
    if pygame.mouse.get_pos()[0] >= barra_intensidade_seta_maior_bgm.porcentagem_pos_x:
        if pygame.mouse.get_pos()[1] >= barra_intensidade_seta_maior_bgm.porcentagem_pos_y:
            if pygame.mouse.get_pos()[0] <= barra_intensidade_seta_maior_bgm.porcentagem_pos_x + barra_intensidade_seta_maior_bgm.largura_transformada:
                if pygame.mouse.get_pos()[1] <= barra_intensidade_seta_maior_bgm.porcentagem_pos_y + barra_intensidade_seta_maior_bgm.altura_transformada:
                    if esfera_marcadora_bgm.porcentagem_pos_x <= barra_intensidade_esteira_bgm.porcentagem_pos_x + barra_intensidade_esteira_bgm.largura_transformada - barra_intensidade_seta_maior_bgm.largura_transformada:
                        esfera_marcadora_bgm.pos_x += 0.5
                        esfera_marcadora_bgm.automatico()


    if pygame.mouse.get_pos()[0] >= barra_intensidade_seta_menor_sfx.porcentagem_pos_x:
        if pygame.mouse.get_pos()[1] >= barra_intensidade_seta_menor_sfx.porcentagem_pos_y:
            if pygame.mouse.get_pos()[0] <= barra_intensidade_seta_menor_sfx.porcentagem_pos_x + barra_intensidade_seta_menor_sfx.largura_transformada:
                if pygame.mouse.get_pos()[1] <= barra_intensidade_seta_menor_sfx.porcentagem_pos_y + barra_intensidade_seta_menor_sfx.altura_transformada:
                    if esfera_marcadora_sfx.porcentagem_pos_x >= barra_intensidade_esteira_sfx.porcentagem_pos_x:
                        esfera_marcadora_sfx.pos_x -= 0.5
                        esfera_marcadora_sfx.automatico()
    if pygame.mouse.get_pos()[0] >= barra_intensidade_esteira_sfx.porcentagem_pos_x:
        if pygame.mouse.get_pos()[1] >= barra_intensidade_esteira_sfx.porcentagem_pos_y:
            if pygame.mouse.get_pos()[0] <= barra_intensidade_esteira_sfx.porcentagem_pos_x + barra_intensidade_esteira_sfx.largura_transformada - barra_intensidade_seta_maior_sfx.largura_transformada:
                if pygame.mouse.get_pos()[1] <= barra_intensidade_esteira_sfx.porcentagem_pos_y + barra_intensidade_esteira_sfx.altura_transformada:
                    lugar_mouse = capturar_posicao_mouse()
                    esfera_marcadora_sfx.pos_x = lugar_mouse[0]
                    esfera_marcadora_sfx.automatico()
    if pygame.mouse.get_pos()[0] >= barra_intensidade_seta_maior_sfx.porcentagem_pos_x:
        if pygame.mouse.get_pos()[1] >= barra_intensidade_seta_maior_sfx.porcentagem_pos_y:
            if pygame.mouse.get_pos()[0] <= barra_intensidade_seta_maior_sfx.porcentagem_pos_x + barra_intensidade_seta_maior_sfx.largura_transformada:
                if pygame.mouse.get_pos()[1] <= barra_intensidade_seta_maior_sfx.porcentagem_pos_y + barra_intensidade_seta_maior_sfx.altura_transformada:
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

if __name__ == '__main__':
    pass