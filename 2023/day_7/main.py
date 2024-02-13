# class C:
#    def __init__(self,count):
#        self.count = count#
#
#    def __cmp__(self,other):
#        return cmp(self.count,other.count)
# longList = [C(random.random()) for i in xrange(1000000)] #about 6.1 secs
# longList2 = longList[:]
#
# longList.sort() #about 52 - 6.1 = 46 secs
# longList2.sort(key = lambda c: c.count) #about 9 - 6.1 = 3 secs
from day_2 import main as m

from enum import Enum
from abc import ABCMeta


class strength(Enum):
    FIVE_OF_A = 7
    FOUR_OF_A = 6
    FULL_HOUSE = 5
    THREE_OF_A = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1


class Hand:
    def __init__(self, line: str):
        line = line.split()
        self.cards = [*line[0]]
        self.bid = int(line[1])
        self.labels = {
            "A": 0,
            "K": 0,
            "Q": 0,
            "J": 0,
            "T": 0,
            "9": 0,
            "8": 0,
            "7": 0,
            "6": 0,
            "5": 0,
            "4": 0,
            "3": 0,
            "2": 0,
        }
        self.strength = strength.HIGH_CARD
        for card in self.cards:
            self.labels[card] += 1
        self.set_strength()

    def set_strength(self):
        seen = 0
        for v in self.labels.values():
            if v == 5:
                self.strength = strength.FIVE_OF_A
            elif v == 4:
                self.strength = strength.FOUR_OF_A
            elif v == 3:
                if seen == 2:
                    self.strength = strength.FULL_HOUSE
                else:
                    self.strength = strength.THREE_OF_A
                seen = 3
            elif v == 2:
                if seen == 3:
                    self.strength = strength.FULL_HOUSE
                elif seen == 2:
                    self.strength = strength.TWO_PAIR
                else:
                    self.strength = strength.ONE_PAIR
                seen = 2

    def __eq__(self, other):
        return True

    def __lt__(self, other):
        if self.strength.value != other.strength.value:
            return self.strength.value < other.strength.value
        for s, o in zip(self.cards, other.cards):
            if s == o:
                continue
            return list(self.labels.keys()).index(s) > list(self.labels.keys()).index(o)

    def __str__(self) -> str:
        return f"{self.cards=}, {self.strength=}"


class Hand_2:
    def __init__(self, line: str):
        line = line.split()
        self.cards = [*line[0]]
        self.bid = int(line[1])
        self.labels = {
            "A": 0,
            "K": 0,
            "Q": 0,
            "T": 0,
            "9": 0,
            "8": 0,
            "7": 0,
            "6": 0,
            "5": 0,
            "4": 0,
            "3": 0,
            "2": 0,
            "J": 0,
        }
        self.strength = strength.HIGH_CARD
        for card in self.cards:
            # if card == "J":
            #    for c in self.labels.keys():
            #        self.labels[c] += 1
            # else:
            self.labels[card] += 1
        self.set_strength()

    def set_strength(self):
        seen = 0

        for v in self.labels.values():
            prev_str = self.strength
            used = 0
            if v == 5 or (v + self.labels["J"]) == 5:
                self.strength = strength.FIVE_OF_A
            elif v == 4 or (v + self.labels["J"]) == 4:
                self.strength = strength.FOUR_OF_A
            elif v == 3 or (v + self.labels["J"]) == 3:
                if seen == 2:
                    self.strength = strength.FULL_HOUSE
                else:
                    self.strength = strength.THREE_OF_A
                    used = 3 - v
                seen = 3
            elif v == 2 or (v + self.labels["J"] - used) == 2:
                if seen == 3:
                    self.strength = strength.FULL_HOUSE
                elif seen == 2:
                    self.strength = strength.TWO_PAIR
                    used = 2 - v
                else:
                    self.strength = strength.ONE_PAIR
                    used = 2 - v
                seen = 2
            if self.strength.value < prev_str.value:
                self.strength = prev_str

    def __eq__(self, other):
        return True

    def __lt__(self, other):
        if self.strength.value != other.strength.value:
            return self.strength.value < other.strength.value
        for s, o in zip(self.cards, other.cards):
            if s == o:
                continue
            return list(self.labels.keys()).index(s) > list(self.labels.keys()).index(o)

    def __str__(self) -> str:
        return f"{self.cards=}, {self.strength=} {self.bid=}\n{self.labels=}\n"


def day1(inp):
    hands = []
    for line in inp:
        hands.append(Hand(line))
    hands.sort()
    total = 0
    for i, hand in enumerate(hands):
        total += hand.bid * (i + 1)
    return total


def day2(inp):
    hands = []
    for line in inp:
        hands.append(Hand_2(line))
    hands.sort()
    total = 0
    for i, hand in enumerate(hands):
        total += hand.bid * (i + 1)
    return total


def main():
    # here?
    with open("day_7/in1.txt", "r") as f:
        d1 = f.readlines()
    print(day1(d1))
    with open("day_7/in1.txt", "r") as f:
        d2 = f.readlines()
    print(day2(d2))


if __name__ == "__main__":
    main()
