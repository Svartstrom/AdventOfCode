
with open('day2_1_in.txt','r') as f:
    b = f.readlines()
    for a in b:
        #print(a)
        a = a.split(',')
        #print(a)
        for i, c in enumerate(a):
            a[i] = int(c)

        #print(len(b))
print(a)
print(a[0])
print(type(a[0]))

op = 0
index = 0
while op != 99:
    op = a[index]

    if op == 1:
        a[a[index+3]] = a[a[index+1]]+ a[a[index+2]]
    
    if op == 2:
        a[a[index+3]] = a[a[index+1]] * a[a[index+2]]
    index = index + 4

print(a)
