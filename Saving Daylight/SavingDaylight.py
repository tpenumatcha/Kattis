import sys
for line in sys.stdin:
    date = line.split()
    sunrise = int(date[3][:date[3].index(":")]) * 60 + int(date[3][date[3].index(":") + 1:])
    sunset = int(date[4][:date[4].index(":")]) * 60 + int(date[4][date[4].index(":") + 1:])
    sunlight = sunset - sunrise
    hours = sunlight // 60
    minutes = sunlight % 60
    print(date[0] + " " + date[1] + " " + date[2] + " " + str(hours) + " hours " + str(minutes) + " minutes")
