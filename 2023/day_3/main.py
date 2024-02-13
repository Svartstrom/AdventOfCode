import re


def day1(inp: list[str]) -> int:
    total = 0
    symbols = []
    numbers = []
    for i_row, line in enumerate(inp):
        symbol_match = re.finditer("([^\d\.])", line.strip())
        number_match = re.finditer("(\d+)", line.strip())
        for r in symbol_match:
            symbols.append((i_row, r.start()))
        for d in number_match:
            for r in range(max(i_row - 1, 0), min(i_row + 1, len(inp)) + 1):
                for c in range(max(d.start() - 1, 0), min(d.end() + 1, len(line))):
                    numbers.append((r, c, int(d.group())))
    for number in numbers:
        if (number[0], number[1]) in symbols:
            total += number[2]
            continue
    return total


def day2(inp):
    total = 0
    symbols = []
    numbers = []
    for i_row, line in enumerate(inp):
        symbol_match = re.finditer("([^\d\.])", line.strip())
        number_match = re.finditer("(\d+)", line.strip())
        for r in symbol_match:
            symbols.append((i_row, r.start(), r.group()))
        for d in number_match:
            for r in range(max(i_row - 1, 0), min(i_row + 1, len(inp)) + 1):
                for c in range(max(d.start() - 1, 0), min(d.end() + 1, len(line))):
                    numbers.append((r, c, int(d.group())))

    gears = []
    for symbol in symbols:
        j = []
        for number in numbers:
            if (number[0], number[1]) == (symbol[0], symbol[1]) and symbol[2] == "*":
                j.append(number[2])
        gears.append(j)
    for g in gears:
        if len(g) == 2:
            total += g[0] * g[1]

    return total


def main():
    with open("day_3/in1.txt", "r") as f:
        d1 = f.readlines()
    print(day1(d1))
    with open("day_3/in1.txt", "r") as f:
        d2 = f.readlines()
    print(day2(d2))


if __name__ == "__main__":
    main()
