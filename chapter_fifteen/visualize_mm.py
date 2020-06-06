import matplotlib.pyplot as plt
from molecular_motion import MolecularMotion
while True:
    molecularmotion = MolecularMotion()
    fig, ax = plt.subplots()
    molecularmotion.walk()
    xcoordinates= molecularmotion.x
    ycoordinates=molecularmotion.y
    num_points= range(molecularmotion.num_points)
    ax.scatter(xcoordinates, ycoordinates, c=num_points,cmap=plt.cm.Blues, edgecolors='none', s=1)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    prompt = input('Want to walk more? (y/n)')
    if prompt == 'n' or prompt == 'N':
        break
