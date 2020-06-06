from die import Die

from plotly.graph_objs import Bar, Layout

from plotly import offline

die = Die()
results = []
for i in range(100):
    result = die.roll()
    results.append(result)
frequencies = []
for values in range(1, die.sides + 1):
    frequency = results.count(values)
    frequencies.append(frequency)
print(frequencies)
x_values = list(range(1, die.sides + 1))
data = [Bar(x=x_values, y=frequencies)]
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling one D6 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
