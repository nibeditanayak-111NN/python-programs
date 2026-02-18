numbers = [4,7,2,7,8,2,4,4,9,8,7,1]
count = 1
for num in set(numbers):
    count =numbers.count(num)
    if count > 2:
        print(num, "appears", count, "times")
