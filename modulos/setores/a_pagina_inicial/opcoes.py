import pygame, sys

sys.path.append('/storage/emulated/0/RDC')

from modulos.classes import *

# variaveis:
janela_opcoes = ExibirImagem('modulos/setores/a_pagina_inicial/opcoes_ext/janela_opcoes.png', 920, 539, 7.4, 66.6)
texto_opcoes = Escrever(9.4, 67.6, 'titulo', 'Opcoes', 'preto')

caixa_confirmadora_bgm = ExibirImagemInterativa('modulos/setores/a_pagina_inicial/opcoes_ext/caixa_marcada.png', 'modulos/setores/a_pagina_inicial/opcoes_ext/caixa_nao_marcada.png', 35, 35, 11.3, 71.6)
texto_bgm = Escrever(20, 71.6, 'corpo', 'BGM', 'preto')
barra_intensidade_seta_menor_bgm = ExibirImagem('modulos/setores/a_pagina_inicial/opcoes_ext/barra_intensidade_menor.png', 35, 46, 32.1, 71.2)
barra_intensidade_esteira_bgm = ExibirImagem('modulos/setores/a_pagina_inicial/opcoes_ext/barra_intensidade_esteira.png', 542, 32, 35.3, 71.6)
barra_intensidade_seta_maior_bgm = ExibirImagem('modulos/setores/a_pagina_inicial/opcoes_ext/barra_intensidade_maior.png', 35, 46, 85.5, 71.2)
esfera_marcadora_bgm = ExibirImagem('modulos/setores/a_pagina_inicial/opcoes_ext/esfera_marcadora.png', 27, 32, 50, 71.6)

caixa_confirmadora_sfx = ExibirImagemInterativa('modulos/setores/a_pagina_inicial/opcoes_ext/caixa_marcada.png', 'modulos/setores/a_pagina_inicial/opcoes_ext/caixa_nao_marcada.png', 35, 35, 11.3, 75.9)
texto_sfx = Escrever(20, 75.9, 'corpo', 'SFX', 'preto')
barra_intensidade_seta_menor_sfx = ExibirImagem('modulos/setores/a_pagina_inicial/opcoes_ext/barra_intensidade_menor.png', 35, 46, 32.1, 75.5)
barra_intensidade_esteira_sfx = ExibirImagem('modulos/setores/a_pagina_inicial/opcoes_ext/barra_intensidade_esteira.png', 542, 32, 35.3, 75.9)
barra_intensidade_seta_maior_sfx = ExibirImagem('modulos/setores/a_pagina_inicial/opcoes_ext/barra_intensidade_maior.png', 35, 46, 85.5, 75.5)
esfera_marcadora_sfx = ExibirImagem('modulos/setores/a_pagina_inicial/opcoes_ext/esfera_marcadora.png', 27, 32, 50, 75.9)


caixa_confirmadora_efeitos = ExibirImagemInterativa('modulos/setores/a_pagina_inicial/opcoes_ext/caixa_marcada.png', 'modulos/setores/a_pagina_inicial/opcoes_ext/caixa_nao_marcada.png', 35, 35, 11.3, 81.8)
texto_efeitos = Escrever(20, 81.8, 'corpo', 'Efeitos', 'preto')

botao_ok = ExibirImagem('modulos/setores/a_pagina_inicial/opcoes_ext/botao_curto.png', 106, 69, 80.5, 88.6)
texto_ok = Escrever(83.4, 89.5, 'corpo', 'OK', 'preto')

# funcoes:
def desenho_pagina_opcoes():
    janela_opcoes.desenho()
    texto_opcoes.desenho()

    caixa_confirmadora_bgm.desenho()
    texto_bgm.desenho()
    barra_intensidade_seta_menor_bgm.desenho()
    barra_intensidade_esteira_bgm.desenho()
    barra_intensidade_seta_maior_bgm.desenho()
    esfera_marcadora_bgm.desenho()

    caixa_confirmadora_sfx.desenho()
    texto_sfx.desenho()
    barra_intensidade_seta_menor_sfx.desenho()
    barra_intensidade_esteira_sfx.desenho()
    barra_intensidade_seta_maior_sfx.desenho()
    esfera_marcadora_sfx.desenho()

    caixa_confirmadora_efeitos.desenho()
    texto_efeitos.desenho()

    botao_ok.desenho()
    texto_ok.desenho()

if __name__ == '__main__':
    pass