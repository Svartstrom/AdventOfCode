import re


class Transformator:
    def __init__(self):
        self.destination = []
        self.source = []
        self.range = []

    def add_range(self, spec: list[str, str, str]):
        self.destination.append(int(spec[0]))
        self.source.append(int(spec[1]))
        self.range.append(int(spec[2]))

    def return_dest(self, source: int) -> int:
        for i, s in enumerate(self.source):
            if source >= s and source <= s + self.range[i]:
                return self.destination[i] + (source - self.source[i])
        return source


def day1(inp):
    seeds = 0
    T = {}
    current = ""
    transformations = [
        "seed-to-soil",
        "soil-to-fertilizer",
        "fertilizer-to-water",
        "water-to-light",
        "light-to-temperature",
        "temperature-to-humidity",
        "humidity-to-location",
    ]
    for line in inp:
        parts = line.split()
        if not parts:
            continue
        if parts[0] == "seeds:":
            seeds = [int(s) for s in parts[1:]]
        elif parts[0] in transformations:
            current = parts[0]
        if current and len(parts) == 3:
            if not current in T.keys():
                T[current] = Transformator()
            T[current].add_range(parts)
    lowest = 0
    for this in seeds:
        for t in transformations:
            this = T[t].return_dest(this)
        if not lowest or this < lowest:
            lowest = this
    return lowest


def gen_seeds(parts):
    odd = [parts[i] for i in range(1, len(parts)) if i % 2 == 1]
    even = [parts[i] for i in range(1, len(parts)) if i % 2 == 0]
    s = [(int(i), int(j)) for i, j in zip(odd, even)]
    i = 0
    r = 0
    while i < len(s):
        yield s[i][0] + r
        r += 1
        if r > s[i][1]:
            r = 0
            i += 1


def day2(inp):
    seeds = 0
    T = {}
    current = ""
    transformations = [
        "seed-to-soil",
        "soil-to-fertilizer",
        "fertilizer-to-water",
        "water-to-light",
        "light-to-temperature",
        "temperature-to-humidity",
        "humidity-to-location",
    ]
    seed_pattern = None
    for line in inp:
        parts = line.split()
        if not parts:
            continue
        if parts[0] == "seeds:":
            seed_pattern = parts
            # print(parts)
            # gen_seeds(parts)

            # seeds = [s for s in range(int(parts[1]),int(parts[2])+int(parts[1]))]
            # seeds2 = [s for s in range(int(parts[1]),int(parts[2])+int(parts[1]))]
            # for seed in seeds2:
            #    seeds.append(seed)
            # print(seeds)
        elif parts[0] in transformations:
            current = parts[0]
        if current and len(parts) == 3:
            if not current in T.keys():
                T[current] = Transformator()
            T[current].add_range(parts)
    lowest = 0
    for this in gen_seeds(seed_pattern):  # seeds:
        for t in transformations:
            this = T[t].return_dest(this)
        if not lowest or this < lowest:
            lowest = this
    return lowest


def main():
    with open("day_5/in1.txt", "r") as f:
        d1 = f.readlines()
    print(day1(d1))
    # with open("day_5/in1.txt","r") as f:
    #    d2 = f.readlines()
    # print(day2(d2))


if __name__ == "__main__":
    main()
