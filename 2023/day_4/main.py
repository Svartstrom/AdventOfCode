def day1(inp):
    total = 0
    for line in inp:
        this = 0
        winning = []
        line = line.split(":")
        winning_str, mine_str = line[1].split("|")
        winning_str = winning_str.split()
        mine_str = mine_str.split()
        for w in winning_str:
            winning.append(int(w))
        for m in mine_str:
            if int(m) in winning:
                if this:
                    this *= 2
                else:
                    this = 1
        total += this
    return total


def day2(inp):
    scratches = [1] * len(inp)
    for i, line in enumerate(inp):
        winning = []
        line = line.split(":")
        winning_str, mine_str = line[1].split("|")
        winning_str = winning_str.split()
        mine_str = mine_str.split()
        for w in winning_str:
            winning.append(int(w))
        for _ in range(scratches[i]):
            j = 0
            for m in mine_str:
                if int(m) in winning:
                    j += 1
                    scratches[i + j] += 1
    return sum(scratches)


def main():
    with open("day_4/in1.txt", "r") as f:
        d1 = f.readlines()
    print(day1(d1))
    with open("day_4/in1.txt", "r") as f:
        d2 = f.readlines()
    print(day2(d2))


if __name__ == "__main__":
    main()
