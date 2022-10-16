"""棋譜と手番を渡されたら、最善手を考えるAIもどきの関数の作成"""
import copy
import random
import tkinter as tk
from othello_ver3_tk_com import OthelloVer3


class OthelloVer4(OthelloVer3):
    def __init__(self):
        super().__init__()
        self.com1_level = self.com_random_level0
        self.com2_level = self.com_random_level0

    def count_board(self, t, board):
        board2 = []
        for i in board:
            for j in i:
                board2.append(j)
        count = board2.count(t)
        return count

    def all_choice_count_dict(self, t1, t2, board):
        """ターンt1、boardにおいて、全ての置き方に対するt2の石の数の辞書型リスト"""
        possible_squares_lists = self.possible_squares_list(t1, board)
        dict_put_choice = {}
        for i, choice in enumerate(possible_squares_lists):
            x, y = choice
            temporary_board = copy.deepcopy(board)
            self.put_a_piece(x, y, t1, temporary_board)
            dict_put_choice[possible_squares_lists[i]] = self.count_board(
                t2, temporary_board)
            self.exception_mean(dict_put_choice, board)
        return dict_put_choice

    def max_choice(self, dict):
        """辞書型リストからValue最大となるkeyを返す"""
        max_choice = max(dict, key=dict.get)
        return max_choice

    def dict_mean(self, dict):
        """辞書型リストのValueの平均値を求める.
        もしリストが空なら、100を返す"""
        if len(dict) == 0:
            return 100
        else:
            mean = sum(dict.values()) / len(dict)
            return mean

    def com_best_choice_level1(self, t, board):
        all_choice_dict = self.all_choice_count_dict(t, t, board)
        max = self.max_choice(all_choice_dict)
        return max

    def come_best_choice_level2(self, t, board):
        possible_squares_lists = self.possible_squares_list(t, board)
        dict_put_choice = {}
        for choice in possible_squares_lists:
            x, y = choice
            temporary_board = copy.deepcopy(board)
            self.put_a_piece(x, y, t, temporary_board)
            choice_dict = self.all_choice_count_dict(-t, t, temporary_board)
            choice_mean = self.dict_mean(choice_dict)
            dict_put_choice[choice] = choice_mean
        max = self.max_choice(dict_put_choice)
        return max

    def come_best_choice_level3(self, t, board):
        possible_squares_lists = self.possible_squares_list(t, board)
        dict_put_choice = {}
        for choice in possible_squares_lists:
            x, y = choice
            temporary_board = copy.deepcopy(board)
            self.put_a_piece(x, y, t, temporary_board)
            possible_squares_lists2 = self.possible_squares_list(
                -t, temporary_board)
            dict_put_choice2 = {}
            for choice2 in possible_squares_lists2:
                x2, y2 = choice2
                temporary_board2 = copy.deepcopy(temporary_board)
                self.put_a_piece(x2, y2, -t, temporary_board2)
                choice_dict = self.all_choice_count_dict(
                    t, t, temporary_board2)
                choice_mean2 = self.dict_mean(choice_dict)
                dict_put_choice2[choice2] = choice_mean2
            self.exception_mean(dict_put_choice2, temporary_board)
            choice_mean = self.dict_mean(dict_put_choice2)
            dict_put_choice[choice] = choice_mean
        self.exception_mean(dict_put_choice, self.board)
        print(dict_put_choice)
        max = self.max_choice(dict_put_choice)
        return max

    def exception_mean(self, dict, board):
        if (0, 0) in dict:
            dict[(0, 0)] = 99
        if (7, 0) in dict:
            dict[(7, 0)] = 99
        if (7, 7) in dict:
            dict[(7, 7)] = 99
        if (0, 7) in dict:
            dict[(0, 7)] = 99
        if board[0][0] == 0:
            if (0, 1) in dict:
                dict[(0, 1)] = 1
            if (1, 0) in dict:
                dict[(1, 0)] = 1
            if (1, 1) in dict:
                dict[(1, 1)] = 1
        if board[0][7] == 0:
            if (0, 6) in dict:
                dict[(0, 6)] = 1
            if (1, 7) in dict:
                dict[(1, 7)] = 1
            if (1, 6) in dict:
                dict[(1, 6)] = 1
        if board[7][7] == 0:
            if (6, 7) in dict:
                dict[(6, 7)] = 1
            if (7, 6) in dict:
                dict[(7, 6)] = 1
            if (6, 6) in dict:
                dict[(6, 6)] = 1
        if board[7][0] == 0:
            if (7, 1) in dict:
                dict[(7, 1)] = 1
            if (6, 0) in dict:
                dict[(6, 0)] = 1
            if (6, 1) in dict:
                dict[(6, 1)] = 1

    def com_random_level0(self, t, board):
        x, y = random.choice(self.possible_squares_list(t, board))
        return (x, y)

    def set_com1_level(self):
        if self.com1:
            def set_com1(level):
                if level == 0:
                    self.com1_level = self.com_random_level0
                if level == 1:
                    self.com1_level = self.com_best_choice_level1
                if level == 2:
                    self.com1_level = self.come_best_choice_level2
                if level == 3:
                    self.com1_level = self.come_best_choice_level3
                com_choose.destroy()
            com_choose = tk.Tk()
            fr = tk.Frame(com_choose)
            fr.grid()
            com_choose.title("CHOOSE COM LEVEL")
            button_level0 = tk.Button(fr, text="LEVEL0", height=4, width=6,
                                      command=lambda: set_com1(0))
            button_level1 = tk.Button(fr, text="LEVEL1", height=4, width=6,
                                      command=lambda: set_com1(1))
            button_level2 = tk.Button(fr, text="LEVEL2", height=4, width=6,
                                      command=lambda: set_com1(2))
            button_level3 = tk.Button(fr, text="LEVEL3", height=4, width=6,
                                      command=lambda: set_com1(3))
            button_level0.grid(row=1, column=1)
            button_level1.grid(row=1, column=2)
            button_level2.grid(row=1, column=3)
            button_level3.grid(row=1, column=4)
            fr.mainloop()

    def set_com2_level(self):
        if self.com2:
            def set_com2(level):
                if level == 0:
                    self.com2_level = self.com_random_level0
                if level == 1:
                    self.com2_level = self.com_best_choice_level1
                if level == 2:
                    self.com2_level = self.come_best_choice_level2
                if level == 3:
                    self.com2_level = self.come_best_choice_level3
                com_choose.destroy()
            com_choose = tk.Tk()
            fr = tk.Frame(com_choose)
            fr.grid()
            com_choose.title("CHOOSE COM LEVEL")
            button_level0 = tk.Button(fr, text="LEVEL0", height=4, width=6,
                                      command=lambda: set_com2(0))
            button_level1 = tk.Button(fr, text="LEVEL1", height=4, width=6,
                                      command=lambda: set_com2(1))
            button_level2 = tk.Button(fr, text="LEVEL2", height=4, width=6,
                                      command=lambda: set_com2(2))
            button_level3 = tk.Button(fr, text="LEVEL3", height=4, width=6,
                                      command=lambda: set_com2(3))
            button_level0.grid(row=1, column=1)
            button_level1.grid(row=1, column=2)
            button_level2.grid(row=1, column=3)
            button_level3.grid(row=1, column=4)
            fr.mainloop()

    def click_com_like_ai(self, event):
        "マス目をクリックした後の流れ(x,y)を入力してからの流れ全てをcomを絡めて行う"
        y = event.x
        x = event.y
        x = x // 70
        y = y // 70
        if self.possible_squares_list(self.turn, self.board) == []:
            self.turn *= -1
            self.turn_yellow(self.canvas, self.turn, self.board, 8, 8)
        else:
            if self.turn == self.com1:
                x, y = self.com1_level(self.com1, self.board)
            elif self.turn == self.com2:
                x, y = self.com2_level(self.com2, self.board)
            elif self.turn == self.player1 or self.turn == self.player2:
                pass
            if (x, y) in self.possible_squares_list(self.turn, self.board):
                self.put_a_piece(x, y, self.turn, self.board)
                self.put_or_turn_all_stones_on_canvas(self.canvas, self.board)
                self.turn *= -1
                self.turn_yellow(self.canvas, self.turn, self.board, x, y)
        self.show_my_turn(self.my_turn, self.turn, self.canvas)
        self.show_result(self.board)

    def main_ver4_tk_com_like_ai(self):
        "comとの対戦をgui上で楽しむ"
        self.set_player_and_com()
        self.set_com1_level()
        self.set_com2_level()
        self.make_board_tkinter()
        self.init_board(self.board)
        self.put_or_turn_all_stones_on_canvas(self.canvas, self.board)
        self.turn_yellow(self.canvas, self.turn, self.board, 8, 8)
        self.canvas.bind('<ButtonPress>', self.click_com_like_ai)
        self.app.mainloop()


if __name__ == '__main__':
    othe = OthelloVer4()
    othe.main_ver4_tk_com_like_ai()
