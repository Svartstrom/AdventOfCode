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
