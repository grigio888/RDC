import pygame, sys
from time import gmtime, strftime

sys.path.append('D:/Vini/Projetos/004 - RDC')

from modulos.segmentacao import *
from modulos.setores.b_inicio.landing_page import *

pygame.init()

janela_personagem = ExibirImagem('modulos/setores/b_inicio/criar_personagem/janela_personagem.png', 972, 1663, 5, 8.8)
texto_personagem = Escrever(7, 9.5, 'titulo', 'Personagem', 'preto')

frame_personagem = ExibirImagem('modulos/setores/b_inicio/criar_personagem/frame.png', 606, 775, 21.9, 14.6)
seta_virar_esquerda = ExibirImagem('modulos/setores/b_inicio/opcoes_ext/barra_intensidade_menor.png', 35, 46, 25.2, 32.8)
personagem_de_demonstracao = ExibirImagem('modulos/setores/b_inicio/criar_personagem/personagem_teste.png', 216, 564, 40.0, 19.8)
personagem_sombra = ExibirImagem('modulos/setores/b_inicio/criar_personagem/sombra.png', 330, 188, 34.7, 40.8)
seta_virar_direita = ExibirImagem('modulos/setores/b_inicio/opcoes_ext/barra_intensidade_maior.png', 35, 46, 71.9, 32.8)

frame_nome = ExibirImagem('modulos/setores/b_inicio/criar_personagem/frame_nome.png', 606, 85, 21.9, 55)
texto_nome = Escrever(50, 56.4, 'corpo', 'Nome de Teste', 'preto', 'centro')
texto_nome_escrevendo = False
texto_nome_entrada = ''
tempo = int(strftime("%S", gmtime()))

level_base = 1
texto_introducao = Escrever(50, 63.3, 'corpo', 'Aprendiz, Level Base: ' + str(level_base), 'preto', 'centro')

texto_atributos = Escrever(50, 68, 'corpo', 'Atributos', 'preto', 'centro')

#caixa_manual = ExibirImagemInterativa('modulos/setores/a_pagina_inicial/opcoes_ext/caixa_marcada.png', 'modulos/setores/a_pagina_inicial/opcoes_ext/caixa_nao_marcada.png', 35, 35, 18.5, 66.8)
#texto_manual = Escrever(23.2, 66.8, 'corpo', 'Manual', 'preto')

#caixa_automatico = ExibirImagemInterativa('modulos/setores/a_pagina_inicial/opcoes_ext/caixa_marcada.png', 'modulos/setores/a_pagina_inicial/opcoes_ext/caixa_nao_marcada.png', 35, 35, 60, 66.8)
#caixa_automatico.mudanca_de_estado()
#caixa_automatico.automatico()
#texto_automatico = Escrever(64.6, 66.8, 'corpo', 'Automatico', 'preto')

atributo_passivo_for = 1
atributo_custo_for = 2
texto_for = Escrever(11.5, 71, 'corpo', 'Str', 'azul')
caixa_for = ExibirImagem('modulos/setores/b_inicio/criar_personagem/grade_atributo.png', 164, 32, 19, 71.1)
atributo_for = Escrever(19.5, 71.2, 'item', str(atributo_passivo_for), 'preto')
aumentar_for = ExibirImagem('modulos/setores/b_inicio/opcoes_ext/barra_intensidade_maior.png', 17, 23, 28.6, 71.3)
custo_for = Escrever(34, 71.2, 'item', str(atributo_custo_for), 'preto', 'direita')

atributo_passivo_agi = 1
atributo_custo_agi = 2
texto_agi = Escrever(11.5, 73.5, 'corpo', 'Agi', 'azul')
caixa_agi = ExibirImagem('modulos/setores/b_inicio/criar_personagem/grade_atributo.png', 164, 32, 19, 73.6)
atributo_agi = Escrever(19.5, 73.7, 'item', str(atributo_passivo_agi), 'preto')
aumentar_agi = ExibirImagem('modulos/setores/b_inicio/opcoes_ext/barra_intensidade_maior.png', 17, 23, 28.6, 73.85)
custo_agi = Escrever(34, 73.7, 'item', str(atributo_custo_agi), 'preto', 'direita')

