import pygame
import sys

sys.path.append('D:/Vini/Projetos/004 - RDC')

from modulos.segmentacao import *
from modulos.setores.a_pagina_inicial.inicio import *
from modulos.setores.a_pagina_inicial.opcoes_ext.opcoes_classes import *

# variaveis:
caixa_confirmadora_sfx = CaixaConfirmadora(11.3, 75.9)
texto_sfx = Escrever(20, 75.9, 'corpo', 'SFX', 'preto')
barra_intensidade_seta_menor_sfx = BDISetas(32, 75.6, 'menor')
barra_intensidade_esteira_sfx = BDIEsteira(35.3, 75.9)
barra_intensidade_seta_maior_sfx = BDISetas(85.5, 75.6, 'maior')
esfera_marcadora_sfx = EsferaMarcadora(50, 75.6)

caixa_confirmadora_efeitos = CaixaConfirmadora(11.3, 81.8)
texto_efeitos = Escrever(20, 81.8, 'corpo', 'Efeitos', 'preto')

botao_ok = Botao(80.5, 88.6, 'curto')
texto_ok = Escrever(83.4, 89.5, 'corpo', 'OK', 'preto')