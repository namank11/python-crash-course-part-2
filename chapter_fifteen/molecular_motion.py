from random import choice

class MolecularMotion:
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x = [250]
        self.y = [260]
    def walk(self):
        while len(self.x) < self.num_points:
            x_direction = choice([-1,1])
            x_distance = choice([0,1,2,3,4])
            x_steps = x_distance * x_direction

            y_direction = choice([-1, 1])
            y_distance = choice([0,1,2,3,4])
            y_steps = y_distance * y_direction

            if (x_steps==0 and y_steps==0):
                continue

            X = self.x[-1] +x_steps
            Y = self.y[-1] +y_steps

            self.x.append(X)
            self.y.append(Y)
