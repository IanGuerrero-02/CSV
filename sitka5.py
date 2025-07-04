import csv
from datetime import datetime

infile = open("sitka_weather_2018_simple.csv","r")

csv_file = csv.reader(infile)

header_row = next(csv_file)

print(header_row)

sitka_highs = []
sitka_dates = []
sitka_lows = []

some_date = datetime.strptime('2018-07-01', '%Y-%m-%d')
print(some_date)


for index, col_header in enumerate(header_row):
    print(index, col_header)

for index, col_header in enumerate(header_row):
    if col_header == "TMAX":
        tmax_index = index
    elif col_header =="TMIN":
        tmin_index = index
    elif col_header == "DATE":
        date_index = index
    elif col_header == "NAME":
        name_index = index


for row in csv_file:
    try:
        high = int(row[tmax_index])
        low = int(row[tmin_index])
        some_date = datetime.strptime(row[date_index], '%Y-%m-%d')
    except ValueError:
        print(f"Missing data for {row}")
    else:
        sitka_highs.append(high)
        sitka_lows.append(low)
        sitka_dates.append(some_date)

print(sitka_highs[:5])
print(sitka_dates[:5])



infile = open("death_valley_2018_simple.csv", "r")
csv_file = csv.reader(infile)
header_row = next(csv_file)
print(header_row)


for index, col_header in enumerate(header_row):
    print(index, col_header)
    if col_header == "TMAX":
        tmax_index = index
    elif col_header == "TMIN":
        tmin_index = index
    elif col_header == "DATE":
        date_index = index
    elif col_header == "NAME":
        name_index = index

dv_dates = []
dv_highs = []
dv_lows = []

for row in csv_file:
    try:
        high = int(row[tmax_index])
        low = int(row[tmin_index])
        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
    except ValueError:
        print(f"Missing data for {row}")
    else:
        dv_highs.append(high)
        dv_lows.append(low)
        dv_dates.append(current_date)

import matplotlib.pyplot as plt

fig = plt.figure()


plt.subplot(2,1,1)
plt.plot(sitka_dates, sitka_highs, c='red', alpha = 0.5)
plt.plot(sitka_dates, sitka_lows, c='blue', alpha = 0.5)
plt.fill_between(sitka_dates,sitka_highs,sitka_lows, facecolor= 'blue', alpha = 0.1)
plt.title("Daily low and high temps Sitka", fontsize=16)
plt.ylabel("Temps (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)


plt.subplot(2,1,2)
plt.plot(dv_dates, dv_highs, c='red', alpha = 0.5)
plt.plot(dv_dates, dv_lows, c='blue', alpha = 0.5)
plt.fill_between(dv_dates,dv_highs,dv_lows, facecolor= 'blue', alpha = 0.1)
plt.title("Daily low and high temps Death Valley", fontsize=16)
plt.xlabel("Dates", fontsize=16)
plt.ylabel("Temps (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

fig.autofmt_xdate()

plt.suptitle("Temperature comparison between SITKA AIRPORT, AK US and DEATH VALLEY, CA US" )

plt.show()

