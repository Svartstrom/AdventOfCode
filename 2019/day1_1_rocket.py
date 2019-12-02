import math
with open('in.txt','r') as f:
    b= f.readlines()
    sum_ = 0
    for a in b:
        a=int(a)

        c = math.floor(a/3)-2
        sum_ += c
        print(str(a)+" "+str(c))

print(sum_)
