import day1.day1 as day1
import day2.day2 as day2
import day3.day3 as day3
import day4.day4 as day4
import day5.day5 as day5
import day6.day6 as day6
import day7.day7 as day7
import day8.day8 as day8

def main():
    i, i2 = day1.day1('day1/in1.txt')
    print(f'Day 1.1: {i}')
    print(f'Day 1.2: {i2}')

    i, i2 = day2.day2('day2/in1.txt')
    print(f'Day 2.1: {i}')
    print(f'Day 2.2: {i2}')

    #i, i2 = day3('day3/test.txt')
    i, i2 = day3.day3('day3/in1.txt')
    print(f'Day 3.1: {i}')
    print(f'Day 3.2: {i2}')

    #i, i2 = day4.day4('day4/test.txt')
    i, i2 = day4.day4('day4/in1.txt')
    print(f'Day 4.1: {i}')
    print(f'Day 4.2: {i2}')

    #i, i2 = day5.day5('day5/test.txt')
    i, i2 = day5.day5('day5/in1.txt')
    print(f'Day 5.1: {i}')
    print(f'Day 5.2: {i2}')

    #i, i2 = day6.day6('day6/test.txt')
    i, i2 = day6.day6('day6/in1.txt')
    print(f'Day 6.1: {i}')
    print(f'Day 6.2: {i2}')

    #i, i2 = day7.day7('day7/test.txt')
    i, i2 = day7.day7('day7/in1.txt')
    print(f'Day 7.1: {i}')
    print(f'Day 7.2: {i2}')

    #i, i2 = day8.day8('day8/test.txt')
    i, i2 = day8.day8('day8/in1.txt')
    print(f'Day 8.1: {i}')
    print(f'Day 8.2: {i2}')
if __name__ == '__main__':
    main()

