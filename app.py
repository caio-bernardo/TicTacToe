"""

- Create a landing page containing selection buttons: Single-player or 
   multiplayer.
- Create a game-board containing nine tiles to play the game along with other 
   details (i.e. playing with a system or another player, whose turn etc.).
- Allow the player to press the tile and check the status of the game (i.e. Tie
   game, anyone of the players won the match or the game is still running).
- Display the message, who won the match.
"""

from functools import partial
from tkinter import *


class TwoPlayer:
   def __init__(self, game_board: Tk) -> None:
      game_board.destroy()


class SinglePlayer:
   def __init__(self, game_board: Tk) -> None:
      game_board.destroy()


class Play:
   def __init__(self) -> None: 
      self.menu = Tk()
      self.menu.geometry("300x300")
      self.menu.title('Tic Tac Toe Game')

      self.btn_sp = Button(self.menu, text='Single Player', width='200')

      self.btn_twop = Button(self.menu, text='Two Players', width='200')

      self.btn_exit = Button(self.menu, text='Exit', command=self.menu.quit,
       width='200')

      self.btn_sp.pack(side='top')
      self.btn_twop.pack(side='top')
      self.btn_exit.pack(side='top')


   def start(self):
      self.menu.mainloop()


if __name__ == "__main__":
   win = Play()
   win.start()
