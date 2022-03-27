# TicTacToe
[![GitHub license](https://img.shields.io/github/license/caio-bernardo/TicTacToe?style=for-the-badge)](https://github.com/caio-bernardo/TicTacToe/blob/main/LICENSE)
![Status do Projeto](https://img.shields.io/badge/status-finalizado-brightgreen?style=for-the-badge) 
[![GitHub stars](https://img.shields.io/github/stars/caio-bernardo/TicTacToe?style=for-the-badge)](https://github.com/caio-bernardo/TicTacToe/stargazers)  
Um jogo de video game do clássico Jogo da Velha para desktop.

![main window](images/image1.png) 

## Indice
[Sobre](#sobre) &#8226; [Recursos](#recursos) &#8226; [Tecnologias](#tecnologias) &#8226; [Uso](#uso) &#8226; [Acesso a código](#acesso-ao-código)

## Sobre
 O jogo conta com dois modos, dois jogadores, *TwoPlayer*, ou jogador contra máquina, *Single Player*.

## Recursos
- [x] Modo de jogo Single Player.
- [x] Modo de jogo Two Player.
- [x] Resultado do jogo de forma personalizada.
- [x] Instalador do jogo.

![board window](images/image3.png)
![result x window](images/image6.png)  
![result tie window](images/image4.png) 
 
## Tecnologias
* Python 3.10
* PyQt5
* PyInstaller

## Uso
* Baixe o instalador [clicando aqui](tictactoe-installer.exe) e em Download.
* Prossiga até que o jogo seja instalado.  
![installer picture1](images/image8.png)
![installer picture2](images/image9.png)
![installer picture3](images/image10.png)
* Por fim pesquise na sua barra de busca e abra o jogo.
![search picture](images/image2.png)

## Acesso ao código
* Clone este repositório.   
` git clone https://github.com/caio-bernardo/TicTacToe.git`
> Você também pode fazer isso pelo GitHub Desktop ou baixar os arquivos manualmente.
* Baixe as dependências do projeto.  
`$ pip install -r requirements`

> Para executar o projeto
* Execute o arquivo run.py.  
`$ python run.py`
* Ou importe a função `start`
~~~ 
from game import start
start()
~~~
