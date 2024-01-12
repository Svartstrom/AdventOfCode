
def day1(inp):
    nums = []
    tot_sum = 0
    for line in inp:
        nums=[]
        for char in line:
            try:
                a = int(char)
                nums.append(a)
            except ValueError:
                pass

        tot_sum += 10*nums[0] + nums[-1]
    return tot_sum

def day2(inp):
    tot_sum = 0
    for line in inp:
        print(line)
        nums=[]
        i = 0
        for char in line:
            try:
                a = int(char)
                try:
                    if i < nums[0][1]:
                        nums[0] = (a,i)
                    else:
                        nums.append((a,i))
                except IndexError:
                    nums = [(a,i)]
            except ValueError:
                pass
            i += 1
        print(nums)
        for char_num in [('one',1),('two',2),('three',3),('four',4),('five',5),('six',6),('seven',7),('eight',8),('nine',9)]:
            inx = line.find(char_num[0])
            rinx = line.rfind(char_num[0])
            try:
                if inx == -1:
                    continue
                elif inx < nums[0][1]:
                    nums.insert(0,(char_num[1],inx))
                elif inx > nums[-1][1]:
                    nums.append((char_num[1],inx))
            except IndexError:
                nums = [(char_num[1],inx)]
            if rinx < nums[0][1]:
                nums.insert(0,(char_num[1],rinx))
            elif rinx > nums[-1][1]:
                nums.append((char_num[1],rinx))
            print(nums,char_num,inx,rinx)
        print(nums)
        tot_sum += 10*nums[0][0] + nums[-1][0]
    return tot_sum

def main():
    with open("day_1/in1.txt","r") as f:
        d1 = f.readlines()
    print(day1(d1))
    with open("day_1/in1.txt","r") as f:
        d2 = f.readlines()
    print(day2(d2))

if __name__ == "__main__":
    main()

