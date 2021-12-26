

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
