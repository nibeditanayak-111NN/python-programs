#*

for i in range(10):
    if i==4:
        break
    print(i)
#*
count = 1
while True:
    print(count)
    if count==5:
        break
    count = count + 1
#*
for j in range(3):
    for k in range(2):
        if k==1:
            break
        print(j, k)       
#*
numbers = [3, 7, 12, 9, 5]
target = 12

for num in numbers:
    if num == target:
        print("Found the target:", num)
        break
    print("Checking:", num)
