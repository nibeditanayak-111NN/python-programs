def function(a, b):
    n = int(input("Enter n (number of terms you want to print): "))

    if n <= 0:
        print("Please enter a positive number")
        return

    print(a, b, end=" ")

    for i in range(2, n):
        next = a + b
        print(next, end=" ")
        a = b
        b = next
function(0, 1)