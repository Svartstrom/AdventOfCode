class point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.n = 1
    def __repr__(self):
        return f'{self.x}, {self.y}: _{self.n}_'
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class point_lister():
    def __init__(self):
        self.world = {}
    def __repr__(self):
        repr = ''
        for key, val in self.world.items():
            repr += f'[{p}]\n'
        return repr

    def addLine(self, x1, y1, x2, y2):
        def addPoint(x_, y_):
            this_point = f'{x_} {y_}'
            if not this_point in self.world:
                self.world[this_point] = 1
            else:
                self.world[this_point] +=1
        if x1 == x2:
            for ii in range(min(y1, y2), max(y1, y2)+1):
                addPoint(x1, ii)
        elif y1 == y2:
            for ii in range(min(x1, x2),max(x1, x2)+1):
                addPoint(ii, y1)
        else:
            x_dir = 1 if x1<x2 else -1
            y_dir = 1 if y1<y2 else -1
            for x, y in zip(range(x1,x2+x_dir,x_dir),range(y1,y2+y_dir,y_dir)):
                addPoint(x,y)
