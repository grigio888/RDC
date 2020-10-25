import pygame
import sys

sys.path.append('D:/Vini/Projetos/004 - RDC')

from modulos.segmentacao import *
from modulos.setores.c_inicio.landing_page_classes import *

pygame.init()

janela_personagem = JanelaLanding(5, 19, 'meio')
texto_personagem = Escrever(7, 20, 'titulo', 'Personagem', 'preto')

personagem_0_frame = Frames(10.6, 23.7, 'frame')
#aqui entra o personagem#
personagem_0_sombra = Frames(21.8, 43.3, 'sombra')
personagem_0_nome = Escrever(29.4, 50.1, 'item', 'Nome_Char', 'preto', 'centro')

personagem_1_frame = Frames(51.7, 23.7, 'frame')
#aqui entra o personagem#
personagem_1_sombra = Frames(62.8, 43.3, 'sombra')
personagem_1_nome = Escrever(70.5, 50.1, 'item', 'Nome_Char', 'preto', 'centro')

personagem_2_frame = Frames(10.6, 52, 'frame')
#aqui entra o personagem#
personagem_2_sombra = Frames(21.8, 71.6, 'sombra')
personagem_2_nome = Escrever(29.4, 78.4, 'item', 'Nome_Char', 'preto', 'centro')

personagem_3_frame = Frames(51.7, 52, 'frame')
#aqui entra o personagem#
personagem_3_sombra = Frames(62.8, 71.6, 'sombra')
personagem_3_nome = Escrever(70.5, 78.4, 'item', 'Nome_Char', 'preto', 'centro')