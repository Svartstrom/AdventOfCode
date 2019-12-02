
with open('day2_2_in.txt','r') as f:
    prog_string = f.readlines()
    for prog in prog_string:
        command = prog.split(',')
        for i, command in enumerate(command):
            org[i] = int(command)
            
            
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

