from .classes import bingo_board

def day4(filename):
    with open(filename,'r') as f:
        first_line = f.readline()
        boards = []
        BB = None
        for line in f.readlines():
            if line == '\n':
                if BB == None:
                    BB = bingo_board()
                else:
                    boards.append(BB)
                    BB = bingo_board()
            else:
                BB.addRow(line)
        boards.append(BB)
        winner = None
        winning_number = None
        for number in first_line.split(','):
            for board in boards:
                board.addNumber(number)
                if board.bingo and not board.checked:
                    winner = board
                    winning_number = number
                    wining_point = board.calculatePoint(int(number))

                    #break
                    board.checked = True
                else:
                    pass

            #if winner:
            #    break
    return wining_point,0
