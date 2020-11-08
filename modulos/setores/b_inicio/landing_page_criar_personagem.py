import pygame, sys

sys.path.append('D:/Vini/Projetos/004 - RDC')

from modulos.segmentacao import *
from modulos.setores.b_inicio.landing_page import *

pygame.init()

janela_personagem = ExibirImagem('modulos/setores/b_inicio/criar_personagem/janela_personagem.png', 972, 1663, 5, 8.8)
texto_personagem = Escrever(7, 9.5, 'titulo', 'Personagem', 'preto')

frame_personagem = ExibirImagem('modulos/setores/b_inicio/criar_personagem/frame.png', 606, 775, 21.9, 14.6)
seta_virar_esquerda = ExibirImagem('modulos/setores/a_pagina_inicial/opcoes_ext/barra_intensidade_menor.png', 35, 46, 25.2, 32.8)
personagem_de_demonstracao = ExibirImagem('modulos/setores/b_inicio/criar_personagem/personagem_teste.png', 216, 564, 40.0, 19.8)
personagem_sombra = ExibirImagem('modulos/setores/b_inicio/criar_personagem/sombra.png', 330, 188, 34.7, 40.8)
seta_virar_direita = ExibirImagem('modulos/setores/a_pagina_inicial/opcoes_ext/barra_intensidade_maior.png', 35, 46, 71.9, 32.8)

frame_nome = ExibirImagem('modulos/setores/b_inicio/criar_personagem/frame_nome.png', 606, 85, 21.9, 55)
texto_nome = Escrever(50, 56.4, 'corpo', 'Nome de Teste', 'preto', 'centro')

texto_atributos = Escrever(50, 63.3, 'corpo', 'Atributos', 'preto', 'centro')

caixa_manual = ExibirImagemInterativa('modulos/setores/a_pagina_inicial/opcoes_ext/caixa_marcada.png', 'modulos/setores/a_pagina_inicial/opcoes_ext/caixa_nao_marcada.png', 35, 35, 18.5, 66.8)
texto_manual = Escrever(23.2, 66.8, 'corpo', 'Manual', 'preto')

caixa_automatico = ExibirImagemInterativa('modulos/setores/a_pagina_inicial/opcoes_ext/caixa_marcada.png', 'modulos/setores/a_pagina_inicial/opcoes_ext/caixa_nao_marcada.png', 35, 35, 60, 66.8)
texto_automatico = Escrever(64.6, 66.8, 'corpo', 'Automatico', 'preto')

texto_str = Escrever(11.5, 71, 'corpo', 'Str', 'azul')
caixa_str = ExibirImagem('modulos/setores/b_inicio/criar_personagem/grade_atributo.png', 164, 32, 19, 71.1)
atributo_str = Escrever(19.5, 71.2, 'item', '5', 'preto')
aumentar_str = ExibirImagem('modulos/setores/a_pagina_inicial/opcoes_ext/barra_intensidade_maior.png', 17, 23, 28.6, 71.3)
custo_str = Escrever(34, 71.2, 'item', '2', 'preto', 'direita')

texto_agi = Escrever(11.5, 73.5, 'corpo', 'Agi', 'azul')
caixa_agi = ExibirImagem('modulos/setores/b_inicio/criar_personagem/grade_atributo.png', 164, 32, 19, 73.6)
atributo_agi = Escrever(19.5, 73.7, 'item', '5', 'preto')
aumentar_agi = ExibirImagem('modulos/setores/a_pagina_inicial/opcoes_ext/barra_intensidade_maior.png', 17, 23, 28.6, 73.85)
custo_agi = Escrever(34, 73.7, 'item', '2', 'preto', 'direita')

texto_vit = Escrever(11.5, 76, 'corpo', 'Vit', 'azul')
caixa_vit = ExibirImagem('modulos/setores/b_inicio/criar_personagem/grade_atributo.png', 164, 32, 19, 76.1)
atributo_vit = Escrever(19.5, 76.2, 'item', '5', 'preto')
aumentar_vit = ExibirImagem('modulos/setores/a_pagina_inicial/opcoes_ext/barra_intensidade_maior.png', 17, 23, 28.6, 76.3)
custo_vit = Escrever(34, 76.2, 'item', '2', 'preto', 'direita')

