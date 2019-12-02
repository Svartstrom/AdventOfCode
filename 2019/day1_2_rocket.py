import math

def calc_fuel(m):
    if m <= 0:
        return 0
    c = math.floor(m/3)-2
    c = c if c >= 0 else 0
    return c + calc_fuel(c)

with open('day1_1_in.txt','r') as f:
    b= f.readlines()
    sum_ = 0
    for a in b:
        a=int(a)

        c = calc_fuel(a)
        sum_ += c
        #print(str(a)+" "+str(c))

print(sum_)
#print(calc_fuel(1969))



