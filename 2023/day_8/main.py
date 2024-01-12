def day1(inp):
    return 1


def day2(inp):
    return 1


def main():
    with open("day_7/in1.txt", "r") as f:
        d1 = f.readlines()
    print(day1(d1))
    with open("day_7/in1.txt", "r") as f:
        d2 = f.readlines()
    print(day2(d2))


if __name__ == "__main__":
    main()
