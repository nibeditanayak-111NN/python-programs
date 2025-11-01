import time

hour = int(time.strftime('%H'))
print("Current Hour:", hour)

if 0 <= hour < 12:
    print("Good Morning Sir!")
elif 12 <= hour < 17:
    print("Good Afternoon Sir!")
else:
    print("Good Evening Sir!")