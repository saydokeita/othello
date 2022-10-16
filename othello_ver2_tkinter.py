import tkinter as tk
import tkinter.messagebox
from othello_ver1_kihu import OthelloVer1


class OthelloVer2(OthelloVer1):
    def __init__(self):
        super().__init__()

    def make_board_tkinter(self):

        "ボードを作成する "
        self.app = tk.Tk()
        self.app.title("OTHELLO")
        self.canvas = tk.Canvas(self.app, width=560, height=630)
        self.canvas.pack()
        # マス目の作成
        for i in range(8):
            for j in range(8):
                tag_name = "square"+str(i) + "," + str(j)
                self.a = self.canvas.create_rectangle(
                    j*70, i*70, 70+j*70, 70 + i*70,
                    fill="green", outline="white", tag=tag_name)
        # 手番の表示
        self.my_turn = self.canvas.create_oval(
            7, 567, 63, 627, fill="black", outline="black", tag="my_stone")

    def put_or_turn_all_stones_on_canvas(self, canv, board):
        "棋譜情報をcanvasに反映させる"
        for x in range(8):
            for y in range(8):
                if board[x][y] == 1:
                    canv.create_oval(y*70+7, x*70+7, 63+y*70, 63+x*70,
                                     fill="black", outline="black")
                elif board[x][y] == -1:
                    canv.create_oval(y*70+7, x*70+7, 63+y*70, 63+x*70,
                                     fill="white", outline="black")

    def turn_yellow(self, canv, t, board, x, y):
        "ターンtにboardの配置可能な場所をcanvasに黄色で示し、x,yはオレンジで示す"
        for i in range(8):
            for j in range(8):
                tag_name = "square"+str(i) + "," + str(j)
                if (i, j) in self.possible_squares_list(t, board):
                    canv.itemconfig(tag_name, fill="yellow")
                else:
                    canv.itemconfig(tag_name, fill="green")
        if x < 8:
            put_tag_name = "square"+str(x) + "," + str(y)
            canv.itemconfig(put_tag_name, fill="orange")

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
            tkinter.messagebox.askyesno(message=player)

    def show_my_turn(self, my_turn, t, canv):
        "現在のターンtをcanv上の碁石my_turnの色で示す"
        if t == 1:
            canv.itemconfig(my_turn, fill="black")
        if t == -1:
            canv.itemconfig(my_turn, fill="white")

    def click(self, event):
        "マス目をクリックした後の流れ(x,y)を入力してからの流れ全てを行う"
        y = event.x
        x = event.y
        x = x // 70
        y = y // 70
        if self.possible_squares_list(self.turn, self.board) == []:
            self.turn *= -1
            self.turn_yellow(self.canvas, self.turn, self.board, 8, 8)
        elif (x, y) in self.possible_squares_list(self.turn, self.board):
            self.put_a_piece(x, y, self.turn, self.board)
            self.put_or_turn_all_stones_on_canvas(self.canvas, self.board)
            self.turn *= -1
            self.turn_yellow(self.canvas, self.turn, self.board, x, y)
        self.show_my_turn(self.my_turn, self.turn, self.canvas)
        self.show_result(self.board)

    def main_ver2_tkinter(self):
        "gui上でオセロを楽しむ"
        self.make_board_tkinter()
        self.init_board(self.board)
        self.put_or_turn_all_stones_on_canvas(self.canvas, self.board)
        self.turn_yellow(self.canvas, self.turn, self.board, 8, 8)
        self.canvas.bind('<ButtonPress>', self.click)
        self.app.mainloop()


if __name__ == '__main__':
    othello = OthelloVer2()
    othello.main_ver2_tkinter()
