from random import choice


class RandomWalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x = [0]
        self.y = [0]

    def get_steps(self):
        direction = choice([-1, 1])
        distance = choice([0, 1, 2, 3, 4])
        steps = distance * direction
        return steps


    def walk(self):
        while len(self.x) < self.num_points:
            xsteps = self.get_steps()
            ysteps = self.get_steps()
            X = self.x[-1] + xsteps
            Y = self.y[-1] + ysteps

            self.x.append(X)
            self.y.append(Y)
