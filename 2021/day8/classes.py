
"""
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
"""
    # 0: 6 abcefg
    # 1: 2 cf
    # 2: 5 acdeg
    # 3: 5 acdfg
    # 4: 4 bcdf
    # 5: 5 abdfg
    # 6: 6 abdefg
    # 7: 3 acf
    # 8: 7 abcdefg
    # 9: 6 abcdfg
class display:
    def __init__(self):
        T = []
        UL = []
        UR = []
        M = []
        LL = []
        LR = []
        B = []
    def checkStr(self,curr_str, input):
        if not curr_str:
            return input
        temp = ''
        for letter in input:
            if letter in curr_str:
                temp += letter
    def addNumber(self, disp_str):
        if len(digit) == 2:   #1
            self.addTwo(disp_str)
        elif len(digit) == 4: #4
            self.addFour(disp_str)
        elif len(digit) == 3: #7
            self.addSeven(disp_str)
        elif len(digit) == 7: #8
            self.addEight(disp_str)
        elif len(digit) == 6: # 0 6 9
            self.add069(disp_str)
        elif len(digit) == 5: # 2 3 5
            self.add235(disp_str)

    def addTwo(self, disp_str):
        pass
    def addFour(self, disp_str):
        pass
    def addSeven(self, disp_str):
        pass
    def addEight(self, disp_str):
        pass
    def add069(self, disp_str):
        pass
    def add235(self, disp_str):
        pass