texto_int = Escrever(11.5, 78.5, 'corpo', 'Int', 'azul')
caixa_int = ExibirImagem('modulos/setores/b_inicio/criar_personagem/grade_atributo.png', 164, 32, 19, 78.6)
atributo_int = Escrever(19.5, 78.75, 'item', '5', 'preto')
aumentar_int = ExibirImagem('modulos/setores/a_pagina_inicial/opcoes_ext/barra_intensidade_maior.png', 17, 23, 28.6, 78.85)
custo_int = Escrever(34, 78.75, 'item', '2', 'preto', 'direita')

texto_des = Escrever(11.5, 81, 'corpo', 'Des', 'azul')
caixa_des = ExibirImagem('modulos/setores/b_inicio/criar_personagem/grade_atributo.png', 164, 32, 19, 81.1)
atributo_des = Escrever(19.5, 81.2, 'item', '5', 'preto')
aumentar_des = ExibirImagem('modulos/setores/a_pagina_inicial/opcoes_ext/barra_intensidade_maior.png', 17, 23, 28.6, 81.3)
custo_des = Escrever(34, 81.2, 'item', '2', 'preto', 'direita')

texto_sor = Escrever(11.5, 83.5, 'corpo', 'Sor', 'azul')
caixa_sor = ExibirImagem('modulos/setores/b_inicio/criar_personagem/grade_atributo.png', 164, 32, 19, 83.6)
atributo_sor = Escrever(19.5, 83.7, 'item', '5', 'preto')
aumentar_sor = ExibirImagem('modulos/setores/a_pagina_inicial/opcoes_ext/barra_intensidade_maior.png', 17, 23, 28.6, 83.8)
custo_sor = Escrever(34, 83.7, 'item', '2', 'preto', 'direita')

texto_atq_fis = Escrever(37.5, 71, 'corpo', 'Ataque Fisico', 'azul')
texto_atq_fis_calculo = Escrever(88.2, 71, 'corpo', '7 + 0', 'preto', 'direita')
divisoria_atq_fis = ExibirImagem('modulos/setores/b_inicio/criar_personagem/divisoria_status.png', 554, 2, 37.2, 72.6)

texto_atq_mag = Escrever(37.5, 73.5, 'corpo', 'Ataque Magico', 'azul')
texto_atq_mag_calculo = Escrever(88.2, 73.5, 'corpo', '9 + 0', 'preto', 'direita')
divisoria_atq_mag = ExibirImagem('modulos/setores/b_inicio/criar_personagem/divisoria_status.png', 554, 2, 37.2, 75.2)

texto_def_fis = Escrever(37.5, 76, 'corpo', 'Def', 'azul')
texto_def_fis_calculo = Escrever(61.6, 76.0, 'corpo', '4 + 0', 'preto', 'direita')
divisoria_def_fis = ExibirImagem('modulos/setores/b_inicio/criar_personagem/divisoria_status.png', 265, 2, 37.2, 77.8)

texto_def_mag = Escrever(64.0, 76, 'corpo', 'DefM', 'azul')
texto_def_mag_calculo = Escrever(88.2, 76.0, 'corpo', '7 + 0', 'preto', 'direita')
divisoria_def_mag = ExibirImagem('modulos/setores/b_inicio/criar_personagem/divisoria_status.png', 265, 2, 63.7, 77.8)

texto_precisao = Escrever(37.5, 78.5, 'corpo', 'Precisao', 'azul')
texto_precisao_calculo = Escrever(61.6, 78.5, 'corpo', '182', 'preto', 'direita')
divisoria_precisao = ExibirImagem('modulos/setores/b_inicio/criar_personagem/divisoria_status.png', 265, 2, 37.2, 80.3)

texto_esquiva = Escrever(64.0, 78.5, 'corpo', 'Esqv', 'azul')
texto_esquiva_calculo = Escrever(88.2, 78.5, 'corpo', '107 + 1', 'preto', 'direita')
divisoria_esquiva = ExibirImagem('modulos/setores/b_inicio/criar_personagem/divisoria_status.png', 265, 2, 63.7, 80.3)

