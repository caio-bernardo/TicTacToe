# TicTacToe
[![GitHub license](https://img.shields.io/github/license/caio-bernardo/TicTacToe)](https://github.com/caio-bernardo/TicTacToe/blob/main/LICENSE)
![Status do Projeto](https://img.shields.io/badge/status-desenvolvimento-brightgreen)  
Um jogo de video game do clássico Jogo da Velha para desktop.

## Indice
[Sobre](#sobre) &#8226; [Features](#features) &#8226; [Tecnologias e Ferramentas usadas](#tecnologias-e-ferramentas-usadas) &#8226; [Versão](#vers%C3%A3o) &#8226; [Pré-requisitos](#pr%C3%A9-requisitos) &#8226; [Instruções de uso](#instru%C3%A7%C3%B5es-de-uso)

## Sobre
 O jogo conta com dois modos, dois jogadores, *TwoPlayer*, ou jogador contra máquina, *Single Player*.

## Features
- [x] Modo de jogo Single Player.
- [x] Modo de jogo Two Player.
- [x] Resultado do jogo de forma personalizada.
- [ ] Instalador do jogo.
 
## Tecnologias e Ferramentas usadas
* Qt Designer
* PyQt5
 
## Versão
A versão atual é a [1.0.0-rc1](CHANGELOG.md/#100-rc1---20220219), saiba mais em [CHANGELOG](CHANGELOG.md)

## Pré-requisitos
* Python instalado
* PyQt5 instalado
* Uma IDE para rodar o código, ex.: Visual Studio Code
> Nota: Isto é apenas um *placeholder*, a versão final contará com um arquivo executavél.

## Instruções de uso
* Clone este repositório. 
` git clone https://github.com/caio-bernardo/TicTacToe.git`
> Você também pode fazer isso pelo GitHub Desktop ou baixar os arquivos manualmente.
* Baixe as dependências do projeto.
`pip install -r requirements`
* Crie um arquivo.py e importe a função [*start*](game/__init__.py) dentro da pasta game, assim como no exemplo abaixo.  
~~~
import game
game.start()
~~~  
> Nota: Isto é apenas um *placeholder*, a versão final contará com um instalavel.
