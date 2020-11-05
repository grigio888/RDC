import pygame, sys
from modulos.segmentacao import *
from modulos.setores.a_pagina_inicial.opcoes import *

sys.path.append(caminho_raiz_pc)

pygame.init()

# variaveis:

fundo_inicio = ExibirImagem('modulos/setores/b_inicio/landing_page/fundo.png', 1080, 2020, 0, 0)

# Conta
janela_conta = ExibirImagem('modulos/setores/b_inicio/landing_page/janela_cima.png', 972, 333, 5, 1.5)
texto_conta = Escrever(7, 2.2, 'titulo', 'Conta', 'preto')

nome_da_conta = Escrever(8.3, 5.7, 'corpo', 'Nome_Da_Conta', 'preto')

num_de_personagens_0 = Escrever(10.1, 9.3, 'corpo', 'No. de Personagens:', 'preto')
num_de_personagens_1 = Escrever(90, 9.3, 'corpo', '0 / 4 pngs', 'preto', 'direita')

score_0 = Escrever(10.1, 12, 'corpo', 'Score Maximo:', 'preto')
score_1 = Escrever(90, 12, 'corpo', '000000000 pts.', 'preto', 'direita')

dinheiro_0 = Escrever(50, 15.5, 'titulo', 'Zenys:', 'preto')
dinheiro_1 = Escrever(93, 15.5, 'titulo', '000000000 z', 'preto', 'direita')

#Personagens
janela_personagem = ExibirImagem('modulos/setores/b_inicio/landing_page/janela_meio.png', 972, 1244, 5, 19)
texto_personagem = Escrever(7, 20, 'titulo', 'Personagem', 'preto')

personagem_0_frame = ExibirImagem('modulos/setores/b_inicio/landing_page/frame_personagem.png', 404, 517, 10.6, 23.7)
personagem_0 = None
personagem_0_adicionar = ExibirImagem('modulos/setores/b_inicio/landing_page/adicionar.png', 60, 60, 26.6, 35)
personagem_0_sombra = ExibirImagem('modulos/setores/b_inicio/landing_page/frame_sombra.png', 165, 94, 21.8, 43.3)
personagem_0_nome = Escrever(29.4, 50.1, 'item', 'Nome_Char', 'preto', 'centro')

personagem_1_frame = ExibirImagem('modulos/setores/b_inicio/landing_page/frame_personagem.png', 404, 517, 51.7, 23.7)
personagem_1 = None
personagem_1_adicionar = ExibirImagem('modulos/setores/b_inicio/landing_page/adicionar.png', 60, 60, 67.7, 35)
personagem_1_sombra = ExibirImagem('modulos/setores/b_inicio/landing_page/frame_sombra.png', 165, 94, 62.8, 43.3)
personagem_1_nome = Escrever(70.5, 50.1, 'item', 'Nome_Char', 'preto', 'centro')

personagem_2_frame = ExibirImagem('modulos/setores/b_inicio/landing_page/frame_personagem.png', 404, 517, 10.6, 52)
personagem_2 = None
personagem_2_adicionar = ExibirImagem('modulos/setores/b_inicio/landing_page/adicionar.png', 60, 60, 26.6, 63.4)
personagem_2_sombra = ExibirImagem('modulos/setores/b_inicio/landing_page/frame_sombra.png', 165, 94, 21.8, 71.6)
personagem_2_nome = Escrever(29.4, 78.4, 'item', 'Nome_Char', 'preto', 'centro')

personagem_3_frame = ExibirImagem('modulos/setores/b_inicio/landing_page/frame_personagem.png', 404, 517, 51.7, 52)
personagem_3 = None
personagem_3_adicionar = ExibirImagem('modulos/setores/b_inicio/landing_page/adicionar.png', 60, 60, 67.7, 63.4)
personagem_3_sombra = ExibirImagem('modulos/setores/b_inicio/landing_page/frame_sombra.png', 165, 94, 62.8, 71.6)
personagem_3_nome = Escrever(70.5, 78.4, 'item', 'Nome_Char', 'preto', 'centro')

