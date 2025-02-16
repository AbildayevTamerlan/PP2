# Task 1
import datetime

x = datetime.datetime.now()

y = x - datetime.timedelta(days = 5)

print(x)
print(y)

print("-----------------")

# Task 2
x = datetime.datetime.now()

yesterday = (x - datetime.timedelta(days = 1)).strftime("%A")
today = x.strftime("%A")
tomorrow = (x + datetime.timedelta(days = 1)).strftime("%A")

print(yesterday)
print(today)
print(tomorrow)

print("-----------------")

# Task 3
x = datetime.datetime.now()

y = datetime.datetime(x.year, x.month, x.day, x.hour, x.minute, x.second)

print(x)
print(y)

print("-----------------")

# Task 4
a = datetime.datetime(2012, 12, 21, 18, 59, 28)
b = datetime.datetime.now()

difference = abs((a - b).total_seconds())

print(difference)