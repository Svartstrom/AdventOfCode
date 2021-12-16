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
    list = []
    this_list = []
    for line in lines:
        no_of_bits = 0
        this_bin = 0
        for letter in line:
            if letter != '\n':
                this_bin = addToBin(this_bin, int(letter))
                no_of_bits +=1
            else:
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
        if line[index] == '\n':
            pass
        elif line[index] == '1':
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
