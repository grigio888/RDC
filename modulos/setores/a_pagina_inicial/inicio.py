import pygame
import sys

sys.path.append('D:/Vini/Projetos/004 - RDC')

from modulos.segmentacao import *
from modulos.classes import *
from modulos.setores.a_pagina_inicial.inicio import *

pygame.init()
pygame.mixer.init()

# variaveis:
fundo = Fundo(0, 0)
logo = Logo(7, 13)

janela_inicio = JanelaInicio(5, 64.7)
texto_inicio = Escrever(7, 65.6, 'titulo', 'Inicio', 'preto')

botao_entrar = Botao(30.1, 69.3, 'largo')
texto_entrar = Escrever(50, 70.8, 'botao', 'Entrar', 'preto', 'centro')

botao_sair = Botao(30.1, 74, 'largo')
texto_sair = Escrever(50, 75.5, 'botao', 'Sair', 'preto', 'centro')

botao_opcoes = Botao(86.7, 79.8, 'opcoes')

som_clique = pygame.mixer.Sound('modulos/som/sfx/mouse/click.ogg')

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
    botao_entrar.desenho()
    texto_entrar.desenho()
    botao_sair.desenho()
    texto_sair.desenho()
    botao_opcoes.desenho()


if __name__ == '__main__':
    from modulos.segmentacao import tela_largura, tela_altura, tela_resolucao, tela, game_rodando
    relogio_de_atualizacao = pygame.time.Clock()
    ponteiro = 30

    while game_rodando:

        musica_menu_inicio()

        while subsetor:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_rodando = False
                    subsetor = False

            if pygame.mouse.get_pos()[0] >= botao_entrar.porcentagem_pos_x:
                if pygame.mouse.get_pos()[1] >= botao_entrar.porcentagem_pos_y:
                    if pygame.mouse.get_pos()[0] <= botao_entrar.porcentagem_pos_x + botao_entrar.largura_transformada:
                        if pygame.mouse.get_pos()[1] <= botao_entrar.porcentagem_pos_y + botao_entrar.altura_transformada:
                            if pygame.mouse.get_pressed()[0]:
                                som_clique.play()

            if pygame.mouse.get_pos()[0] >= botao_sair.porcentagem_pos_x:
                if pygame.mouse.get_pos()[1] >= botao_sair.porcentagem_pos_y:
                    if pygame.mouse.get_pos()[0] <= botao_sair.porcentagem_pos_x + botao_sair.largura_transformada:
                        if pygame.mouse.get_pos()[1] <= botao_sair.porcentagem_pos_y + botao_sair.altura_transformada:
                            if pygame.mouse.get_pressed()[0]:
                                som_clique.play()

            if pygame.mouse.get_pos()[0] >= botao_opcoes.porcentagem_pos_x:
                if pygame.mouse.get_pos()[1] >= botao_opcoes.porcentagem_pos_y:
                    if pygame.mouse.get_pos()[0] <= botao_opcoes.porcentagem_pos_x + botao_opcoes.largura_transformada:
                        if pygame.mouse.get_pos()[1] <= botao_opcoes.porcentagem_pos_y + botao_opcoes.altura_transformada:
                            if pygame.mouse.get_pressed()[0]:
                                som_clique.play()

            # desenhando elementos na tela
            desenho_pagina_inicial()

            # atualizacao da tela
            pygame.display.update()
            relogio_de_atualizacao.tick(ponteiro)
