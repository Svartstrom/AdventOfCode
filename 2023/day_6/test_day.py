
from day_6.main import day1, day2

in1 = """Time:      7  15   30
Distance:  9  40  200"""

in2 = """ 
"""

def test_day1():
    a = day1(in1.split("\n"))
    assert a == 288

def test_day2():
    a = day2(in1.split("\n"))
    assert a == 71503