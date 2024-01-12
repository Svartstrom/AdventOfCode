def day1(filename):
    prev = 1000000000
    i, i2, n = 0, 0, 0
    p1, p2, p3 = 100000000, 0, 0
    with open(filename,'r') as f:
        lines = f.readlines()
        for line in lines:
            line = int(line)
            if line > p1:
                i+=1
            p3, p2, p1 = p2, p1, line
            if n > 2:
                if p1 + p2 + p3 > prev:
                    i2 += 1
                prev = p1 + p2 + p3
            n += 1
    return i, i2


def day2(filename):
    hors, vert, depth, aim = 0,0,0,0
    with open(filename,'r') as f:
        lines = f.readlines()
        for line in lines:
            dir, mag = line.split()
            if dir == 'up':
                vert -= int(mag)
                aim -= int(mag)
            elif dir == 'down':
                vert += int(mag)
                aim += int(mag)
            elif dir == 'forward':
                hors += int(mag)
                depth += aim * int(mag)
    return hors * vert, hors * depth


def addToBin(bin, bit):
    if bit == '\n':
        return bin
    if not isinstance(bit,int):
        bit = int(bit)
    bin *= 2
    bin += bit
    return bin

def countBitsInPos(bin_list, pos):
    no_of_bits = 0
    for _bin in bin_list:
        no_of_bits += (_bin & 2**pos) > 0
    return no_of_bits > (len(bin_list) / 2)

def calcGammaEpsilon(lines):
    this_list = []
    for line in lines:
        line = line.strip()
        no_of_bits = 0
        this_bin = 0
        for letter in line:
            this_bin = addToBin(this_bin, int(letter))
            no_of_bits +=1
            
        this_list.append(this_bin)
    gamma = 0
    epsilon = 0
    for bit_pos in range(no_of_bits-1, -1, -1):
        most_prevalent = countBitsInPos(this_list, bit_pos)
        gamma = addToBin(gamma, most_prevalent > 0)
        epsilon = addToBin(epsilon, most_prevalent == 0)
    #10110
    return gamma*epsilon


def calcRecursivePrevalence(lines, index, dir):
    # oxygen is most prevalent bit, if you remove those that dont have the previous "bits the same"
    # CO2 is least prevalent bit, if you remove those that dont have the previous "bits the same"
    if not lines or index >= len(lines[0])-1:
        return []
    ones = []
    zeros = []
    for line in lines:
        line = line.strip()
        if line[index] == '1':
            ones.append(line)
        else:
            zeros.append(line)
    if dir == 'MOST':
        if len(ones) >= len(zeros):
            if len(ones) == 1:
                match = ones[0]
            else:
                match = calcRecursivePrevalence(ones, index+1, dir)
        else:
            if len(zeros) == 1:
                match = zeros[0]
            else:
                match = calcRecursivePrevalence(zeros, index+1, dir)
    else:
        if len(ones) < len(zeros):
            if len(ones) == 1:
                match = ones[0]
            else:
                match =  calcRecursivePrevalence(ones, index+1, dir)
        else:
            if len(zeros) == 1:
                match = zeros[0]
            else:
                match =  calcRecursivePrevalence(zeros, index+1, dir)
    return match
def day3(filename):
    with open(filename,'r') as f:
        lines = f.readlines()
    gamma_eps = calcGammaEpsilon(lines)
    most_prevalent = calcRecursivePrevalence(lines, 0, 'MOST')
    least_prevalent = calcRecursivePrevalence(lines, 0, 'LEAST')

    oxygen, CO2 = 0,0
    for _bin in most_prevalent:
        oxygen = addToBin(oxygen, _bin)
    for _bin in least_prevalent:
        CO2 = addToBin(CO2, _bin)
    return gamma_eps, oxygen*CO2



from .day4/classes import bingo_board

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



from .day5/classes import point, point_lister

def day5(filename):
    lister = point_lister()
    with open(filename,'r') as f:
        lines = f.readlines()
        for line in lines:
            points = line.split(' -> ')
            start = points[0].strip().split(',')
            end = points[1].strip().split(',')
            lister.addLine(int(start[0]),int(start[1]),int(end[0]),int(end[1]))
        intersektions = 0
        for key, val in lister.world.items():
            if val > 1:
                intersektions += 1
    return intersektions,0


