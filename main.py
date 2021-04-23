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
                    pygame.QUIT()
                
                escrever_login_senha(event)

                # interacao com o mouse
                
                if mouse_colidindo(botao_entrar):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        autenticacao = lendo_login()
                        if autenticacao:
                            from modulos.setores.b_inicio.landing_page import *
                            setor = 'landing'
                            subsetor = 'caiu'
                        if not autenticacao:
                            subsetor = 'autenticacao falha'

                elif mouse_colidindo(botao_sair):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pygame.QUIT()

                elif mouse_colidindo(botao_extras):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        from modulos.setores.a_pagina_inicial.extras import *
                        subsetor = 'extras'

            # desenhando elementos na tela
            desenho_pagina_inicial()
            mouse.desenho()

            # atualizacao da tela
            atualizacao_da_tela()
    
        while subsetor == 'autenticacao falha':

            # definindo evento de saida
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.QUIT()

                # interacao com o mouse
                if mouse_colidindo(botao_ok_aviso):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        subsetor = 'inicio'


            # desenhando elementos na tela
            desenho_pagina_inicial()
            desenho_pagina_aviso()
            mouse.desenho()

            # atualizacao da tela
            atualizacao_da_tela()

        while subsetor == 'extras':

            # definindo evento de saida
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.QUIT()

                # interacao com o mouse
                if mouse_colidindo(botao_criar_conta):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        entrando_criar_conta()
                        subsetor = 'criar conta'

                if mouse_colidindo(botao_ok_extras):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        subsetor = 'caiu'

            # desenhando elementos na tela
            desenho_pagina_inicial()
            desenho_pagina_extras()
            mouse.desenho()

            # atualizacao da tela
            atualizacao_da_tela()

        while subsetor == 'criar conta':

            # definindo evento de saida
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.QUIT()

                escrever_login_email_senha_extras(event)

                # interacao com o mouse
                if mouse_colidindo(botao_cancelar_extras):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        subsetor = 'extras'

                if mouse_colidindo(botao_confirmar_extras):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        verificador = verificando_duplicidade_cadastro()
                        subsetor = 'confirmacao'

            # desenhando elementos na tela
            desenho_pagina_inicial()
            desenho_pagina_criar_conta()
            mouse.desenho()

            # atualizacao da tela
            atualizacao_da_tela()

        while subsetor == 'confirmacao':

            # definindo evento de saida
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.QUIT()

                if verificador == 'ok':
                    escrever_senha_confirmacao_extras(event)

                # interacao com o mouse
                if verificador == 'ok':
                    if mouse_colidindo(botao_nao_aviso_extras):
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            subsetor = 'criar conta'

                    if mouse_colidindo(botao_ok_aviso_extras):
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if texto_campo_senha_extras_real.frase == texto_campo_confirmacao_senha_aviso_real.frase:
                                adicionando_cadastro()
                                verificador = 'cadastro concluido'
                
                if verificador == 'login duplicado' or verificador == 'email duplicado':
                    if mouse_colidindo(botao_ok_aviso_login_extras):
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            subsetor = 'criar conta'

                if verificador == 'cadastro concluido':
                    if mouse_colidindo(botao_ok_aviso_login_extras):
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            subsetor = 'caiu'

            # desenhando elementos na tela
            desenho_pagina_inicial()
            desenho_pagina_criar_conta()
            desenho_pagina_aviso_extras(verificador)
            mouse.desenho()

            # atualizacao da tela
            atualizacao_da_tela()

    while setor == 'landing':

        while subsetor == 'caiu':
            
            subsetor = 'inicio'

        while subsetor == 'inicio':

            # definindo evento de saida
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.QUIT()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if mouse_colidindo(frame_opcoes):
                        subsetor = 'opcoes'

                    if mouse_colidindo(personagem_0_frame):
                        from modulos.setores.b_inicio.landing_page_criar_personagem import *
                        entrando_criar_personagem()
                        subsetor = 'criacao'

            # desenhando elementos na tela
            desenho_landing_page()
            teste_personagem()
            interacao_landingpage_mouse_colisao()
            mouse.desenho()

            # atualizacao da tela
            atualizacao_da_tela()

        while subsetor == 'opcoes':

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    setor = 'landing'
                    subsetor = 'caiu'

                # interacao com o mouse
                interacao_opcoes_mouse_evento(event)
                interacao_opcoes_mouse_saida(event)
                if interacao_opcoes_mouse_saida(event) == 'caiu':
                    gravando_alteracoes_db()
                    subsetor = 'caiu'

            interacao_opcoes_mouse()

            # desenhando elementos na tela
            desenho_landing_page()
            desenho_pagina_opcoes()
            mouse.desenho()

            # atualizacao da tela
            atualizacao_da_tela()
        
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
            mouse.desenho()
            
            desenho_aumento_de_atributo()
            calculos()

            # atualizacao da tela
            atualizacao_da_tela()