texto_critico = Escrever(37.5, 81, 'corpo', 'Critico', 'azul')
texto_critico_calculo = Escrever(61.6, 81, 'corpo', '2', 'preto', 'direita')
divisoria_critico = ExibirImagem('modulos/setores/b_inicio/criar_personagem/divisoria_status.png', 265, 2, 37.2, 82.7)

texto_vel_atq = Escrever(64.0, 81, 'corpo', 'Vel Atq', 'azul')
texto_vel_atq_calculo = Escrever(88.2, 81, 'corpo', '159', 'preto', 'direita')
divisoria_vel_atq = ExibirImagem('modulos/setores/b_inicio/criar_personagem/divisoria_status.png', 265, 2, 63.7, 82.7)

texto_pts_atributos = Escrever(37.5, 83.5, 'corpo', 'Pontos de Atributos', 'azul')
texto_pts_atributos_calculo = Escrever(88.2, 83.5, 'corpo', '0', 'preto', 'direita')
divisoria_pts_atributos = ExibirImagem('modulos/setores/b_inicio/criar_personagem/divisoria_status.png', 554, 2, 37.2, 85.1)

botao_ok_janela_personagem = ExibirImagem('modulos/setores/a_pagina_inicial/opcoes_ext/botao_curto.png', 106, 69, 83, 86.5)
texto_ok_janela_personagem = Escrever(85.9, 87.4, 'corpo', 'OK', 'preto')

def desenho_landing_page_criar_personagem():

    janela_personagem.desenho()
    texto_personagem.desenho()

    frame_personagem.desenho()
    seta_virar_esquerda.desenho()
    personagem_sombra.desenho()
    personagem_de_demonstracao.desenho()
    seta_virar_direita.desenho()

    frame_nome.desenho()
    texto_nome.desenho()

    texto_atributos.desenho()

    caixa_manual.desenho()
    texto_manual.desenho()

    caixa_automatico.desenho()
    texto_automatico.desenho()

    texto_str.desenho()
    caixa_str.desenho()
    atributo_str.desenho()
    aumentar_str.desenho()
    custo_str.desenho()

    texto_agi.desenho()
    caixa_agi.desenho()
    atributo_agi.desenho()
    aumentar_agi.desenho()
    custo_agi.desenho()

    texto_vit.desenho()
    caixa_vit.desenho()
    atributo_vit.desenho()
    aumentar_vit.desenho()
    custo_vit.desenho()

    texto_int.desenho()
    caixa_int.desenho()
    atributo_int.desenho()
    aumentar_int.desenho()
    custo_int.desenho()

    texto_des.desenho()
    caixa_des.desenho()
    atributo_des.desenho()
    aumentar_des.desenho()
    custo_des.desenho()

    texto_sor.desenho()
    caixa_sor.desenho()
    atributo_sor.desenho()
    aumentar_sor.desenho()
    custo_sor.desenho()

    texto_atq_fis.desenho()
    texto_atq_fis_calculo.desenho()
    divisoria_atq_fis.desenho()

    texto_atq_mag.desenho()
    texto_atq_mag_calculo.desenho()
    divisoria_atq_mag.desenho()

    texto_def_fis.desenho()
    texto_def_fis_calculo.desenho()
    divisoria_def_fis.desenho()

    texto_def_mag.desenho()
    texto_def_mag_calculo.desenho()
    divisoria_def_mag.desenho()

    texto_precisao.desenho()
    texto_precisao_calculo.desenho()
    divisoria_precisao.desenho()

    texto_esquiva.desenho()
    texto_esquiva_calculo.desenho()
    divisoria_esquiva.desenho()

    texto_critico.desenho()
    texto_critico_calculo.desenho()
    divisoria_critico.desenho()

    texto_vel_atq.desenho()
    texto_vel_atq_calculo.desenho()
    divisoria_vel_atq.desenho()

    texto_pts_atributos.desenho()
    texto_pts_atributos_calculo.desenho()
    divisoria_pts_atributos.desenho()

    botao_ok_janela_personagem.desenho()
    texto_ok_janela_personagem.desenho()


if __name__ == '__main__':

    game_rodando = True
    while game_rodando == True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_rodando = False

        desenho_landing_page()
        desenho_landing_page_criar_personagem()

        pygame.display.update()
        relogio_de_atualizacao.tick(ponteiro)