
class bingo_board:
    def __init__(self):
        self.bingo = False
        self.checked = False
        self.rows = []
    def __repr__(self):
        repr = ''
        for row in self.rows:
            temp = ' '.join(row)+'\n'
            repr += temp
        #temp = ' '.join(self.rows)
        #repr = '\n'.join(temp)
        return repr
    def addRow(self, row):
        row = row.strip()
        self.rows.append(row.split())
    def addNumber(self, number):
        for i, row in enumerate(self.rows):
            for j, this_num in enumerate(row):
                if this_num == number:
                    self.rows[i][j] = '_'+this_num
                    #print(this_num)
                self.checkRows()
                self.checkCols()
    def checkRows(self):
        for row in self.rows:
            for i, col in enumerate(row):
                if col[0] != '_':
                    break
                if i == len(row)-1:
                    self.bingo = True
    def checkCols(self):
        for i in range(len(self.rows[0])):
            for j, row in enumerate(self.rows):
                if row[i][0] != '_':
                    break
                if j == len(row)-1:
                    self.bingo = True
    def calculatePoint(self, last):
        score = 0
        for row in self.rows:
            for number in row:
                if number[0] != '_':
                    score += int(number)
        return score * last
