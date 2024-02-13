import re


def day1(inp):
    colors = [(12, "red"), (13, "green"), (14, "blue")]
    total = 0
    for i, line in enumerate(inp):
        line = line.strip().split(":")[1].split(";")
        possible = True
        for draw in line:
            for color in colors:
                resp = re.findall(f"(\d+) {color[1]}", draw)
                if resp and int(resp[0]) > color[0]:
                    possible = False
        if possible:
            total += i + 1
    return total


def day2(inp):
    total = 0
    for _, line in enumerate(inp):
        colors = [(0, "red"), (0, "green"), (0, "blue")]
        line = line.strip().split(":")[1].split(";")
        for draw in line:
            for i_color, color in enumerate(colors):
                resp = re.findall(f"(\d+) {color[1]}", draw)
                if resp and int(resp[0]) > color[0]:
                    colors[i_color] = (int(resp[0]), color[1])
        intermediate = 1
        for j in colors:
            intermediate *= j[0]
        total += intermediate
    return total


def main():
    with open("day_2/in1.txt", "r") as f:
        d1 = f.readlines()
    print(day1(d1))
    with open("day_2/in1.txt", "r") as f:
        d2 = f.readlines()
    print(day2(d2))


if __name__ == "__main__":
    main()
