
import day1.day1 as day1
import day2.day2 as day2
import day3.day3 as day3
import day4.day4 as day4
import day5.day5 as day5
import day6.day6 as day6
import day7.day7 as day7
import day8.day8 as day8

def test_day1():
    old_i, old_i2 = day1.day1('day1/in1.txt')
    new_i, new_i2 = day1.day1('day1/in1.txt')
    assert old_i == new_i
    assert old_i2 == new_i2

def test_day2():
    old_i, old_i2 = day2.day2('day2/in1.txt')
    new_i, new_i2 = day2.day2('day2/in1.txt')
    assert old_i == new_i
    assert old_i2 == new_i2

def test_day3():
    old_i, old_i2 = day3.day3('day3/in1.txt')
    new_i, new_i2 = day3.day3('day3/in1.txt')
    assert old_i == new_i
    assert old_i2 == new_i2

def test_day4():
    old_i, old_i2 = day4.day4('day4/in1.txt')
    new_i, new_i2 = day4.day4('day4/in1.txt')
    assert old_i == new_i
    assert old_i2 == new_i2

def test_day5():
    old_i, old_i2 = day5.day5('day5/in1.txt')
    new_i, new_i2 = day5.day5('day5/in1.txt')
    assert old_i == new_i
    assert old_i2 == new_i2

def test_day6():
    old_i, old_i2 = day6.day6('day6/in1.txt')
    new_i, new_i2 = day6.day6('day6/in1.txt')
    assert old_i == new_i
    assert old_i2 == new_i2

def test_day7():
    old_i, old_i2 = day7.day7('day7/in1.txt')
    new_i, new_i2 = day7.day7('day7/in1.txt')
    assert old_i == new_i
    assert old_i2 == new_i2

def test_day8():
    old_i, old_i2 = day8.day8('day8/in1.txt')
    new_i, new_i2 = day8.day8('day8/in1.txt')
    assert old_i == new_i
    assert old_i2 == new_i2