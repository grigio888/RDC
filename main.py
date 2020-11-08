import pygame

pygame.init()
pygame.mixer.init()

from modulos.segmentacao import *

while game_rodando:

    musica_menu_inicio()

    while setor == 'pagina inicial':

        while subsetor == 'caiu':

            subsetor = 'inicio'

        while subsetor == 'inicio':

            # definindo evento de saida
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_rodando = False
                    setor = 'saida'
                    subsetor = 'saida'
                
                # interacao com o mouse
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] >= botao_entrar.porcentagem_pos_x:
                        if pygame.mouse.get_pos()[1] >= botao_entrar.porcentagem_pos_y:
                            if pygame.mouse.get_pos()[0] <= botao_entrar.porcentagem_pos_x + botao_entrar.largura_transformada:
                                if pygame.mouse.get_pos()[1] <= botao_entrar.porcentagem_pos_y + botao_entrar.altura_transformada:
                                    from modulos.setores.b_inicio.landing_page import *
                                    setor = 'landing'
                                    subsetor = 'caiu'
                                    som_clique.play()

                    if pygame.mouse.get_pos()[0] >= botao_sair.porcentagem_pos_x:
                        if pygame.mouse.get_pos()[1] >= botao_sair.porcentagem_pos_y:
                            if pygame.mouse.get_pos()[0] <= botao_sair.porcentagem_pos_x + botao_sair.largura_transformada:
                                if pygame.mouse.get_pos()[1] <= botao_sair.porcentagem_pos_y + botao_sair.altura_transformada:
                                    game_rodando = False
                                    setor = 'saida'
                                    subsetor = 'saida'
                                    som_clique.play()

                    if pygame.mouse.get_pos()[0] >= botao_opcoes.porcentagem_pos_x:
                        if pygame.mouse.get_pos()[1] >= botao_opcoes.porcentagem_pos_y:
                            if pygame.mouse.get_pos()[0] <= botao_opcoes.porcentagem_pos_x + botao_opcoes.largura_transformada:
                                if pygame.mouse.get_pos()[1] <= botao_opcoes.porcentagem_pos_y + botao_opcoes.altura_transformada:
                                    from modulos.setores.a_pagina_inicial.opcoes import *
                                    subsetor = 'opcoes'
                                    som_clique.play()

            # desenhando elementos na tela
            desenho_pagina_inicial()

            # atualizacao da tela
            pygame.display.update()
            relogio_de_atualizacao.tick(ponteiro)
    
        while subsetor == 'opcoes':
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_rodando = False
                    setor = 'saida'
                    subsetor = 'saida'

                # interacao com o mouse
                if event.type == pygame.MOUSEBUTTONDOWN:
                    interacao_opcoes_mouse_pMOUSEBUTTON()
                    subsetor = interacao_opcoes_mouse_pMOUSEBUTTON()              
                
            if pygame.mouse.get_pressed()[0]:
                interacao_opcoes_mouse_pGETPRESSED()

            # desenhando elementos na tela
            desenho_pagina_inicial()
            desenho_pagina_opcoes()

            # atualizacao da tela
            pygame.display.update()
            relogio_de_atualizacao.tick(ponteiro)

    while setor == 'landing':

        while subsetor == 'caiu':
            
            subsetor = 'inicio'

        while subsetor == 'inicio':

            # definindo evento de saida
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_rodando = False
                    setor = 'saida'
                    subsetor = 'saida'

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] >= frame_opcoes.porcentagem_pos_x:
                        if pygame.mouse.get_pos()[1] >= frame_opcoes.porcentagem_pos_y:
                            if pygame.mouse.get_pos()[0] <= frame_opcoes.porcentagem_pos_x + frame_opcoes.largura_transformada:
                                if pygame.mouse.get_pos()[1] <= frame_opcoes.porcentagem_pos_y + frame_opcoes.altura_transformada:
                                    subsetor = 'opcoes'
                                    som_clique.play()
                    if pygame.mouse.get_pos()[0] >= personagem_0_frame.porcentagem_pos_x:
                        if pygame.mouse.get_pos()[1] >= personagem_0_frame.porcentagem_pos_y:
                            if pygame.mouse.get_pos()[0] <= personagem_0_frame.porcentagem_pos_x + personagem_0_frame.largura_transformada:
                                if pygame.mouse.get_pos()[1] <= personagem_0_frame.porcentagem_pos_y + personagem_0_frame.altura_transformada:
                                    from modulos.setores.b_inicio.landing_page_criar_personagem import *
                                    subsetor = 'criacao'
                                    som_clique.play()

            # desenhando elementos na tela
            desenho_landing_page()


            interacao_landingpage_mouse_colisao()

            # atualizacao da tela
            pygame.display.update()
            relogio_de_atualizacao.tick(ponteiro)

        while subsetor == 'opcoes':

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    setor = 'landing'
                    subsetor = 'caiu'

                # interacao com o mouse
                if event.type == pygame.MOUSEBUTTONDOWN:
                    interacao_opcoes_mouse_pMOUSEBUTTON()
                    subsetor = interacao_opcoes_mouse_pMOUSEBUTTON()               
                
            if pygame.mouse.get_pressed()[0]:
                interacao_opcoes_mouse_pGETPRESSED()

            

            # desenhando elementos na tela
            desenho_landing_page()
            desenho_pagina_opcoes()

            # atualizacao da tela
            pygame.display.update()
            relogio_de_atualizacao.tick(ponteiro)
        
        while subsetor == 'criacao':

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    setor = 'landing'
                    subsetor = 'caiu'

                # interacao com o mouse
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] >= botao_ok_janela_personagem.porcentagem_pos_x:
                        if pygame.mouse.get_pos()[1] >= botao_ok_janela_personagem.porcentagem_pos_y:
                            if pygame.mouse.get_pos()[0] <= botao_ok_janela_personagem.porcentagem_pos_x + botao_ok_janela_personagem.largura_transformada:
                                if pygame.mouse.get_pos()[1] <= botao_ok_janela_personagem.porcentagem_pos_y + botao_ok_janela_personagem.altura_transformada:
                                    setor = 'landing'
                                    subsetor = 'caiu'
                                    som_clique.play()
            
            # desenhando elementos na tela
            desenho_landing_page()
            desenho_landing_page_criar_personagem()

            # atualizacao da tela
            pygame.display.update()
            relogio_de_atualizacao.tick(ponteiro)