#Diversos
janela_diversos = ExibirImagem('modulos/setores/b_inicio/landing_page/janela_baixo.png', 972, 333, 5, 81.5)
texto_diversos = Escrever(7, 82.4, 'titulo', 'Diversos', 'preto')

frame_mochila = ExibirImagem('modulos/setores/b_inicio/landing_page/frame_item.png', 210, 240, 8.5, 85.2)
opcao_mochila = ExibirItem(11.3, 85, 2641, 1, 2.2)
texto_mochila = Escrever(17.75, 95.5, 'item', 'Mochila', 'preto', 'centro')

frame_chave = ExibirImagem('modulos/setores/b_inicio/landing_page/frame_item.png', 210, 240, 30, 85.2)
opcao_chave = ExibirItem(34.4, 86, 7026, 1, 1.9)
texto_chave = Escrever(39.5, 95.5, 'item', 'Chave', 'preto', 'centro')

frame_forja = ExibirImagem('modulos/setores/b_inicio/landing_page/frame_item.png', 210, 240, 51.6, 85.2)
opcao_forja = ExibirItem(52.5, 84.5, 7811, 1, 2.4)
texto_forja = Escrever(60.85, 95.5, 'item', 'Forja', 'preto', 'centro')

frame_opcoes = ExibirImagem('modulos/setores/b_inicio/landing_page/frame_item.png', 210, 240, 73.1, 85.2)
opcao_opcoes = ExibirItem(75.5, 85, 7703, 1, 2.1)
texto_opcoes = Escrever(82.35, 95.5, 'item', 'Opcoes', 'preto', 'centro')

def interacao_landingpage_mouse_colisao():
    if pygame.mouse.get_pos()[0] >= personagem_0_frame.porcentagem_pos_x:
        if pygame.mouse.get_pos()[1] >= personagem_0_frame.porcentagem_pos_y:
            if pygame.mouse.get_pos()[0] <= personagem_0_frame.porcentagem_pos_x + personagem_0_frame.largura_transformada:
                if pygame.mouse.get_pos()[1] <= personagem_0_frame.porcentagem_pos_y + personagem_0_frame.altura_transformada:
                    personagem_0_adicionar.desenho()
    if pygame.mouse.get_pos()[0] >= personagem_1_frame.porcentagem_pos_x:
        if pygame.mouse.get_pos()[1] >= personagem_1_frame.porcentagem_pos_y:
            if pygame.mouse.get_pos()[0] <= personagem_1_frame.porcentagem_pos_x + personagem_1_frame.largura_transformada:
                if pygame.mouse.get_pos()[1] <= personagem_1_frame.porcentagem_pos_y + personagem_1_frame.altura_transformada:
                    personagem_1_adicionar.desenho()
    if pygame.mouse.get_pos()[0] >= personagem_2_frame.porcentagem_pos_x:
        if pygame.mouse.get_pos()[1] >= personagem_2_frame.porcentagem_pos_y:
            if pygame.mouse.get_pos()[0] <= personagem_2_frame.porcentagem_pos_x + personagem_2_frame.largura_transformada:
                if pygame.mouse.get_pos()[1] <= personagem_2_frame.porcentagem_pos_y + personagem_2_frame.altura_transformada:
                    personagem_2_adicionar.desenho()
    if pygame.mouse.get_pos()[0] >= personagem_3_frame.porcentagem_pos_x:
        if pygame.mouse.get_pos()[1] >= personagem_3_frame.porcentagem_pos_y:
            if pygame.mouse.get_pos()[0] <= personagem_3_frame.porcentagem_pos_x + personagem_3_frame.largura_transformada:
                if pygame.mouse.get_pos()[1] <= personagem_3_frame.porcentagem_pos_y + personagem_3_frame.altura_transformada:
                    personagem_3_adicionar.desenho()

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

    frame_chave.desenho()
    opcao_chave.desenho()
    texto_chave.desenho()

    frame_forja.desenho()
    opcao_forja.desenho()
    texto_forja.desenho()

    frame_opcoes.desenho()
    opcao_opcoes.desenho()
    texto_opcoes.desenho()


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