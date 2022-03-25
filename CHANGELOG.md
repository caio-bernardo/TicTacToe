# CHANGELOG
Toda e qualquer alteração no projeto será documentada neste arquivo.
 
## [NãoPublicado] 
### [EmBreve]
- [ ] Arquivo .exe para download do jogo
- [ ] Melhoras na performace
- [ ] Refatoração de código mal desenvolvido

## [1.0.0] - 2022/03/25
###
 
## [1.0.0-rc1] - 2022/02/19
### [Adicionado]
* Nova classe Enum [GameMode](game/src/tools.py/) define os modos de jogo.
* Documentação apropriada.
* Novo arquivo [requiriments](requeriments.txt), contém as dependências do projeto.
* Novo tópico [Tecnologias e Ferramentas usadas](README.md/#tecnologias-e-ferramentas-usadas)] adicionado ao README.md
* Novos métodos *player_mode*, *computer_mode* em [window](game/src/window.py). Responsáveis por alterar os botões na grade.
* Novos métodos *go_to_board_page_n_singleplayer* e *go_to_board_page_n_twoplaye*. Responsáveis por definir o modo de jogo.
* Novos método *has_game_finished*. Responsável por verificar e encerrar o jogo caso ele esteja terminado.
* Novo método *change_player*. Responsável por alterar para o próximo jogador após um fim de turno.

### [Modificado]
* [Instruções de uso](README.md/#instru%C3%A7%C3%B5es-de-uso) agora conta com as dependências do projeto e melhor explicação.
* Nota no fim das instruções alterada de *arquivo executalvel* para *instalavel*.
* Agora os botões [*btn_p1*](game/src/window.py) e [*btn_p2*](game/src/window.py) da página principal usam os métodos *go_to_board_page_n_singleplayer* e *go_to_board_page_n_twoplaye*, respectivamente.
* Objeto de *GameState* transferido da função *go_to_board_page* para *has_game_finished*.
* Método *write_on_board* renomeado para [*run_a_turn*](game/src/window.py). Agora o método apenas reune e executa outros métodos.
 
### [Corrigido]
* Agora o link da versão *0.3.0* contém a url correta.
* Objeto de *GameState* agora atualiza o atributo *player* corretamente.
* Ordem de prioridade de *ComputerMove* alterada. Antes ele priorizava arruinar uma vitória do adversário ou invés de uma vitória, agora a prioridade foi invertida.
* Type Hint adicionado a alguns métodos.

## [0.3.0] - 2022/02/18
### [Adicionado]
* Modo Single Player
* Classe *ComputerMove*, que escolhe um local na grade e joga contra o usuário.
* Novos métodos que definem o modo de jogo
* Tupla com os botões da grade
* Novo método *computer_move* que joga contra o jogador

### [Removido]
* *setter* da classe *Player* ( o método swap o substitui)
* classe *Button*
 
### [Modificado]
* o método *check_4_winner* agora tem sua própria classe
* O texto dos botões da grade são reiniciados por um loop.

## [0.2.1] - 2022/02/09
### [Corrigido]
* Mudanças no CHANGELOG, agora as versões redirecionam para comparação entre versões de forma correta.

## [0.2.0] - 2022/02/08
### [Adicionado]
* Arquivo [tools](game/src/tools.py) contém funcionalidades da interface
* Classes (Board, Player, GameSate, Results) adicionadas ao arquivo [tools](game/src/tools.py), essas classes excercem funcionalidades sobre o arquivo [window](game/src/window.py)
* Função [start](game/__init__.py) inicia a jogo.

### [Removido]
* Arquivos __init__.py desnecessários nas pastas [interface](game/interface/) e [src](game/src/)

### [Modificado]
* Arquivo *src/main* renomeado para [window](game/src/window.py)
* O arquivo [window](game/src/window.py) agora conta apenas com funções destinadas a aspectos visuais e a interface
* Mudanças na forma de iniciar o jogo. Saiba mais em [README](README.md/#instru%C3%A7%C3%B5es-de-uso).

### [Corrigido]
* Problemas de importação de modulos
* Um erro de digitação no arquivo [README](README.md), o número da versão estava "1.0.1".


## [0.1.0] - 2022/02/06
### [Adicionado]
* O pacote [game](game), contém todos os arquivos do projeto.
* Pasta [images](game/images), contém todas as imagens e o arquivo [resource.qrc](game/images/resource.qrc), que permite o acesso as imagens.
* Arquivo [game_gui.ui](game/interface/game_gui.ui), criado pelo Qt Designer e compilado em XML.
* Arquivo [resource.py](game/interface/rcc/resource.py), permite o acesso as imagens pelo game_gui.
* Arquivo [game_gui.py](game/interface/uic/game_gui.py), a interface gráfica em linguagem Python
* Arquivo [main.py](game/src/main.py), contém as funcionalidades da interface.
* O arquivo [__init__.py](game/__init__.py) da pasta game permite a execução do código
> Nota: Isto é um placeholder

### [Modificado]
- Reestruturação e reorganização do projeto.
> Referente a substituição da biblioteca Tkinter pelo PyQt5;
> Além da organização do projeto no pacote game

### [Removido]
- Arquivo app.py

[EmBreve]: https://github.com/caio-bernardo/TicTacToe/compare/v1.0.0-rc1...HEAD
[1.0.0-rc1]: https://github.com/caio-bernardo/TicTacToe/compare/v0.3.0...v1.0.0-rc1
[0.3.0]: https://github.com/caio-bernardo/TicTacToe/compare/v0.2.1...v0.3.0
[0.2.1]: https://github.com/caio-bernardo/TicTacToe/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/caio-bernardo/TicTacToe/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/caio-bernardo/TicTacToe/compare/main...game-v.2.0
