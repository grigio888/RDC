import pygame
import sys

sys.path.append('C:/Users/Pri e Vini/Desktop/Projetos/004 - RDC')

from modulos.segmentacao import *
from modulos.classes import *

pygame.init()

texto_loading = Escrever(9, 65.6, 'titulo', 'Loading', 'preto')

def desenho_pagina_loading():
    fundo.desenho()

    janela_inicio.desenho()
    texto_loading.desenho()
