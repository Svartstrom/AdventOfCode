from day_7.main import day1, day2

in1 = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

in2 = """ 
"""


def test_day1():
    a = day1(in1.split("\n"))
    assert a == 6440


def test_day2():
    a = day2(in1.split("\n"))
    assert a == 5905
