def main():
    w = [[j for j in x] for x in [range(1,4),range(4,11)]]
    for i, week in enumerate(w):
        for day in week:
            create_day(i+1,day)
def create_day(w,d):
    filename = f"week_{w}.py"
    with open(filename, "a") as f:
        f.write(f"""
def day_{d}:
    pass

""")

pass
if __name__ == "__main__":
    main()
