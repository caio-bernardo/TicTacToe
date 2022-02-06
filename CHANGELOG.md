# CHANGELOG
Toda e qualquer alteração no projeto será documentada neste arquivo.
===
## [NãoPublicado]
### [Adicionado]
- [ ] Refatoração do arquivo main
- [ ] Criação de testes
- [ ] Modo Single Player
- [ ] Arquivo .exe para download do jogo

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

[0.1.0]: https://github.com/caio-bernardo/TicTacToe/compare/main...game-v.2.0
