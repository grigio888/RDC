import pygame
import sys

sys.path.append('D:/Vini/Projetos/004 - RDC')

from modulos.segmentacao import *
from modulos.setores.a_pagina_inicial.inicio import *
from modulos.setores.a_pagina_inicial.opcoes_ext.opcoes_classes import *

# variaveis:
janela_opcoes = JanelaOpcoes(7.4, 66.6)
texto_opcoes = Escrever(9.4, 67.6, 'titulo', 'Opcoes', 'preto')

caixa_confirmadora_bgm = CaixaConfirmadora(11.3, 71.6)
texto_bgm = Escrever(20, 71.6, 'corpo', 'BGM', 'preto')
barra_intensidade_seta_menor_bgm = BDISetas(32, 71.3, 'menor')
barra_intensidade_esteira_bgm = BDIEsteira(35.3, 71.6)
barra_intensidade_seta_maior_bgm = BDISetas(85.5, 71.3, 'maior')
esfera_marcadora_bgm = EsferaMarcadora(50, 71.7)