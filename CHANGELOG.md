# CHANGELOG
Toda e qualquer alteração no projeto será documentada neste arquivo.
## [NãoPublicado]
### [EmBreve]
- [ ] Criação de testes
- [ ] Modo Single Player
- [ ] Arquivo .exe para download do jogo
- [ ] Melhoras na performace

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

[0.2.1]: https://github.com/caio-bernardo/TicTacToe/compare/v0.1.0...v0.2.0
[0.2.0]: https://github.com/caio-bernardo/TicTacToe/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/caio-bernardo/TicTacToe/compare/main...game-v.2.0
