# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from play import Play
from read_write_file import ReadWriteFile


class MainGameHandler:
    board = {
        "R": [[0, 0], "LIVE", None, 1, 1],
        "B": [[7, 0], "LIVE", None, 1, 1],
        "G": [[7, 7], "LIVE", None, 1, 1],
        "Y": [[0, 7], "LIVE", None, 0, 0],
        "A": [[2, 2], False],
        "M": [[5, 2], False],
        "H": [[5, 5], False],
        "D": [[2, 5], False],
    }

    @staticmethod
    def is_night(key):
        if key == "R":
            return True
        elif key == "B":
            return True
        elif key == "G":
            return True
        elif key == "Y":
            return True
        else:
            return False

    def apply_instructions(self):

        instructions = ReadWriteFile.read()
        play = Play()
        # print(self.board)
        for nmove in instructions:
            self.board = play.move(nmove, self.board)
            # for night in data:
            #     Board.move(night,self.board,direction)

        for key in self.board.keys():
            # print(key)
            row = self.board[key][0][0]
            col = self.board[key][0][1]
            # print(row, col)
            if self.is_night(key):

                if (row < 0 or col < 0 or row > 8 or col > 8) and self.board[key][1] != "DEAD":
                    self.board[key][0] = "null"
                    self.board[key][1]="DROWNED"

                if self.board[key][2] is None:
                    self.board[key][2] = "null"
        print(self.board)
        ReadWriteFile.write(self.board)




#         Prepare the game result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # MainGameHandler.define_initial_board()
    start_game = MainGameHandler()
    start_game.apply_instructions()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
