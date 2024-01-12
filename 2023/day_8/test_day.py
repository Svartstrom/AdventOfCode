from day_8.main import day1, day2

in1 = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

in2 = """ 
"""


def test_day1():
    a = day1(in1.split("\n"))
    assert a == 2


def test_day2():
    a = day2(in1.split("\n"))
    assert a == 5905
