import pygame
import sys

sys.path.append('C:/Users/Pri e Vini/Desktop/Projetos/004 - RDC')

from modulos.segmentacao import *
from modulos.classes import *

pygame.init()

# variaveis:
fundo = FundoInicio(0, 0)


janela_conta = JanelaLanding(5, 3, 'cima')
texto_conta = Escrever(7, 3.9, 'titulo', 'Conta', 'preto')


nome_da_conta = Escrever(8.5, 7, 'corpo', 'Nome_Da_Conta', 'preto')
num_de_personagens_0 = Escrever(10.5, 10.5, 'corpo', 'No. de Personagens:', 'preto')
num_de_personagens_1 = Escrever(90, 10.5, 'corpo', '0 / 4 pngs', 'preto', 'direita')
score_0 = Escrever(10.5, 13, 'corpo', 'Score Maximo:', 'preto')
score_1 = Escrever(90, 13, 'corpo', '000000000 pts.', 'preto', 'direita')
dinheiro_0 = Escrever(50, 16.3, 'titulo', 'Zenys:', 'preto')
dinheiro_1 = Escrever(93, 16.3, 'titulo', '000000000 z', 'preto', 'direita')


janela_personagem = JanelaLanding(5, 21, 'meio')
texto_personagem = Escrever(7, 21.9, 'titulo', 'Personagem', 'preto')
personagem_0_frame = FramePersonagem(11.5, 25.5, 'frame')
#aqui entra o personagem#
personagem_0_sombra = FramePersonagem(22.5, 43.5, 'sombra')
personagem_1_frame = FramePersonagem(52.5, 25.5, 'frame')
#aqui entra o personagem#
personagem_1_sombra = FramePersonagem(63.5, 43.5, 'sombra')
personagem_2_frame = FramePersonagem(11.5, 50.5, 'frame')
#aqui entra o personagem#
personagem_2_sombra = FramePersonagem(22.5, 69.5, 'sombra')
personagem_3_frame = FramePersonagem(52.5, 50.5, 'frame')
#aqui entra o personagem#
personagem_3_sombra = FramePersonagem(63.5, 69.5, 'sombra')


janela_diversos = JanelaLanding(5, 82, 'baixo')
texto_diversos = Escrever(7, 82.9, 'titulo', 'Diversos', 'preto')

def desenho_landing_page():
    fundo.desenho()


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
    personagem_1_frame.desenho()
    #aqui entra o personagem#
    personagem_1_sombra.desenho()
    personagem_2_frame.desenho()
    #aqui entra o personagem#
    personagem_2_sombra.desenho()
    personagem_3_frame.desenho()
    #aqui entra o personagem#
    personagem_3_sombra.desenho()


    janela_diversos.desenho()
    texto_diversos.desenho()


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