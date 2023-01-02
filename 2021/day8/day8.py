
def day8(filename):
    with open(filename,'r') as f:
        lines = f.readlines()
    no_unique = 0
    for line in lines:
        line = line.split('|')
        input, output = line[0], line[1]

        for digit in output.split(' '):
            digit = digit.strip()
            if len(digit) == 2:   #1
                no_unique += 1
            elif len(digit) == 4: #4
                no_unique += 1
            elif len(digit) == 3: #7
                no_unique += 1
            elif len(digit) == 7: #8
                no_unique += 1

    return no_unique, 0
