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