atributo_passivo_vit = 1
atributo_custo_vit = 2
texto_vit = Escrever(11.5, 76, 'corpo', 'Vit', 'azul')
caixa_vit = ExibirImagem('modulos/setores/b_inicio/criar_personagem/grade_atributo.png', 164, 32, 19, 76.1)
atributo_vit = Escrever(19.5, 76.2, 'item', str(atributo_passivo_vit), 'preto')
aumentar_vit = ExibirImagem('modulos/setores/b_inicio/opcoes_ext/barra_intensidade_maior.png', 17, 23, 28.6, 76.3)
custo_vit = Escrever(34, 76.2, 'item', str(atributo_custo_vit), 'preto', 'direita')

atributo_passivo_int = 1
atributo_custo_int = 2
texto_int = Escrever(11.5, 78.5, 'corpo', 'Int', 'azul')
caixa_int = ExibirImagem('modulos/setores/b_inicio/criar_personagem/grade_atributo.png', 164, 32, 19, 78.6)
atributo_int = Escrever(19.5, 78.75, 'item', str(atributo_passivo_int), 'preto')
aumentar_int = ExibirImagem('modulos/setores/b_inicio/opcoes_ext/barra_intensidade_maior.png', 17, 23, 28.6, 78.85)
custo_int = Escrever(34, 78.75, 'item', str(atributo_custo_int), 'preto', 'direita')

atributo_passivo_des = 1
atributo_custo_des = 2
texto_des = Escrever(11.5, 81, 'corpo', 'Des', 'azul')
caixa_des = ExibirImagem('modulos/setores/b_inicio/criar_personagem/grade_atributo.png', 164, 32, 19, 81.1)
atributo_des = Escrever(19.5, 81.2, 'item', str(atributo_passivo_des), 'preto')
aumentar_des = ExibirImagem('modulos/setores/b_inicio/opcoes_ext/barra_intensidade_maior.png', 17, 23, 28.6, 81.3)
custo_des = Escrever(34, 81.2, 'item', str(atributo_custo_des), 'preto', 'direita')

atributo_passivo_sor = 1
atributo_custo_sor = 2
texto_sor = Escrever(11.5, 83.5, 'corpo', 'Sor', 'azul')
caixa_sor = ExibirImagem('modulos/setores/b_inicio/criar_personagem/grade_atributo.png', 164, 32, 19, 83.6)
atributo_sor = Escrever(19.5, 83.7, 'item', str(atributo_passivo_sor), 'preto')
aumentar_sor = ExibirImagem('modulos/setores/b_inicio/opcoes_ext/barra_intensidade_maior.png', 17, 23, 28.6, 83.8)
custo_sor = Escrever(34, 83.7, 'item', str(atributo_custo_sor), 'preto', 'direita')

ataque_fisico_passivo = 7
ataque_fisico_item = 0
texto_atq_fis = Escrever(37.5, 71, 'corpo', 'Ataque Fisico', 'azul')
texto_atq_fis_calculo = Escrever(88.2, 71, 'corpo', str(ataque_fisico_passivo) + ' + ' + str(ataque_fisico_item), 'preto', 'direita')
divisoria_atq_fis = ExibirImagem('modulos/setores/b_inicio/criar_personagem/divisoria_status.png', 554, 2, 37.2, 72.6)

ataque_magico_passivo = 9
ataque_magico_item = 0
texto_atq_mag = Escrever(37.5, 73.5, 'corpo', 'Ataque Magico', 'azul')
texto_atq_mag_calculo = Escrever(88.2, 73.5, 'corpo', str(ataque_magico_passivo) + ' + ' + str(ataque_magico_item), 'preto', 'direita')
divisoria_atq_mag = ExibirImagem('modulos/setores/b_inicio/criar_personagem/divisoria_status.png', 554, 2, 37.2, 75.2)

defesa_fisica_passiva = 4
defesa_fisica_item = 0
texto_def_fis = Escrever(37.5, 76, 'corpo', 'Def', 'azul')
texto_def_fis_calculo = Escrever(61.6, 76.0, 'corpo', str(defesa_fisica_passiva) + ' + ' + str(defesa_fisica_item), 'preto', 'direita')
divisoria_def_fis = ExibirImagem('modulos/setores/b_inicio/criar_personagem/divisoria_status.png', 265, 2, 37.2, 77.8)

