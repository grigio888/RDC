import pygame
import sys

sys.path.append('D:/Vini/Projetos/004 - RDC')

from modulos.segmentacao import *
from modulos.classes import *

pygame.init()

# variaveis:
fundo = FundoInicio(0, 0)


janela_conta = JanelaLanding(5, 3.2, 'cima')
texto_conta = Escrever(7, 3.9, 'titulo', 'Conta', 'preto')

nome_da_conta = Escrever(8.3, 7.1, 'corpo', 'Nome_Da_Conta', 'preto')

num_de_personagens_0 = Escrever(10.1, 10.5, 'corpo', 'No. de Personagens:', 'preto')
num_de_personagens_1 = Escrever(90, 10.5, 'corpo', '0 / 4 pngs', 'preto', 'direita')

score_0 = Escrever(10.1, 13, 'corpo', 'Score Maximo:', 'preto')
score_1 = Escrever(90, 13, 'corpo', '000000000 pts.', 'preto', 'direita')

dinheiro_0 = Escrever(50, 16.3, 'titulo', 'Zenys:', 'preto')
dinheiro_1 = Escrever(93, 16.3, 'titulo', '000000000 z', 'preto', 'direita')



janela_personagem = JanelaLanding(5, 21, 'meio')
texto_personagem = Escrever(7, 21.8, 'titulo', 'Personagem', 'preto')

personagem_0_frame = Frames(10.6, 25.4, 'frame')
#aqui entra o personagem#
personagem_0_sombra = Frames(21.8, 43.7, 'sombra')
personagem_0_nome = Escrever(29.4, 50, 'item', 'nome_char', 'preto', 'centro')

personagem_1_frame = Frames(51.7, 25.4, 'frame')
#aqui entra o personagem#
personagem_1_sombra = Frames(62.8, 43.7, 'sombra')
personagem_1_nome = Escrever(70.5, 50, 'item', 'nome_char', 'preto', 'centro')

personagem_2_frame = Frames(10.6, 51.9, 'frame')
#aqui entra o personagem#
personagem_2_sombra = Frames(21.8, 70.2, 'sombra')
personagem_2_nome = Escrever(29.4, 76.6, 'item', 'nome_char', 'preto', 'centro')

personagem_3_frame = Frames(51.7, 51.9, 'frame')
#aqui entra o personagem#
personagem_3_sombra = Frames(62.8, 70.2, 'sombra')
personagem_3_nome = Escrever(70.5, 76.6, 'item', 'nome_char', 'preto', 'centro')



janela_diversos = JanelaLanding(5, 82, 'baixo')
texto_diversos = Escrever(7, 82.9, 'titulo', 'Diversos', 'preto')
frame_mochila = Frames(9, 85.5, 'frame_item')
opcao_mochila = ImagemItem(11, 85, 2641, 1)
texto_mochila = Escrever(14, 94.7, 'item', 'Mochila', 'preto')

frame_2 = Frames(30, 85.5, 'frame_item')
opcao_2 = ImagemItem(34, 86, 7026, 1, 0.75)
texto_2 = Escrever(35, 94.7, 'item', 'Chave', 'preto')

frame_3 = Frames(51, 85.5, 'frame_item')
opcao_3 = ImagemItem(52.5, 86, 2641, 1)
texto_3 = Escrever(56, 94.7, 'item', 'Forja', 'preto')

frame_4 = Frames(72, 85.5, 'frame_item')
opcao_4 = ImagemItem(73.5, 86, 2641, 1)
texto_4 = Escrever(77, 94.7, 'item', 'Opcoes', 'preto')



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