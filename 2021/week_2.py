

def day6(filename):
    population = {ii:0 for ii in range(0,9)}
    generations = 257
    with open(filename,'r') as f:
        lines = f.readline()
    temp = lines.strip().split(',')
    for this in temp:
        population[int(this)] += 1
    for gen in range(1, generations):
        zeros = population[0]
        for age in range(1,9):
            population[age-1] = population[age]
        population[6] += zeros
        population[8] = zeros
        if gen == 80:
            prob_1 = population
    total_1, total_2 = 0,0
    s = ''
    for jj in range(0,9):
        s += f'{population[jj]}, '
        total_1 += prob_1[jj]
        total_2 += population[jj]
    return total_1, total_2


import math

def rms(arr, n):
    ans = 0
    for j in arr:
        ans += math.sqrt((int(j)-n)**2)
    return ans

def qms(arr,n):
    ans = 0
    for j in arr:
        steps = math.sqrt((int(j)-n)**2)
        if steps%2 == 0:
            temp = (steps + 1) * (steps/2)
        else:
            temp = (steps + 1) * ((steps-1)/2)
            temp += (steps+1)/2
        ans += temp
    return ans
def day7(filename):
    with open(filename,'r') as f:
        line = f.readline()
        line = line.split(',')
    line = [int(i) for i in line]
    minDist = 1000000000000
    minDist2 = 1000000000000
    maxPos = max(line)
    for this_dist in range(maxPos):
        dist = rms(line, this_dist)
        dist2 = qms(line, this_dist)
        if dist < minDist:
            minDist = dist
        if dist2 < minDist2:
            minDist2 = dist2
    return minDist, minDist2




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



def day_9(filename):
    pass


def day_10(filename):
    pass


def day_11(filename):
    pass


def day_12(filename):
    pass