defesa_magica_passiva = 7
defesa_magica_item = 0
texto_def_mag = Escrever(64.0, 76, 'corpo', 'DefM', 'azul')
texto_def_mag_calculo = Escrever(88.2, 76.0, 'corpo', str(defesa_magica_passiva) + ' + ' + str(defesa_magica_item), 'preto', 'direita')
divisoria_def_mag = ExibirImagem('modulos/setores/b_inicio/criar_personagem/divisoria_status.png', 265, 2, 63.7, 77.8)

precisao_passiva = 182
precisao_item = 0
texto_precisao = Escrever(37.5, 78.5, 'corpo', 'Precisao', 'azul')
texto_precisao_calculo = Escrever(61.6, 78.5, 'corpo', str(precisao_passiva), 'preto', 'direita')
divisoria_precisao = ExibirImagem('modulos/setores/b_inicio/criar_personagem/divisoria_status.png', 265, 2, 37.2, 80.3)

esquiva_normal = 107
esquiva_perfeita = 1
texto_esquiva = Escrever(64.0, 78.5, 'corpo', 'Esqv', 'azul')
texto_esquiva_calculo = Escrever(88.2, 78.5, 'corpo', str(esquiva_normal) + ' + ' + str(esquiva_perfeita), 'preto', 'direita')
divisoria_esquiva = ExibirImagem('modulos/setores/b_inicio/criar_personagem/divisoria_status.png', 265, 2, 63.7, 80.3)

critico_passivo = 2
critico_item = 0
texto_critico = Escrever(37.5, 81, 'corpo', 'Critico', 'azul')
texto_critico_calculo = Escrever(61.6, 81, 'corpo', str(critico_passivo), 'preto', 'direita')
divisoria_critico = ExibirImagem('modulos/setores/b_inicio/criar_personagem/divisoria_status.png', 265, 2, 37.2, 82.7)

velocidade_de_ataque = 159
texto_vel_atq = Escrever(64.0, 81, 'corpo', 'Vel Atq', 'azul')
texto_vel_atq_calculo = Escrever(88.2, 81, 'corpo', str(velocidade_de_ataque), 'preto', 'direita')
divisoria_vel_atq = ExibirImagem('modulos/setores/b_inicio/criar_personagem/divisoria_status.png', 265, 2, 63.7, 82.7)

pontos_de_atributos = 48
texto_pts_atributos = Escrever(37.5, 83.5, 'corpo', 'Pontos de Atributos', 'azul')
texto_pts_atributos_calculo = Escrever(88.2, 83.5, 'corpo', str(pontos_de_atributos), 'preto', 'direita')
divisoria_pts_atributos = ExibirImagem('modulos/setores/b_inicio/criar_personagem/divisoria_status.png', 554, 2, 37.2, 85.1)

botao_ok_janela_personagem = ExibirImagem('modulos/setores/b_inicio/opcoes_ext/botao_curto.png', 106, 69, 83, 86.5)
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

    texto_introducao.desenho()

    texto_atributos.desenho()

    #caixa_manual.desenho()
    #texto_manual.desenho()

    #caixa_automatico.desenho()
    #texto_automatico.desenho()

    texto_for.desenho()
    caixa_for.desenho()
    atributo_for.desenho()
    #aumentar_for.desenho()
    custo_for.desenho()

    texto_agi.desenho()
    caixa_agi.desenho()
    atributo_agi.desenho()
    #aumentar_agi.desenho()
    custo_agi.desenho()

    texto_vit.desenho()
    caixa_vit.desenho()
    atributo_vit.desenho()
    #aumentar_vit.desenho()
    custo_vit.desenho()

    texto_int.desenho()
    caixa_int.desenho()
    atributo_int.desenho()
    #aumentar_int.desenho()
    custo_int.desenho()

    texto_des.desenho()
    caixa_des.desenho()
    atributo_des.desenho()
    #aumentar_des.desenho()
    custo_des.desenho()

    texto_sor.desenho()
    caixa_sor.desenho()
    atributo_sor.desenho()
    #aumentar_sor.desenho()
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

