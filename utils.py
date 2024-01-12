import os
PYTHON_DAY = """
def day_DAY(filename):
    pass

"""

def main():
    i = 6
    w = [[j for j in x] for x in [range(1,i),range(i,i+7),range(i+7,2*i+8),range(2*i+8,3*i+7)]]
    #w = [[d for d in x] for x in range(week*())]
    #0-5
    #6-12
    #13-19
    try:
        os.remove("2021/week_1.py")
        os.remove("2021/week_2.py")
        os.remove("2021/week_3.py")
        os.remove("2021/week_4.py")
    except:
        pass
    for i, week in enumerate(w):
        for day in week:
            create_day(i+1,day)
def create_day(w,d):
    filename = f"2021/week_{w}.py"
    with open(filename, "a") as f:
        f.write(PYTHON_DAY.replace("DAY", str(d)))

pass
if __name__ == "__main__":
    main()
