import csv
from datetime import datetime

infile = open("death_valley_2018_simple.csv","r")

csv_file = csv.reader(infile)

header_row = next(csv_file)

print(header_row)

highs = []
dates = []
lows = []

some_date = datetime.strptime('2018-07-01', '%Y-%m-%d')
print(some_date)


for index, col_header in enumerate(header_row):
    print(index, col_header)

for row in csv_file:
    try:
        high = int(row[4])
        low = int(row[5])
        some_date = datetime.strptime(row[2], '%Y-%m-%d')
    except ValueError:
        print(f"Missing data for {row}")

    else:
        highs.append(int(row[4]))
        lows.append(int(row[5]))
    
        dates.append(some_date)

print(highs[:5])
print(dates[:5])

import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dates, highs, c='red', alpha = 0.5)
plt.plot(dates, lows, c='blue', alpha = 0.5)

plt.fill_between(dates,highs,lows, facecolor= 'blue', alpha = 0.1)

plt.title("Daily low and high temps - 2018", fontsize=16)
plt.xlabel("Dates", fontsize=16)
plt.ylabel("Temps (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

fig.autofmt_xdate()

plt.show()



