import matplotlib.pyplot as plt
import plotly


input_values = [i for i in range(1,1001)]
squares = [j**2 for j in input_values]
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(input_values, squares, c=squares, cmap=plt.cm.Greens , s=1)
ax.set_title('Squares', fontsize=24)
ax.set_xlabel('Value', fontsize=24)
ax.set_ylabel('Square of Value', fontsize=24)
ax.tick_params(axis='both', labelsize=24)
ax.axis([0, 1100, 0, 1100000])
plt.show()
