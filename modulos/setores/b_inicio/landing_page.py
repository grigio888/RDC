import pygame, sys
import mysql.connector as conectante
from modulos.segmentacao import *
from modulos.setores.b_inicio.opcoes import *

sys.path.append(caminho_raiz_pc)

pygame.init()

# conectando ao banco de dados:
login = conectante.connect(user='root', password='kiju1475',
                         host='localhost',
                         database='rdc')

cursor = login.cursor()

comando = ('select noChar, score, zeny from login join informacoes_da_conta on infos_FK where login = %s and senha = %s')
cursor.execute(comando, (texto_campo_login.frase, texto_campo_senha_real.frase))

dados_landing_page = cursor.fetchall()

login.close()

# variaveis:

fundo_inicio = ExibirImagem('modulos/setores/b_inicio/landing_page/fundo.png', 1080, 2020, 0, 0)

# Conta
janela_conta = ExibirImagem('modulos/setores/b_inicio/landing_page/janela_cima.png', 972, 333, 5, 1.5)
texto_conta = Escrever(janela_conta.pos_x + 2, janela_conta.pos_y + 0.9, 'titulo', 'Conta', 'preto')

nome_da_conta = Escrever(janela_conta.pos_x + 3.3, janela_conta.pos_y + 4.2, 'corpo', texto_campo_login.frase, 'preto')

num_de_personagens_0 = Escrever(janela_conta.pos_x + 5.1, janela_conta.pos_y + 7.8, 'corpo', 'No. de Personagens:', 'preto')
num_de_personagens_1 = Escrever(janela_conta.pos_x + 85, janela_conta.pos_y + 7.8, 'corpo', str(dados_landing_page[0][0]) + ' / 4 pngs', 'preto', 'direita')

score_0 = Escrever(janela_conta.pos_x + 5.1, janela_conta.pos_y + 10.5, 'corpo', 'Score Maximo:', 'preto')
score_1 = Escrever(janela_conta.pos_x + 85, janela_conta.pos_y + 10.5, 'corpo', str(dados_landing_page[0][1]) + ' pts.', 'preto', 'direita')

dinheiro_0 = Escrever(janela_conta.pos_x + 45, janela_conta.pos_y + 14, 'titulo', 'Zenys:', 'preto')
dinheiro_1 = Escrever(janela_conta.pos_x + 88, janela_conta.pos_y + 14, 'titulo', str(dados_landing_page[0][2]) + ' z', 'preto', 'direita')

#Personagens
janela_personagem = ExibirImagem('modulos/setores/b_inicio/landing_page/janela_meio.png', 972, 1244, 5, 19)
texto_personagem = Escrever(janela_personagem.pos_x + 2, janela_personagem.pos_y + 0.9, 'titulo', 'Personagem', 'preto')

personagem_0_frame = ExibirImagem('modulos/setores/b_inicio/landing_page/frame_personagem.png', 404, 517, janela_personagem.pos_x + 5.6, janela_personagem.pos_y + 4.7)
personagem_0 = None
personagem_0_adicionar = ExibirImagem('modulos/setores/b_inicio/landing_page/adicionar.png', 60, 60, janela_personagem.pos_x + 21.6, janela_personagem.pos_y + 16)
personagem_0_sombra = ExibirImagem('modulos/setores/b_inicio/landing_page/frame_sombra.png', 165, 94, janela_personagem.pos_x + 16.8, janela_personagem.pos_y + 24.3)
personagem_0_nome = Escrever(janela_personagem.pos_x + 24.4, janela_personagem.pos_y + 31.1, 'item', 'Nome_Char', 'preto', 'centro')

personagem_1_frame = ExibirImagem('modulos/setores/b_inicio/landing_page/frame_personagem.png', 404, 517, janela_personagem.pos_x + 46.7, janela_personagem.pos_y + 4.7)
personagem_1 = None
personagem_1_adicionar = ExibirImagem('modulos/setores/b_inicio/landing_page/adicionar.png', 60, 60, janela_personagem.pos_x + 62.7, janela_personagem.pos_y + 16)
personagem_1_sombra = ExibirImagem('modulos/setores/b_inicio/landing_page/frame_sombra.png', 165, 94, janela_personagem.pos_x + 57.8, janela_personagem.pos_y + 24.3)
personagem_1_nome = Escrever(janela_personagem.pos_x + 65.5, janela_personagem.pos_y + 31.1, 'item', 'Nome_Char', 'preto', 'centro')

