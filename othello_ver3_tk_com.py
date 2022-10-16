import random
import tkinter as tk
from othello_ver2_tkinter import OthelloVer2


class OthelloVer3(OthelloVer2):
    def __init__(self):
        super().__init__()
        self.player1 = None
        self.player2 = None
        self.com1 = None
        self.com2 = None

    def set_player_and_com(self):
        "playerとcomを先手、後手にセットする"
        def com_or_player(num):
            "先手に１、後手に-1をセット"
            if num == 1:
                self.player1 = 1
                self.com1 = -1
            if num == 2:
                self.com1 = 1
                self.player1 = -1
            if num == 3:
                self.com1 = 1
                self.com2 = -1
            if num == 4:
                self.player1 = 1
                self.player2 = -1
            question.destroy()
        question = tk.Tk()
        f = tk.Frame(question)
        f.grid()
        question.title("START GAME")
        button_f = tk.Button(f, text="YOU FIRST", height=4, width=6,
                             command=lambda: com_or_player(1))
        button_s = tk.Button(f, text="COM FIRST", height=4, width=6,
                             command=lambda: com_or_player(2))
        button_allcom = tk.Button(
            f, text="ALL COM", height=4, width=6,
            command=lambda: com_or_player(3))
        button_noncom = tk.Button(
            f, text="NO COM", height=4, width=6,
            command=lambda: com_or_player(4))
        button_f.grid(row=1, column=1)
        button_s.grid(row=1, column=2)
        button_allcom.grid(row=1, column=3)
        button_noncom.grid(row=1, column=4)
        f.mainloop()

    def show_result(self, board):
        "結果をmessage boxで示す"
        result = self.check_gameover_or_continue(board)
        if result != 4:
            if result == 1:
                player = "先手の勝利"
            elif result == 2:
                player = "後手の勝利"
            elif result == 3:
                player = "引き分け"
            self.canvas.create_text(
                140, 560, text=player,
                anchor="nw", font=("HG丸ｺﾞｼｯｸM-PRO", 70))

    def click_com(self, event):
        "マス目をクリックした後の流れ(x,y)を入力してからの流れ全てをcomを絡めて行う"
        y = event.x
        x = event.y
        x = x // 70
        y = y // 70
        if self.possible_squares_list(self.turn, self.board) == []:
            self.turn *= -1
            self.turn_yellow(self.canvas, self.turn, self.board, 8, 8)
        else:
            if self.turn == self.com1 or self.turn == self.com2:
                x, y = random.choice(
                    self.possible_squares_list(self.turn, self.board))
            elif self.turn == self.player1 or self.turn == self.player2:
                pass
            if (x, y) in self.possible_squares_list(self.turn, self.board):
                self.put_a_piece(x, y, self.turn, self.board)
                self.put_or_turn_all_stones_on_canvas(self.canvas, self.board)
                self.turn *= -1
                self.turn_yellow(self.canvas, self.turn, self.board, x, y)
        self.show_my_turn(self.my_turn, self.turn, self.canvas)
        self.show_result(self.board)

    def main_ver3_tk_com(self):
        "comとの対戦をgui上で楽しむ"
        self.set_player_and_com()
        self.make_board_tkinter()
        self.init_board(self.board)
        self.put_or_turn_all_stones_on_canvas(self.canvas, self.board)
        self.turn_yellow(self.canvas, self.turn, self.board, 8, 8)
        self.canvas.bind('<ButtonPress>', self.click_com)
        self.app.mainloop()


if __name__ == '__main__':
    othe = OthelloVer3()
    othe.main_ver3_tk_com()
