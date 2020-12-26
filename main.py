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
                
                escrever_login_senha(event)

                # interacao com o mouse
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] >= botao_entrar.porcentagem_pos_x:
                        if pygame.mouse.get_pos()[1] >= botao_entrar.porcentagem_pos_y:
                            if pygame.mouse.get_pos()[0] <= botao_entrar.porcentagem_pos_x + botao_entrar.largura_transformada:
                                if pygame.mouse.get_pos()[1] <= botao_entrar.porcentagem_pos_y + botao_entrar.altura_transformada:
                                    autenticacao = lendo_login()
                                    if autenticacao:
                                        from modulos.setores.b_inicio.landing_page import *
                                        setor = 'landing'
                                        subsetor = 'caiu'
                                        som_clique.play()
                                    if not autenticacao:
                                        subsetor = 'autenticacao falha'
                                        som_clique.play()

                    if pygame.mouse.get_pos()[0] >= botao_sair.porcentagem_pos_x:
                        if pygame.mouse.get_pos()[1] >= botao_sair.porcentagem_pos_y:
                            if pygame.mouse.get_pos()[0] <= botao_sair.porcentagem_pos_x + botao_sair.largura_transformada:
                                if pygame.mouse.get_pos()[1] <= botao_sair.porcentagem_pos_y + botao_sair.altura_transformada:
                                    game_rodando = False
                                    setor = 'saida'
                                    subsetor = 'saida'
                                    som_clique.play()

                    if pygame.mouse.get_pos()[0] >= botao_extras.porcentagem_pos_x:
                        if pygame.mouse.get_pos()[1] >= botao_extras.porcentagem_pos_y:
                            if pygame.mouse.get_pos()[0] <= botao_extras.porcentagem_pos_x + botao_extras.largura_transformada:
                                if pygame.mouse.get_pos()[1] <= botao_extras.porcentagem_pos_y + botao_extras.altura_transformada:
                                    from modulos.setores.a_pagina_inicial.extras import *
                                    subsetor = 'extras'
                                    som_clique.play()

            # desenhando elementos na tela
            desenho_pagina_inicial()

            # atualizacao da tela
            pygame.display.update()
            relogio_de_atualizacao.tick(ponteiro)
            tela_tamanho = pygame.display.get_window_size()
    
        while subsetor == 'extras':

            # definindo evento de saida
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_rodando = False
                    setor = 'saida'
                    subsetor = 'saida'

                # interacao com o mouse
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] >= botao_criar_conta.porcentagem_pos_x:
                        if pygame.mouse.get_pos()[1] >= botao_criar_conta.porcentagem_pos_y:
                            if pygame.mouse.get_pos()[0] <= botao_criar_conta.porcentagem_pos_x + botao_criar_conta.largura_transformada:
                                if pygame.mouse.get_pos()[1] <= botao_criar_conta.porcentagem_pos_y + botao_criar_conta.altura_transformada:
                                    som_clique.play()
                                    entrando_criar_conta()
                                    subsetor = 'criar conta'

                    if pygame.mouse.get_pos()[0] >= botao_ok_extras.porcentagem_pos_x:
                        if pygame.mouse.get_pos()[1] >= botao_ok_extras.porcentagem_pos_y:
                            if pygame.mouse.get_pos()[0] <= botao_ok_extras.porcentagem_pos_x + botao_ok_extras.largura_transformada:
                                if pygame.mouse.get_pos()[1] <= botao_ok_extras.porcentagem_pos_y + botao_ok_extras.altura_transformada:
                                    som_clique.play()
                                    subsetor = 'caiu'

            # desenhando elementos na tela
            desenho_pagina_inicial()
            desenho_pagina_extras()

            # atualizacao da tela
            pygame.display.update()
            relogio_de_atualizacao.tick(ponteiro)
            tela_tamanho = pygame.display.get_window_size()

        while subsetor == 'criar conta':

            # definindo evento de saida
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_rodando = False
                    setor = 'saida'
                    subsetor = 'saida'

                escrever_login_email_senha_extras(event)

                # interacao com o mouse
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] >= botao_cancelar_extras.porcentagem_pos_x:
                        if pygame.mouse.get_pos()[1] >= botao_cancelar_extras.porcentagem_pos_y:
                            if pygame.mouse.get_pos()[0] <= botao_cancelar_extras.porcentagem_pos_x + botao_cancelar_extras.largura_transformada:
                                if pygame.mouse.get_pos()[1] <= botao_cancelar_extras.porcentagem_pos_y + botao_cancelar_extras.altura_transformada:
                                    som_clique.play()
                                    subsetor = 'extras'

                    if pygame.mouse.get_pos()[0] >= botao_confirmar_extras.porcentagem_pos_x:
                        if pygame.mouse.get_pos()[1] >= botao_confirmar_extras.porcentagem_pos_y:
                            if pygame.mouse.get_pos()[0] <= botao_confirmar_extras.porcentagem_pos_x + botao_confirmar_extras.largura_transformada:
                                if pygame.mouse.get_pos()[1] <= botao_confirmar_extras.porcentagem_pos_y + botao_confirmar_extras.altura_transformada:
                                    som_clique.play()
                                    subsetor = 'extras'

            # desenhando elementos na tela
            desenho_pagina_inicial()
            desenho_pagina_criar_conta()

            # atualizacao da tela
            pygame.display.update()
            relogio_de_atualizacao.tick(ponteiro)
            tela_tamanho = pygame.display.get_window_size()

        while subsetor == 'autenticacao falha':

            # definindo evento de saida
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_rodando = False
                    setor = 'saida'
                    subsetor = 'saida'
                
                escrever_login_senha(event)

                # interacao com o mouse
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pos()[0] >= botao_ok_aviso.porcentagem_pos_x:
                        if pygame.mouse.get_pos()[1] >= botao_ok_aviso.porcentagem_pos_y:
                            if pygame.mouse.get_pos()[0] <= botao_ok_aviso.porcentagem_pos_x + botao_ok_aviso.largura_transformada:
                                if pygame.mouse.get_pos()[1] <= botao_ok_aviso.porcentagem_pos_y + botao_ok_aviso.altura_transformada:
                                    subsetor = 'inicio'
                                    som_clique.play()

            # desenhando elementos na tela
            desenho_pagina_inicial()
            desenho_pagina_aviso()

            # atualizacao da tela
            pygame.display.update()
            relogio_de_atualizacao.tick(ponteiro)
            tela_tamanho = pygame.display.get_window_size()

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
            tela_tamanho = pygame.display.get_window_size()

        while subsetor == 'opcoes':

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    setor = 'landing'
                    subsetor = 'caiu'

                # interacao com o mouse
                interacao_opcoes_mouse_evento(event)
                interacao_opcoes_mouse_saida(event)
                if interacao_opcoes_mouse_saida(event) == 'caiu':
                    subsetor = 'caiu'

            interacao_opcoes_mouse()

            # desenhando elementos na tela
            desenho_landing_page()
            desenho_pagina_opcoes()

            # atualizacao da tela
            pygame.display.update()
            relogio_de_atualizacao.tick(ponteiro)
            tela_tamanho = pygame.display.get_window_size()
        
        while subsetor == 'criacao':

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    setor = 'landing'
                    subsetor = 'caiu'
                
                escrever_nome(event)
                aumento_de_atributo(event)

                # interacao com o mouse
                #interacao_criar_personagem_caixas_confirm(event)
                interacao_opcoes_mouse_saida(event)
                if interacao_opcoes_mouse_saida(event) == 'caiu':
                    setor = 'landing'
                    subsetor = 'caiu'
            
            # desenhando elementos na tela
            desenho_landing_page()
            desenho_landing_page_criar_personagem()
            
            desenho_aumento_de_atributo()
            calculos()

            # atualizacao da tela
            pygame.display.update()
            relogio_de_atualizacao.tick(ponteiro)
            tela_tamanho = pygame.display.get_window_size()
