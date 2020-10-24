import pygame
import sys

sys.path.append('D:/Vini/Projetos/004 - RDC')

from modulos.segmentacao import *
from modulos.classes import *

pygame.init()

# variaveis:

fundo_inicio = FundoInicio(0, 0)
from modulos.setores.c_inicio.landing_page_conta import *
from modulos.setores.c_inicio.landing_page_personagem import *
from modulos.setores.c_inicio.landing_page_diversos import *

def desenho_landing_page():
    fundo_inicio.desenho()



    janela_conta.desenho()
    texto_conta.desenho()



    nome_da_conta.desenho()
    num_de_personagens_0.desenho()
    num_de_personagens_1.desenho()
    score_0.desenho()
    score_1.desenho()
    dinheiro_0.desenho()
    dinheiro_1.desenho()



    janela_personagem.desenho()
    texto_personagem.desenho()

    personagem_0_frame.desenho()
    #aqui entra o personagem#
    personagem_0_sombra.desenho()
    personagem_0_nome.desenho()

    personagem_1_frame.desenho()
    #aqui entra o personagem#
    personagem_1_sombra.desenho()
    personagem_1_nome.desenho()

    personagem_2_frame.desenho()
    #aqui entra o personagem#
    personagem_2_sombra.desenho()
    personagem_2_nome.desenho()

    personagem_3_frame.desenho()
    #aqui entra o personagem#
    personagem_3_sombra.desenho()
    personagem_3_nome.desenho()



    janela_diversos.desenho()
    texto_diversos.desenho()

    frame_mochila.desenho()
    opcao_mochila.desenho()
    texto_mochila.desenho()

    frame_2.desenho()
    opcao_2.desenho()
    texto_2.desenho()

    frame_3.desenho()
    opcao_3.desenho()
    texto_3.desenho()

    frame_4.desenho()
    opcao_4.desenho()
    texto_4.desenho()


if __name__ == "__main__":
    from modulos.segmentacao import tela_largura, tela_altura, tela_resolucao, tela, game_rodando
    relogio_de_atualizacao = pygame.time.Clock()
    ponteiro = 30

    while game_rodando:
        # definindo evento de saida
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_rodando = False
                setor = 'saida'
                subsetor = 'saida'
        
        # interacao com o mouse
        #if pygame.mouse.get_pos()[0] >= botao_entrar.porcentagem_pos_x:
            #if pygame.mouse.get_pos()[1] >= botao_entrar.porcentagem_pos_y:
                #if pygame.mouse.get_pos()[0] <= botao_entrar.porcentagem_pos_x + botao_entrar.largura_transformada:
                    #if pygame.mouse.get_pos()[1] <= botao_entrar.porcentagem_pos_y + botao_entrar.altura_transformada:
                        #if pygame.mouse.get_pressed()[0]:
                            #game_rodando = True
                            #setor = 'loading'
                            #subsetor = 'saida'
                            #som_clique.play()

        # desenhando elementos na tela
        desenho_landing_page()

        # atualizacao da tela
        pygame.display.update()
        relogio_de_atualizacao.tick(ponteiro)