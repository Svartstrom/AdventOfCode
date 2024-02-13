import re


def day1(inp):
    times = []
    distances = []
    time_match = re.finditer("(\d+)", inp[0].strip())
    dist_match = re.finditer("(\d+)", inp[1].strip())
    for d in time_match:
        times.append(int(d.group()))
    for d in dist_match:
        distances.append(int(d.group()))
    win_prod = 1
    print(times)
    for i_race in range(len(times)):
        win = 0
        for hold_time in range(times[i_race]):
            speed = hold_time
            tot_race_time = times[i_race]
            tot_dist = speed * (tot_race_time - hold_time)
            if tot_dist > distances[i_race]:
                win += 1
        win_prod *= win
    return win_prod


def day2(inp):
    times = []
    distances = []
    timestring = "".join(inp[0].split())
    time_match = re.finditer("(\d+)", timestring)
    dist_match = re.finditer("(\d+)", "".join(inp[1].split()))
    for d in time_match:
        times.append(int(d.group()))
    for d in dist_match:
        distances.append(int(d.group()))
    win_prod = 1
    for i_race in range(len(times)):
        win = 0
        for hold_time in range(times[i_race]):
            speed = hold_time
            tot_race_time = times[i_race]
            tot_dist = speed * (tot_race_time - hold_time)
            if tot_dist > distances[i_race]:
                win += 1
        win_prod *= win
    return win_prod


def main():
    with open("day_6/in1.txt", "r") as f:
        d1 = f.readlines()
    print(day1(d1))
    with open("day_6/in1.txt", "r") as f:
        d2 = f.readlines()
    print(day2(d2))


if __name__ == "__main__":
    main()
