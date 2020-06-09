import csv

from datetime import datetime

import matplotlib.pyplot as plt

file_name = 'data_csv/sitka_weather_2018_simple.csv'
with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    rains = []
    dates = []
    for index, row in enumerate(header_row):
        print(index, row)
    for row in reader:
        try:
            rain = float(row[5])
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
        except ValueError:
            print(f'Missing data for {current_date}')
        else:
            rains.append(rain)
            dates.append(current_date)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, rains, c='red')
plt.title('Rainfall of SITKA')
plt.xlabel('Dates')
fig.autofmt_xdate()
plt.ylabel('Precipitation')
plt.tick_params(axis='both', which='major')
plt.show()
