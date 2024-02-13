from day_1 import main as day1
from day_2 import main as day2
from day_3 import main as day3
from day_4 import main as day4
from day_5 import main as day5
from day_6 import main as day6
from day_7 import main as day7
from day_8 import main as day8

import time


def main():
    all_days = [day1, day2, day3, day4, day5, day6, day7, day8]
    for day in all_days:
        start = time.time()
        # print(f"{day.__name__}")
        day.main()
        print(f"time elapsed for {day.__name__} is {time.time()-start:.02}s")


if __name__ == "__main__":
    main()