personagem_2_frame = ExibirImagem('modulos/setores/b_inicio/landing_page/frame_personagem.png', 404, 517, janela_personagem.pos_x + 5.6, janela_personagem.pos_y + 33)
personagem_2 = None
personagem_2_adicionar = ExibirImagem('modulos/setores/b_inicio/landing_page/adicionar.png', 60, 60, janela_personagem.pos_x + 21.6, janela_personagem.pos_y + 44.4)
personagem_2_sombra = ExibirImagem('modulos/setores/b_inicio/landing_page/frame_sombra.png', 165, 94, janela_personagem.pos_x + 16.8, janela_personagem.pos_y + 52.6)
personagem_2_nome = Escrever(janela_personagem.pos_x + 24.4, janela_personagem.pos_y + 59.4, 'item', 'Nome_Char', 'preto', 'centro')

personagem_3_frame = ExibirImagem('modulos/setores/b_inicio/landing_page/frame_personagem.png', 404, 517, janela_personagem.pos_x + 46.7, janela_personagem.pos_y + 33)
personagem_3 = None
personagem_3_adicionar = ExibirImagem('modulos/setores/b_inicio/landing_page/adicionar.png', 60, 60, janela_personagem.pos_x + 62.7, janela_personagem.pos_y + 44.4)
personagem_3_sombra = ExibirImagem('modulos/setores/b_inicio/landing_page/frame_sombra.png', 165, 94, janela_personagem.pos_x + 57.8, janela_personagem.pos_y + 52.6)
personagem_3_nome = Escrever(janela_personagem.pos_x + 65.5, janela_personagem.pos_y + 59.4, 'item', 'Nome_Char', 'preto', 'centro')

#Diversos
janela_diversos = ExibirImagem('modulos/setores/b_inicio/landing_page/janela_baixo.png', 972, 333, 5, 81.5)
texto_diversos = Escrever(janela_diversos.pos_x + 2, janela_diversos.pos_y + 0.9, 'titulo', 'Diversos', 'preto')

frame_mochila = ExibirImagem('modulos/setores/b_inicio/landing_page/frame_item.png', 210, 240, janela_diversos.pos_x + 3.5, janela_diversos.pos_y + 3.7)
opcao_mochila = ExibirItem(janela_diversos.pos_x + 6.3, janela_diversos.pos_y + 3.5, 2641, 1, 2.2)
texto_mochila = Escrever(janela_diversos.pos_x + 12.75, janela_diversos.pos_y + 14, 'item', 'Mochila', 'preto', 'centro')

frame_chave = ExibirImagem('modulos/setores/b_inicio/landing_page/frame_item.png', 210, 240, janela_diversos.pos_x + 25, janela_diversos.pos_y + 3.7)
opcao_chave = ExibirItem(janela_diversos.pos_x + 29.4, janela_diversos.pos_y + 4.5, 7026, 1, 1.9)
texto_chave = Escrever(janela_diversos.pos_x + 34.5, janela_diversos.pos_y + 14, 'item', 'Chave', 'preto', 'centro')

frame_forja = ExibirImagem('modulos/setores/b_inicio/landing_page/frame_item.png', 210, 240, janela_diversos.pos_x + 46.6, janela_diversos.pos_y + 3.7)
opcao_forja = ExibirItem(janela_diversos.pos_x + 47.5, janela_diversos.pos_y + 3, 7811, 1, 2.4)
texto_forja = Escrever(janela_diversos.pos_x + 55.85, janela_diversos.pos_y + 14, 'item', 'Forja', 'preto', 'centro')

frame_opcoes = ExibirImagem('modulos/setores/b_inicio/landing_page/frame_item.png', 210, 240, janela_diversos.pos_x + 68.1, janela_diversos.pos_y + 3.7)
opcao_opcoes = ExibirItem(janela_diversos.pos_x + 70.5, janela_diversos.pos_y + 3.5, 7703, 1, 2.1)
texto_opcoes = Escrever(janela_diversos.pos_x + 77.35, janela_diversos.pos_y + 14, 'item', 'Opcoes', 'preto', 'centro')

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