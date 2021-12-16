import day1.day1 as day1
import day2.day2 as day2
import day3.day3 as day3
import day4.day4 as day4

def main():
    i, i2 = day1.day1('day1/in1.txt')
    print(f'Day 1.1: {i}')
    print(f'Day 1.2: {i2}')

    i, i2 = day2.day2('day2/in1.txt')
    print(f'Day 2.1: {i}')
    print(f'Day 2.2: {i2}')

    #i, i2 = day3('day3/test.txt')
    i, i2 = day3.day3('day3/in1.txt')
    #i2 = day3_2('day3/in1.txt')
    print(f'Day 3.1: {i}')
    print(f'Day 3.2: {i2}')

    i, i2 = day4.day4('day4/test.txt')
    i, i2 = day4.day4('day4/in1.txt')
    print(f'Day 4.1: {i}')
    print(f'Day 4.2: {i2}')
if __name__ == '__main__':
    main()
