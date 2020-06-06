import matplotlib.pyplot as plt

input_values = [i for i in range(1, 5001)]
cubes = [j ** 3 for j in input_values]
fig, ax = plt.subplots()
ax.scatter(input_values, cubes, s=1, c=cubes, cmap=plt.cm.Blues)
ax.set_title('Cubes', fontsize=24)
ax.set_ylabel('Cubes', fontsize=24)
ax.set_xlabel('Input Values', fontsize=24)
plt.show()
