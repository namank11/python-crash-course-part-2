import matplotlib.pyplot as plt
from random_walk import RandomWalk
while True:
    randomwalk = RandomWalk(30000)
    fig, ax = plt.subplots()
    randomwalk.walk()
    xcoordinates= randomwalk.x
    ycoordinates=randomwalk.y
    num_points= range(randomwalk.num_points)
    ax.scatter(xcoordinates, ycoordinates, c=num_points,cmap=plt.cm.Blues, edgecolors='none', s=1)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    prompt = input('Want to walk more? (y/n)')
    if prompt == 'n' or prompt == 'N':
        break
