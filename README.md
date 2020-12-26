# RDC
Segundo projeto que estou usando para escalabilidade de codigos em um programa de porte grande.


----------------------------------------------------------------------------------------------

Change Logs:

26/12/20:
- Adicionado janela Extras.
- Adicionado esqueleto para a função de registro de contas.

- Tela de opções acessada somente após o login.



25/12/20:
- Adicionada (parcial) integração com banco de dados MySQL.
- Adicionado tela de login com autenticadores.
- Adicionado funcionalidade 'Full Screen', mas apenas experimental (ocasiona má renderização de basicamente tudo.).

- Melhorado o modo como as posições das janelas são renderizadas.
- Melhorado o modo como a reescala das imagens são feitas, sendo menos dependes de ajuste manual de renderização.

- Removido opcoes da tela inicial (LogOn) para ser adicionado um menu de extras (com opções de registro).

Obs.: A demora entre o commit anterior e esse é por estar aprendendo sql.



09/11/20:
- Adicionado interações (For, Agi, Vit, Int, Des e Sor) nos menus, se atentando ao gasto de atributos.
- As tabelas de caracteriscas se atualizam conforme adicionado pontos na distribuição de atributos.
- Adicionado função de Escrever Nome.



08/11/20:
- Adicionado interações com o menu de opções na Landing Page.
- Adicionado Opções através do menu de landing page.
- Adicionado interações com os frames de personagens (aparecem a opção de criar caso o mouse/touch passe em cima).
- Adicionado o modelo de janela para criação de personagens.



04/11/20:
- Corrigido transição da tela inicial para à de opções (loading 0.1s)
- Corrigido transição da tela inicial para à Landing Page (loading 0.3s)
- Varias outras otimizações menores e gerenciamento de dados.

Me deparei com diversos problemas de otimização de código, com esperas de até 10s nos smarphones.
Corrigido o problema, loadings praticamente instataneos agora.



25/10/20:
- Continuando a escrita.



24/10/20:
- Continuando a escrita.



22/10/20:
- Continuando a escrita.



21/09/20:
- Criado tela de inicio (Com bgm, sfx e interacoes).
- Criado tela de opcoes iniciais (as caixas confirmadoras e esteiras ainda nao possuem suas atribuidas).
- Criado tela de loading (transicao) (tenho que aprender um modo de carregar os modulos somente quando for preciso, deixando o programa mais leve e rapido).
- Tela de landing page em construcao.
