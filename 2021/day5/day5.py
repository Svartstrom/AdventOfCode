from .classes import point, point_lister

def day5(filename):
    lister = point_lister()
    with open(filename,'r') as f:
        lines = f.readlines()
        for line in lines:
            points = line.split(' -> ')
            start = points[0].strip().split(',')
            end = points[1].strip().split(',')
            lister.addLine(int(start[0]),int(start[1]),int(end[0]),int(end[1]))
        intersektions = 0
        for key, val in lister.world.items():
            if val > 1:
                intersektions += 1
    return intersektions,0
