
from day_3.main import day1, day2

in1 = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

in2 = """ 
"""

def test_day1():
    a = day1(in1.split())
    assert a == 4361

def test_day2():
    a = day2(in1.split())
    assert a == 467835