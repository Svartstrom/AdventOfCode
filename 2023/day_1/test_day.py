
from day_1.main import day1, day2

in1 = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

in2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

def test_day1():

    
    a = day1(in1.split())
    assert a == 142

def test_day2():
    a = day2(in2.split())
    assert a == 281