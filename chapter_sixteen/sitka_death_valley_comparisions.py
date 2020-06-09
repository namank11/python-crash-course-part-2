import csv

from datetime import datetime

import matplotlib.pyplot as plt

file_name_sitka = 'data_csv/sitka_weather_2018_simple.csv'
file_name_death_valley = 'data_csv/death_valley_2018_simple.csv'


def get_data(file_name, dates, highs, lows):
    with open(file_name) as f:
        reader = csv.reader(f)
        header_row = next(reader)
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
sitka_dates = []
sitka_highs = []
sitka_lows = []
death_valley_dates = []
death_valley_highs = []
death_valley_lows = []
get_data(file_name_sitka, sitka_dates, sitka_highs, sitka_lows)
get_data(file_name_death_valley, death_valley_dates, death_valley_highs, death_valley_lows)
ax.plot(sitka_dates, sitka_highs, c='red', alpha=0.5)
ax.plot(sitka_dates, sitka_lows, c='green', alpha=0.5)
plt.fill_between(sitka_dates, sitka_highs, sitka_lows, facecolor='blue', alpha=0.1)
ax.plot(death_valley_dates, death_valley_highs, c='red', alpha=0.5)
ax.plot(death_valley_dates, death_valley_lows, c='green', alpha=0.5)
plt.fill_between(death_valley_dates, death_valley_highs, death_valley_lows, facecolor='blue', alpha=0.1)
plt.title('Daily high and low Temperature of Sitka-Death Valley')
plt.xlabel('Dates')
fig.autofmt_xdate()
plt.ylabel('Temperature')
plt.tick_params(axis='both', which='major')
plt.show()
