import pygame
import sys

sys.path.append('D:/Vini/Projetos/004 - RDC')

from modulos.segmentacao import *
from modulos.classes import *

pygame.init()

janela_diversos = JanelaLanding(5, 81.5, 'baixo')
texto_diversos = Escrever(7, 82.4, 'titulo', 'Diversos', 'preto')

frame_mochila = Frames(8.5, 85.2, 'frame_item')
opcao_mochila = ImagemItem(11.3, 85, 2641, 1)
texto_mochila = Escrever(17.75, 95, 'item', 'Mochila', 'preto', 'centro')

frame_2 = Frames(30, 85.2, 'frame_item')
opcao_2 = ImagemItem(34.4, 86, 7026, 1, 0.75)
texto_2 = Escrever(39.5, 95, 'item', 'Chave', 'preto', 'centro')

frame_3 = Frames(51.6, 85.2, 'frame_item')
opcao_3 = ImagemItem(52.5, 84.5, 7811, 1, 1)
texto_3 = Escrever(60.85, 95, 'item', 'Forja', 'preto', 'centro')

frame_4 = Frames(73.1, 85.2, 'frame_item')
opcao_4 = ImagemItem(75.7, 84.5, 7703, 1, 0.95)
texto_4 = Escrever(82.35, 95, 'item', 'Opcoes', 'preto', 'centro')