#def interacao_criar_personagem_caixas_confirm(evento):
#    if evento.type == pygame.MOUSEBUTTONDOWN:
#        if pygame.mouse.get_pos()[0] >= caixa_manual.porcentagem_pos_x:
#            if pygame.mouse.get_pos()[1] >= caixa_manual.porcentagem_pos_y:
#                if pygame.mouse.get_pos()[0] <= caixa_manual.porcentagem_pos_x + caixa_manual.largura_transformada:
#                    if pygame.mouse.get_pos()[1] <= caixa_manual.porcentagem_pos_y + caixa_manual.altura_transformada:
#                        caixa_manual.mudanca_de_estado()
#                        caixa_manual.automatico()
#                        caixa_automatico.mudanca_de_estado()
#                        caixa_automatico.automatico()
#                        print('funcionou 1')
#        if pygame.mouse.get_pos()[0] >= caixa_automatico.porcentagem_pos_x:
#            if pygame.mouse.get_pos()[1] >= caixa_automatico.porcentagem_pos_y:
#                if pygame.mouse.get_pos()[0] <= caixa_automatico.porcentagem_pos_x + caixa_automatico.largura_transformada:
#                    if pygame.mouse.get_pos()[1] <= caixa_automatico.porcentagem_pos_y + caixa_automatico.altura_transformada:
#                        caixa_automatico.mudanca_de_estado()
#                        caixa_automatico.automatico()
#                        caixa_manual.mudanca_de_estado()
#                        caixa_manual.automatico()
#                        print('funcionou 2')

def interacao_opcoes_mouse_saida(evento):
    if evento.type == pygame.MOUSEBUTTONDOWN:
       if pressionar_botao(botao_ok_janela_personagem):
            return 'caiu'

def escrever_nome(event):
    
    global texto_nome_escrevendo, texto_nome_entrada, tempo
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        if pygame.mouse.get_pos()[0] >= frame_nome.porcentagem_pos_x:
            if pygame.mouse.get_pos()[1] >= frame_nome.porcentagem_pos_y:
                if pygame.mouse.get_pos()[0] <= frame_nome.porcentagem_pos_x + frame_nome.largura_transformada:
                    if pygame.mouse.get_pos()[1] <= frame_nome.porcentagem_pos_y + frame_nome.altura_transformada:
                        texto_nome_escrevendo = True
                        
        else:
            texto_nome_escrevendo = False

    #if texto_nome_escrevendo == True:
    #    if tempo % 2 == 0:
    #        if texto_nome.frase[:-1] != 'I':
    #            texto_nome.frase += 'I'
    #    else:
    #        if texto_nome.frase[:-1] == 'I':
    #            texto_nome.frase = texto_nome.frase[:-1]
            

    if event.type == pygame.KEYDOWN:
        if texto_nome_escrevendo:
            if event.key == pygame.K_RETURN:
                texto_nome_escrevendo = False
            elif event.key == pygame.K_BACKSPACE:
                texto_nome.frase = texto_nome.frase[:-1]
            else:
                texto_nome.frase += event.unicode

atributo_custo = [atributo_custo_for, atributo_custo_agi, atributo_custo_vit, atributo_custo_int, atributo_custo_des, atributo_custo_sor]
atributo_passivo = [atributo_passivo_for, atributo_passivo_agi, atributo_passivo_vit, atributo_passivo_int, atributo_passivo_des, atributo_passivo_sor]
atributo = [atributo_for, atributo_agi, atributo_vit, atributo_int, atributo_des, atributo_sor]
aumentar_atributo = [aumentar_for, aumentar_agi, aumentar_vit, aumentar_int, aumentar_des, aumentar_sor]

