day = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"]

firstDay = [
    "Thursday",
    "Sunday",
    "Sunday",
    "Wednesday",
    "Friday",
    "Monday",
    "Wednesday",
    "Saturday",
    "Tuesday",
    "Thursday",
    "Sunday",
    "Tuesday"]

d = list(map(int, raw_input().split()))
print(day[(day.index(firstDay[d[1] - 1]) + (d[0] - 1)) % 7])
