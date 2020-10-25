import pygame

pygame.init()
pygame.mixer.init()

from modulos.segmentacao import *

while game_rodando:

    musica_menu_inicio()

    while setor == 'pagina inicial':

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
                                    from modulos.setores.b_loading.loading import *
                                    setor = 'inicio'
                                    subsetor = 'loading'
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
                                    subsetor = 'opcoes'
                                    som_clique.play()

            # desenhando elementos na tela
            desenho_pagina_inicial()

            # atualizacao da tela
            pygame.display.update()
            relogio_de_atualizacao.tick(ponteiro)
    
        while subsetor == 'opcoes':

            carregando = Loading(27.7, 70.5, '0')
            carregado = 0

            while carregado == 0:

                for loading in range (0, 101, 25):

                    if loading <= 40:
                        from modulos.setores.a_pagina_inicial.opcoes_ext.opcoes_parte_1 import *

                    if loading >= 70:
                        from modulos.setores.a_pagina_inicial.opcoes_ext.opcoes_parte_2 import *
                        
                    if loading >= 90:
                        from modulos.setores.a_pagina_inicial.opcoes import *

                    if loading >= 95:
                        carregado = 1

                    desenho_pagina_inicial()
                    carregando.porcentagem_de_carregamento = str(loading)
                    carregando.desenho()
                    
                    pygame.display.update()
                    relogio_de_atualizacao.tick(ponteiro)

            while carregado == 1:
                # definindo evento de saida
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_rodando = False
                        setor = 'saida'
                        subsetor = 'saida'
                        carregado = 2

                    # interacao com o mouse
                    if event.type == pygame.MOUSEBUTTONDOWN:
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
                                        game_rodando = False
                                        setor = 'pagina inicial'
                                        subsetor = 'inicio'
                                        carregado = 2
                                        som_clique.play()
                
                
                if pygame.mouse.get_pressed()[0]:
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

                

                # desenhando elementos na tela
                desenho_pagina_inicial()
                desenho_pagina_opcoes()

                # atualizacao da tela
                pygame.display.update()
                relogio_de_atualizacao.tick(ponteiro)

    while setor == 'inicio':

        carregando = Loading(27.7, 70.5, '0')

        while subsetor == 'loading':

            for loading in range (0, 101, 20):

                if loading <= 0:
                    from modulos.setores.c_inicio.landing_page_classes import *
                    fundo_inicio = FundoInicio(0, 0)

                if loading >= 10:
                    from modulos.setores.c_inicio.landing_page_conta import *
                    
                if loading >= 25:
                    from modulos.setores.c_inicio.landing_page_personagem import *

                if loading >= 50:
                    from modulos.setores.c_inicio.landing_page_diversos import *

                if loading >= 75:
                    from modulos.setores.c_inicio.landing_page import *

                if loading >= 95:
                    subsetor = 'landing'

                fundo.desenho()
                carregando.porcentagem_de_carregamento = str(loading)
                carregando.desenho()

                pygame.display.update()
                relogio_de_atualizacao.tick(ponteiro)

        while subsetor == 'landing':

            # definindo evento de saida
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_rodando = False
                    setor = 'saida'
                    subsetor = 'saida'

            # desenhando elementos na tela
            desenho_landing_page()

            # atualizacao da tela
            pygame.display.update()
            relogio_de_atualizacao.tick(ponteiro)