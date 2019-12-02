
with open('day2_2_in.txt','r') as f:
    b = f.readlines()
    for a in b:
        #print(a)
        a = a.split(',')
        #print(a)
        for i, c in enumerate(a):
            a[i] = int(c)

        #print(len(b))
def run_code(bb):
    op = 0
    index = 0
    print(bb[0],bb[1],bb[2])
    while op != 99:
        op = bb[index]

        if op == 1:
            bb[bb[index+3]] = bb[bb[index+1]]+ bb[bb[index+2]]
            index += 4
        
        elif op == 2:
            bb[bb[index+3]] = bb[bb[index+1]] * bb[bb[index+2]]
            index += 4
        else:
            print(op, bb[0], index)
            break
    return bb[0]

org = a


ans_ = 0
noun = 0
verb = 0
while ans_ != 19690720:
    test = org[:]
    test[1] = noun
    test[2] = verb
    ans_ = run_code(test)
    print("noun:"+str(noun)+" verb: "+str(verb)+" => ans_:" +str(ans_))
    noun += 1
    if noun > 99:
        noun = 0
        verb += 1
    if verb > 99:
        break
print("noun: " + str(noun))
print("verb: " + str(verb))

print(org[0])
print(a)
print(org)