def aumento_de_atributo(event):
    
    global pontos_de_atributos, texto_pts_atributos_calculo, atributo_custo, atributo_passivo_for, atributo_passivo_agi, atributo_passivo_vit, atributo_passivo_int, atributo_passivo_des, atributo_passivo_sor
    
    for index in range(0, 6):
        if pontos_de_atributos >= atributo_custo[index]:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] >= aumentar_atributo[index].porcentagem_pos_x:
                    if pygame.mouse.get_pos()[1] >= aumentar_atributo[index].porcentagem_pos_y:
                        if pygame.mouse.get_pos()[0] <= aumentar_atributo[index].porcentagem_pos_x + aumentar_atributo[index].largura_transformada:
                            if pygame.mouse.get_pos()[1] <= aumentar_atributo[index].porcentagem_pos_y + aumentar_atributo[index].altura_transformada:
                                if index == 0:
                                    atributo_passivo_for += 1
                                    pontos_de_atributos -= atributo_custo[index]
                                    atributo_for.frase = str(atributo_passivo_for)
                                    texto_pts_atributos_calculo.frase = str(pontos_de_atributos)
                                if index == 1:
                                    atributo_passivo_agi += 1
                                    pontos_de_atributos -= atributo_custo[index]
                                    atributo_agi.frase = str(atributo_passivo_agi)
                                    texto_pts_atributos_calculo.frase = str(pontos_de_atributos)
                                if index == 2:
                                    atributo_passivo_vit += 1
                                    pontos_de_atributos -= atributo_custo[index]
                                    atributo_vit.frase = str(atributo_passivo_vit)
                                    texto_pts_atributos_calculo.frase = str(pontos_de_atributos)
                                if index == 3:
                                    atributo_passivo_int += 1
                                    pontos_de_atributos -= atributo_custo[index]
                                    atributo_int.frase = str(atributo_passivo_int)
                                    texto_pts_atributos_calculo.frase = str(pontos_de_atributos)
                                if index == 4:
                                    atributo_passivo_des += 1
                                    pontos_de_atributos -= atributo_custo[index]
                                    atributo_des.frase = str(atributo_passivo_des)
                                    texto_pts_atributos_calculo.frase = str(pontos_de_atributos)
                                if index == 5:
                                    atributo_passivo_sor += 1
                                    pontos_de_atributos -= atributo_custo[index]
                                    atributo_sor.frase = str(atributo_passivo_sor)
                                    texto_pts_atributos_calculo.frase = str(pontos_de_atributos)
                                
def desenho_aumento_de_atributo():
    
    global pontos_de_atributos, atributos_custo, aumentar_atributo
    
    for index in range(0, 6):
        if pontos_de_atributos >= atributo_custo[index]:
            aumentar_atributo[index].desenho()
            
def calculos():
    ataque_fisico_passivo = ((level_base // 4) + atributo_passivo_for + (atributo_passivo_des // 5) + (atributo_passivo_sor // 3))
    texto_atq_fis_calculo.frase = str(ataque_fisico_passivo) + ' + ' + str(ataque_fisico_item)
    ataque_magico_passivo = ((level_base // 4) + atributo_passivo_int + (atributo_passivo_int // 2) + (atributo_passivo_des // 5) + (atributo_passivo_sor // 3))
    texto_atq_mag_calculo.frase = str(ataque_magico_passivo) + ' + ' + str(ataque_magico_item)
    defesa_fisica_passiva = (1 + (level_base // 2) + (atributo_passivo_agi // 5) + (atributo_passivo_vit // 2))
    texto_def_fis_calculo.frase = str(defesa_fisica_passiva) + ' + ' + str(defesa_fisica_item)
    defesa_magica_passiva = (1 + (level_base // 4) + atributo_passivo_int + (atributo_passivo_vit // 5) + (atributo_passivo_des // 5))
    texto_def_mag_calculo.frase = str(defesa_magica_passiva) + ' + ' + str(defesa_magica_item)
    precisao_passiva = (175 +  level_base + atributo_passivo_des + (atributo_passivo_sor // 3) + precisao_item)
    texto_precisao_calculo.frase = str(precisao_passiva)
    esquiva_passiva = (100 +  level_base + atributo_passivo_agi + (atributo_passivo_sor // 5))
    esquiva_perfeita = (1 + (atributo_passivo_sor // 10))
    texto_esquiva_calculo.frase = str(esquiva_passiva) + ' + ' + str(esquiva_perfeita)
    critico_passivo = ((atributo_passivo_sor // 3) + critico_item)
    texto_critico_calculo.frase = str(critico_passivo)
    
if __name__ == '__main__':

    game_rodando = True
    while game_rodando == True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_rodando = False

            escrever_nome(event)
            aumento_de_atributo(event)

        desenho_landing_page()
        desenho_landing_page_criar_personagem()
        #distribuicao_de_pontos_atributos()

        desenho_aumento_de_atributo()
        calculos()

        pygame.display.update()
        relogio_de_atualizacao.tick(ponteiro)