"""
- TODO Make the Single Player Mode
- TODO Get away of the spagheti code
"""

from functools import partial
from tkinter import *
from tkinter import messagebox


class TwoPlayer:
    def __init__(self, game_board: Tk) -> None:
        game_board.destroy()
        self.game_board = Tk()
        self.game_board.title('Tic Tac Toe')

        self.board_replica = [[" " for c in range(3)] for i in range(3)]

        self.l1 = Button(self.game_board, text = "Player 1 : X", width = 10)
        self.l1.grid(row = 1, column = 2)

        self.l2 = Button(self.game_board, text = "Player 2 : O", 
                    width = 10, state = DISABLED)
        self.l2.grid(row = 2, column = 2)

        self.board()

    # 3 rows and 3 colums of buttons
    def board(self):
        global button
        button = []
        for r in range(3):
            m = r + 3
            button.append(r)
            button[r] = []
            for c in range(3): 
                button[r].append(c)
                get_t = partial(self.get_text, r, c)
                button[r][c] = Button(self.game_board, command=get_t, height=5, width=10,
                    bd=5)
            n = c + 1
            button[r][c].grid(row=m, column=n)
         
    def check_player_time(self):
        l1_state = str(self.l1["state"])
        l2_state = str(self.l2["state"])
        if l1_state == 'normal' or l1_state == 'active':
            return 'X'
        elif l2_state == 'normal' or l2_state == 'active':
            return 'O'
        else:
            print(str(self.l1["state"]))
            raise TypeError('No button is ACTIVE')

    def get_text(self, r, c):
        sign = self.check_player_time()
        if self.isfree(r, c):
            if sign == 'X':
                self.l1.config(state=DISABLED)
                self.l2.config(state=ACTIVE)
                self.board_replica[r][c] = sign

            elif sign == 'O':
                self.l1.config(state=ACTIVE)
                self.l2.config(state=DISABLED)
                self.board_replica[r][c] = sign

            button[r][c].config(text=self.board_replica[r][c])

        if self.winner(self.board_replica, "X"):
            self.game_board.destroy()
            box = messagebox.showinfo('Winner', 'Player X wins!')
        elif self.winner(self.board_replica, 'O'):
            self.game_board.destroy()
            box = messagebox.showinfo('Winner', 'Player O wins!')
        elif self.isfull():
            self.game_board.destroy()
            box = messagebox.showinfo('Tie Game', 'Tie Game!')

    def winner(self, b, sign):
	    return ((b[0][0] == sign and b[0][1] == sign and b[0][2] == sign) or
				(b[1][0] == sign and b[1][1] == sign and b[1][2] == sign) or
				(b[2][0] == sign and b[2][1] == sign and b[2][2] == sign) or
				(b[0][0] == sign and b[1][0] == sign and b[2][0] == sign) or
				(b[0][1] == sign and b[1][1] == sign and b[2][1] == sign) or
				(b[0][2] == sign and b[1][2] == sign and b[2][2] == sign) or
				(b[0][0] == sign and b[1][1] == sign and b[2][2] == sign) or
				(b[0][2] == sign and b[1][1] == sign and b[2][0] == sign))

    def isfull(self):
        for c in self.board_replica:
            if c.count(' ') > 0:
                return False
        return True

    def isfree(self, r, c):
        return self.board_replica[r][c] == " "


class SinglePlayer:
    def __init__(self, game_board: Tk) -> None:
        game_board.destroy()
        self.game_board = Tk()
        self.game_board.title('Tic Tac Toe')

        self.board_replica = [[" " for c in range(3)] for i in range(3)]

        self.l1 = Button(self.game_board, text = "Player 1 : X", width = 10)
        self.l1.grid(row = 1, column = 2)

        self.l2 = Button(self.game_board, text = "Player 2 : O", 
                    width = 10, state = DISABLED)
        self.l2.grid(row = 2, column = 2)

        self.board()

    # 3 rows and 3 colums of buttons
    def board(self):
        global button
        button = []
        for r in range(3):
            m = r + 3
            button.append(r)
            button[r] = []
            for c in range(3): 
                button[r].append(c)
                get_t = partial(self.get_text, r, c)
                button[r][c] = Button(self.game_board, command=get_t, height=5, width=10,
                    bd=5)
            n = c + 1
            button[r][c].grid(row=m, column=n)
         
    def check_player_time(self):
        l1_state = str(self.l1["state"])
        l2_state = str(self.l2["state"])
        if l1_state == 'normal' or l1_state == 'active':
            return 'X'
        elif l2_state == 'normal' or l2_state == 'active':
            return 'O'
        else:
            print(str(self.l1["state"]))
            raise TypeError('No button is ACTIVE')

    def get_text(self, r, c):
        sign = self.check_player_time()
        if self.isfree(r, c):
            if sign == 'X':
                self.l1.config(state=DISABLED)
                self.l2.config(state=ACTIVE)
                self.board_replica[r][c] = sign

            elif sign == 'O':
                self.l1.config(state=ACTIVE)
                self.l2.config(state=DISABLED)
                self.board_replica[r][c] = sign

            button[r][c].config(text=self.board_replica[r][c])

        if self.winner(self.board_replica, "X"):
            self.game_board.destroy()
            box = messagebox.showinfo('Winner', 'Player X wins!')
        elif self.winner(self.board_replica, 'O'):
            self.game_board.destroy()
            box = messagebox.showinfo('Winner', 'Player O wins!')
        elif self.isfull():
            self.game_board.destroy()
            box = messagebox.showinfo('Tie Game', 'Tie Game!')

    def winner(self, b, sign):
	    return ((b[0][0] == sign and b[0][1] == sign and b[0][2] == sign) or
				(b[1][0] == sign and b[1][1] == sign and b[1][2] == sign) or
				(b[2][0] == sign and b[2][1] == sign and b[2][2] == sign) or
				(b[0][0] == sign and b[1][0] == sign and b[2][0] == sign) or
				(b[0][1] == sign and b[1][1] == sign and b[2][1] == sign) or
				(b[0][2] == sign and b[1][2] == sign and b[2][2] == sign) or
                (b[0][0] == sign and b[1][1] == sign and b[2][2] == sign) or
                (b[0][2] == sign and b[1][1] == sign and b[2][0] == sign))

    def isfull(self):
        for c in self.board_replica:
            if c.count(' ') > 0:
                return False
        return True

    def isfree(self, r, c):
        return self.board_replica[r][c] == " "


class Play:
   def __init__(self) -> None: 
      self.menu = Tk()
      self.menu.geometry("300x300")
      self.menu.title('Tic Tac Toe Game')

      self.singleplayer = partial(SinglePlayer, self.menu)
      self.twoplayer = partial(TwoPlayer, self.menu)

      self.label_title = Label(self.menu, text='Tic Tac Toe', font='Arial 16',
       pady=10)

      self.label_select_mode = Label(self.menu, text='Select a Game Mode',
       font='Arial 12', pady=5)

      self.btn_sp = Button(self.menu, text='SinglePlayer', 
        command=self.singleplayer,width='200')

      self.btn_twop = Button(self.menu, text='Two Players',
       command=self.twoplayer, width='200')

      self.btn_exit = Button(self.menu, text='Exit', command=self.menu.quit,
       width='200')

      self.set_layout()

   def set_layout(self):
      self.label_title.pack(side='top')
      self.label_select_mode.pack(side='top')
      self.btn_sp.pack(side='top')
      self.btn_twop.pack(side='top')
      self.btn_exit.pack(side='top')

   def start(self):
      self.menu.mainloop()


if __name__ == "__main__":
   win = Play()
   win.start()
