from random import randint

class Game:
    def __init__(self):
        self.r = int(input("Masukkan jumlah baris : "))
        self.c = int(input("Masukkan jumlah kolom : "))
        self.board = Board(self.r, self.c)
        self.board.display()
        self.gameOver = False
        self.playGame()

    def playGame(self):
        while not self.gameOver:
            baris = int(input("input baris yang ingin anda buka : "))
            kolom = int(input("input kolom yang ingin anda buka : "))
            if baris > self.r-1 or kolom > self.c-1:
                print("Maaf inputan anda diluar jangkauan")
                continue
            self.board.openCell(baris, kolom)
            self.board.display()
            if self.board.score >= 3 :
                self.gameOver = True
                print("You Win!")
            elif self.board.score <= -3 or self.board.step == self.r * self.c:
                self.gameOver = True
                print("You Lose!")

class Board:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.board = []
        self.score = 0
        self.step = 0
        for _ in range(self.row):
            self.baris = []
            for _ in range(self.col):
                d = randint(-1,1)
                if d == -1:
                    square = Bomb()
                elif d == 0:
                    square = Empty()
                else:
                    square = Bonus()
                self.baris.append(square)
            self.board.append(self.baris)
    
    def openCell(self, h, v):
        if self.board[h][v].isOpen:
            print("Cell, sudah dibuka, buka yang lain ya...")
            return 
        else:
            self.board[h][v].open()

        self.score += self.board[h][v].score
        self.step += 1
        print(self.board[h][v].caption)

    def display(self):
        # print("board : ", self.board)
        self.number = 0
        print("score : ", self.score)
        for i in range(self.row):
            for j in range(self.col):
                self.number += 1
                if self.board[i][j].isOpen:
                    print(self.board[i][j].shape, end=" ")
                else:
                    print("\033[33m {} \033[m".format(self.number), end=" ")       
            print()

class Square:
    def __init__(self):
        self.isOpen = False
        self.shape = "\033[33m * \033[m" 
        self.score = 0

    def open(self):
        self.isOpen = True

class Bonus(Square):
    def __init__(self):
        Square.__init__(self)
        self.shape = "\033[32m $ \033[m"
        self.score = 1
        self.caption = "yeay, anda mendapatkan bonus"

    def __repr__(self):
        return "Bonus cell"

class Empty(Square):
    def __init__(self):
        super().__init__()
        self.shape = "\033[34m 0 \033[m"
        self.score = 0
        self.caption = "anda mendapatkan sel kosong"

    def __repr__(self):
        return "Empty cell"

class Bomb(Square):
    def __init__(self):
        super().__init__()
        self.shape = "\033[31m ! \033[m"
        self.score = -1
        self.caption = "wah, anda mendapatkan bom!!!"

    def __repr__(self):
        return "Bonus cell"


Game()

# bonus = Bonus()
# print(bonus.__dir__)
# print(bonus.__dict__)




