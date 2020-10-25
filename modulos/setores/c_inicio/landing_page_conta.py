import pygame
import sys

sys.path.append('D:/Vini/Projetos/004 - RDC')

from modulos.segmentacao import *
from modulos.setores.c_inicio.landing_page_classes import *

pygame.init()

janela_conta = JanelaLanding(5, 1.5, 'cima')
texto_conta = Escrever(7, 2.2, 'titulo', 'Conta', 'preto')

nome_da_conta = Escrever(8.3, 5.7, 'corpo', 'Nome_Da_Conta', 'preto')

num_de_personagens_0 = Escrever(10.1, 9.3, 'corpo', 'No. de Personagens:', 'preto')
num_de_personagens_1 = Escrever(90, 9.3, 'corpo', '0 / 4 pngs', 'preto', 'direita')

score_0 = Escrever(10.1, 12, 'corpo', 'Score Maximo:', 'preto')
score_1 = Escrever(90, 12, 'corpo', '000000000 pts.', 'preto', 'direita')

dinheiro_0 = Escrever(50, 15.5, 'titulo', 'Zenys:', 'preto')
dinheiro_1 = Escrever(93, 15.5, 'titulo', '000000000 z', 'preto', 'direita')