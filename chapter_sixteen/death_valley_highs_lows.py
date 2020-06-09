import csv

from datetime import datetime

import matplotlib.pyplot as plt

file_name = 'data_csv/death_valley_2018_simple.csv'
with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    highs = []
    dates = []
    lows = []
    for row in reader:
        try:
            high = int(row[5])
            low = int(row[6])
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
        except ValueError:
            print(f'Missing data for {current_date}')
        else:
            highs.append(high)
            dates.append(current_date)
            lows.append(low)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='green', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
plt.title('Daily high and low Temperature of Death Valley')
plt.xlabel('Dates')
fig.autofmt_xdate()
plt.ylabel('Temperature')
plt.tick_params(axis='both', which='major')
plt.show()
