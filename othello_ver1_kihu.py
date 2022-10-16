

class OthelloVer1(object):
    def __init__(self):
        self.board = [[0]*8 for _ in range(8)]
        self.turn = 1

    # ボードの初期化
    def init_board(self, board):
        '盤面をに初期状態にする'
        for i in range(8):
            for j in range(8):
                board[i][j] = 0
        board[3][3] = -1
        board[3][4] = 1
        board[4][3] = 1
        board[4][4] = -1

    # 配置可能かどうかの確認
    def turnbackabove(self, x, y, t, board):
        '（x、y）の上側のマス目を数値化'
        global a1
        global b1
        for i in range(1, x+1):
            if board[x-i][y] == -t:
                a1 += 1
            if board[x-i][y] == t:
                b1 += 1
                break
            if board[x-i][y] == 0:
                break

    def turnbackleft(self, x, y, t, board):
        '（x、y）の左側のマス目を数値化'
        global a2
        global b2
        for i in range(1, y+1):
            if board[x][y-i] == -t:
                a2 += 1
            if board[x][y-i] == t:
                b2 += 1
                break
            if board[x][y-i] == 0:
                break

    def turnbackdown(self, x, y, t, board):
        '（x、y）の下側のマス目を数値化'
        global a3, b3
        for i in range(1, 8-x):
            if board[x+i][y] == -t:
                a3 += 1
            if board[x+i][y] == t:
                b3 += 1
                break
            if board[x+i][y] == 0:
                break

    def turnbackright(self, x, y, t, board):
        '（x、y）の右側のマス目を数値化'
        global a4, b4
        for i in range(1, 8-y):
            if board[x][y+i] == -t:
                a4 += 1
            if board[x][y+i] == t:
                b4 += 1
                break
            if board[x][y+i] == 0:
                break

    def turnbacklefttabove(self, x, y, t, board):
        '（x、y）の左上側のマス目を数値化'
        global a5, b5
        if x >= y:
            for i in range(1, y+1):
                if board[x-i][y-i] == -t:
                    a5 += 1
                if board[x-i][y-i] == t:
                    b5 += 1
                    break
                if board[x-i][y-i] == 0:
                    break
        if x < y:
            for i in range(1, x+1):
                if board[x-i][y-i] == -t:
                    a5 += 1
                if board[x-i][y-i] == t:
                    b5 += 1
                    break
                if board[x-i][y-i] == 0:
                    break

    def turnbackrightdown(self, x, y, t, board):
        '（x、y）の右下側のマス目を数値化'
        global a6, b6
        if x >= y:
            for i in range(1, 8-x):
                if board[x+i][y+i] == -t:
                    a6 += 1
                if board[x+i][y+i] == t:
                    b6 += 1
                    break
                if board[x+i][y+i] == 0:
                    break
        if x < y:
            for i in range(1, 8-y):
                if board[x+i][y+i] == -t:
                    a6 += 1
                if board[x+i][y+i] == t:
                    b6 += 1
                    break
                if board[x+i][y+i] == 0:
                    break

    def turnbackrighttabove(self, x, y, t, board):
        '（x、y）の右上側のマス目を数値化'
        global a7, b7
        if x + y >= 7:
            for i in range(1, 8-y):
                if board[x-i][y+i] == -t:
                    a7 += 1
                if board[x-i][y+i] == t:
                    b7 += 1
                    break
                if board[x-i][y+i] == 0:
                    break
        if x + y < 7:
            for i in range(1, x+1):
                if board[x-i][y+i] == -t:
                    a7 += 1
                if board[x-i][y+i] == t:
                    b7 += 1
                    break
                if board[x-i][y+i] == 0:
                    break

    def turnbackleftdown(self, x, y, t, board):
        '（x、y）の左下側のマス目を数値化'
        global a8, b8
        if x + y >= 7:
            for i in range(1, 7-x):
                if board[x+i][y-i] == -t:
                    a8 += 1
                if board[x+i][y-i] == t:
                    b8 += 1
                    break
                if board[x+i][y-i] == 0:
                    break
        if x + y < 7:
            for i in range(1, y+1):
                if board[x+i][y-i] == -t:
                    a8 += 1
                if board[x+i][y-i] == t:
                    b8 += 1
                    break
                if board[x+i][y-i] == 0:
                    break

    # ## リスト作成
    def possible_squares_list(self, t, board):
        'boardのターンtにおいて配置可能なマス目のリスト生成'
        square_list = []
        for x in range(8):
            for y in range(8):
                if board[x][y] == 0:
                    self.init_turnbackcount()
                    self.turnbackabove(x, y, t, board)
                    self.turnbackdown(x, y, t, board)
                    self.turnbackright(x, y, t, board)
                    self.turnbackleft(x, y, t, board)
                    self.turnbacklefttabove(x, y, t, board)
                    self.turnbackleftdown(x, y, t, board)
                    self.turnbackrightdown(x, y, t, board)
                    self.turnbackrighttabove(x, y, t, board)
                    if((b1 != 0 and a1 != 0) or (b2 != 0 and a2 != 0)
                       or (b3 != 0 and a3 != 0) or (b4 != 0 and a4 != 0)
                       or (b5 != 0 and a5 != 0) or (b6 != 0 and a6 != 0)
                       or (b7 != 0 and a7 != 0) or (b8 != 0 and a8 != 0)):
                        square_list.append((x, y))
                    self.init_turnbackcount()
        return square_list

    # 駒操作の関数
    def init_turnbackcount(self):
        '裏返る個数の初期化'
        global a1, a2, a3, a4, a5, a6, a7, a8
        global b1, b2, b3, b4, b5, b6, b7, b8
        a1 = 0
        b1 = 0
        a2 = 0
        b2 = 0
        a3 = 0
        b3 = 0
        a4 = 0
        b4 = 0
        a5 = 0
        b5 = 0
        a6 = 0
        b6 = 0
        a7 = 0
        b7 = 0
        a8 = 0
        b8 = 0

    # 石を実際に置く操作
    def turn_back_all_direction(self, x, y, t, board):
        "x,y周囲の石を裏返す"
        self.turnbackabove(x, y, t, board)
        self.turnbackleft(x, y, t, board)
        self.turnbackdown(x, y, t, board)
        self.turnbackright(x, y, t, board)
        self.turnbacklefttabove(x, y, t, board)
        self.turnbackrightdown(x, y, t, board)
        self.turnbackrighttabove(x, y, t, board)
        self.turnbackleftdown(x, y, t, board)
        if b1 == 1:
            for j in range(a1):
                board[x-1-j][y] *= -1
        if b2 == 1:
            for j in range(a2):
                board[x][y-1-j] *= -1
        if b3 == 1:
            for j in range(a3):
                board[x+1+j][y] *= -1
        if b4 == 1:
            for j in range(a4):
                board[x][y+1+j] *= -1
        if b5 == 1:
            for j in range(a5):
                board[x-1-j][y-1-j] *= -1
        if b6 == 1:
            for j in range(a6):
                board[x+1+j][y+1+j] *= -1
        if b7 == 1:
            for j in range(a7):
                board[x-1-j][y+1+j] *= -1
        if b8 == 1:
            for j in range(a8):
                board[x+1+j][y-1-j] *= -1

    ###
    def put_a_piece(self, x, y, t, board):
        'boardのターンtにおいて、(x,y)に石を置き、全方向を裏返す'
        self.init_turnbackcount()
        self.turn_back_all_direction(x, y, t, board)
        self.init_turnbackcount()
        board[x][y] = t

    # ゲームの勝敗チェック
    def check_gameover_or_continue(self, board):
        'boardの盤面の駒、空白の数を数え、勝敗を調べ,先手勝利で１、後手勝利で２、引き分けで３、続行で４を返す'
        board2 = []
        for i in board:
            for j in i:
                board2.append(j)
        ocount = board2.count(0)
        fcount = board2.count(1)
        scount = board2.count(-1)
        if(ocount == 0):
            if (fcount > scount):
                return 1
            if (fcount < scount):
                return 2
            if (fcount == scount):
                return 3
        else:
            return 4

    # ゲーム開始
    def main_ver_kihu(self):
        "棋譜上でオセロを楽しむモード"
        self.init_board(self.board)
        while True:
            for i in range(len(self.board)):
                print(self.board[i])

            print("手番は", self.turn)

            print("設置可能なマス目",
                  self.possible_squares_list(self.turn, self.board))

            if self.possible_squares_list(self.turn, self.board) == []:
                input("passと入力して下さい")
                self.turn *= -1
                continue

            while True:
                x = int(input("上のリストから（x、y）を選び「x」と入力して下さい"))
                y = int(input("左からy列目を「y」と入力して下さい"))
                if (x, y) in self.possible_squares_list(self.turn, self.board):
                    self.put_a_piece(x, y, self.turn, self.board)
                    break
                else:
                    continue

            gameovercheck = self.check_gameover_or_continue(self.board)
            if gameovercheck == 1:
                print("先手の勝利")
                break
            elif gameovercheck == 2:
                print("後手の勝利")
                break
            elif gameovercheck == 3:
                print("引き分け")
                break
            elif gameovercheck == 4:
                self.turn *= -1


if __name__ == '__main__':
    othello = OthelloVer1()
    othello.main_ver_kihu()
