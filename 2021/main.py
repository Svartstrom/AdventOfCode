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
            p3 = p2
            p2 = p1
            p1 = line
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
    bin *= 2
    bin += bit
    return bin

def countBitsInPos(bin_list, pos):
    no_of_bits = 0
    for _bin in bin_list:
        no_of_bits += (_bin & 2**pos) > 0
    return no_of_bits > (len(bin_list) / 2)

def day3(filename):
    list = []
    this_list = []

    ll = ''
    n, n_ = 0, 0
    tot=0
    with open(filename,'r') as f:
        lines = f.readlines()
        for line in lines:
            j = 0
            #bin = format(line)
            no_of_bits = 0
            this_bin = 0
            #print(bin+3)
            print('for stav in line:')
            for stav in line:
                if stav != '\n':
                    print(stav)
                    this_bin = addToBin(this_bin, int(stav))
                    no_of_bits +=1
                else:
                    this_list.append(this_bin)
                if j > len(list)-1:
                    try:
                        list.append(int(stav))
                    except ValueError:
                        pass
                else:
                    try:
                        list[j] += int(stav)
                    except ValueError:
                        pass
                j += 1
            tot += 1
        #print(list)
        gamma = 0
        epsilon = 0
        print(f'list: {list}')
        for p in list:
            print(bin(p))
        print('f')
        for p in this_list:
            print(bin(p))
        print(no_of_bits)
        for bit_pos in range(no_of_bits-1, -1, -1):
            print(bit_pos)
            most_prevalent = countBitsInPos(this_list, bit_pos)
            print(f'most_prev: {most_prevalent}')
            gamma = addToBin(gamma, most_prevalent > 0)
            epsilon = addToBin(epsilon, most_prevalent == 0)
            print(gamma,epsilon,gamma*epsilon)
        for jj in range(len(list), 0, -1):
            #print(f'{list[len(list)-jj]} > {tot/2} : {list[len(list)-jj]>tot/2} * {2**(jj-1)} = {(list[len(list)-jj]>tot/2) * 2**(jj-1)}')
            #print((list[len(list)-jj]>tot/2) * 2**(jj-1))
            n += (list[len(list)-jj]>tot/2) * 2**(jj-1)
            n_ += (list[len(list)-jj]<tot/2) * 2**(jj-1)
        #print(bin+2)
        print(n,bin(n),n_,bin(n_),n*n_)
        print(gamma,bin(gamma),epsilon,bin(epsilon),gamma*epsilon)
        #10110
        return n*n_
def day3_2(filename):
    with open(filename,'r') as f:
        lines = f.readlines()
        for line in lines:
            pass
    return 0
def main():
    i, i2 = day1('day1/in1.txt')
    print(f'Day 1.1: {i}')
    print(f'Day 1.2: {i2}')

    i, i2 = day2('day2/in1.txt')
    print(f'Day 2.1: {i}')
    print(f'Day 2.2: {i2}')

    i = day3('day3/test.txt')
    #i = day3('day3/in1.txt')
    i2 = day3_2('day3/in1.txt')
    print(f'Day 3.1: {i}')
    print(f'Day 3.2: {i2}')
if __name__ == '__main__':
    main()
