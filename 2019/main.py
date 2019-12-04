import math

def calc_fuel(m):
    if m <= 0:
        return 0
    c = math.floor(m/3)-2
    c = c if c >= 0 else 0
    return c + calc_fuel(c)

def createCablePath(directions):
    Path = []
    x, y = 0, 0
    for step in directions:
        count = int(step[1:])
        for i in range(count):
            if step[0] == "U":
                y += 1 
                Path.append((x,y))
            if step[0] == "D":
                y -= 1 
                Path.append((x,y))
            if step[0] == "L":
                x -= 1 
                Path.append((x,y))
            if step[0] == "R":
                x += 1 
                Path.append((x,y))
    return Path


def findNumberOfSteps(Path,point):
    for i, p in enumerate(Path):
        #print(p)
        if p == point:
            return i+1
    return -1

def manhattanDistance(P1, P2):
    return abs(P2[0] - P1[0]) + abs(P2[1] - P1[1])


def run_code(bb):
    op = 0
    index = 0
    while op != 99:
        op = bb[index]

        if op == 1:
            bb[bb[index+3]] = bb[bb[index+1]]+ bb[bb[index+2]]
            index += 4
        
        elif op == 2:
            bb[bb[index+3]] = bb[bb[index+1]] * bb[bb[index+2]]
            index += 4
        else:
            break
    return bb[0]


def numberOfCombinations(start, end):
    current = start
    valid = 0
    while current < end:
        current += 1
        temp = current
        prev = 10
        prev2 = 11
        oneSame, allDec = 0, 1
        while temp > 0:
            i = temp % 10
            temp = math.floor(temp / 10)
            if prev == i and prev2 != i and (temp%10 != i):
                oneSame = 1
            if i > prev:
                allDec = 0
            prev2 = prev
            prev = i

        if oneSame and allDec:
            valid += 1
    return valid


def day1_2():
    with open('day1_1_in.txt','r') as f:
        b= f.readlines()
    sum_ = 0
    for a in b:
        a=int(a)

        c = calc_fuel(a)
        sum_ += c
    print(sum_)

def day2_2():
    with open('day2_2_in.txt','r') as f:
        b = f.readlines()
    for org in b:
        org = org.split(',')
        for i, c in enumerate(org):
            org[i] = int(c)

    ans_ = 0
    noun = 0
    verb = 0
    while ans_ != 19690720:
        test = org[:]
        test[1] = noun
        test[2] = verb
        ans_ = run_code(test)
        noun += 1
        if noun > 99:
            noun = 0
            verb += 1
        if verb > 99:
            break
    print("noun: " + str(noun))
    print("verb: " + str(verb))

def day3_1():
    Path = []
    with open('day3_1_in.txt','r') as f:
        b = f.readlines()
    for a in b:
        a = a.split(',')
        Path.append(createCablePath(a))
    minDist = 10000000
    for s in Path[0]:
        if s in Path[1]:
            dist = manhattanDistance((0, 0),s)
            if dist < minDist:
                minDist = dist
                minS = s
    print(f"minimum manhattan distance is to {minS}, and is {minDist}")
def day3_2():
    Path = []
    with open('day3_1_in.txt','r') as f:
        b = f.readlines()
    for a in b:
        a = a.split(',')
        Path.append(createCablePath(a))
    minDist = 10000000
    for s in Path[0]:
        if s in Path[1]:
            dist0 = findNumberOfSteps(Path[0],s)
            dist1 = findNumberOfSteps(Path[1],s)

            dist = dist0 + dist1
            dist = dist if dist >=0 else 10000000
            if dist < minDist:
                minDist = dist
                minS = s
    print(f"minimum amount of steps is to {minS}, and is {minDist}")


def day4_1():
    start = 197487
    end = 673251

    result = numberOfCombinations(start, end)
    print(result)


def day5_1()

if __name__ == "__main__":
    #print("Day1: ")
    #day1_2()
    #print("Day2: ")
    #day2_2()
    #print("Day3: ")
    #day3_1()
    #day3_2()
    #print("Day4: ")
    #day4_1()
    print("Day4: ")
    day5_1()
