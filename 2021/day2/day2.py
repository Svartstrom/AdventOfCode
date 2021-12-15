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
