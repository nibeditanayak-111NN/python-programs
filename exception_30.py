# Example 1
try:
    a = int(input("Enter a number: "))
    print(10 / a)
except ZeroDivisionError:
    print("Error: You can't divide by zero.")
except ValueError:
    print("Error: Please enter a valid number.")


# Example 2
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Division by zero not allowed!")
else:
    print("Division successful. Result:", result)


# Example 3
try:
    f = open("data.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("File not found!")
else:
    print("File read successfully.")
finally:
    # Only close if file opened successfully
    try:
        f.close()
    except:
        pass
    print("File closed.")


# Example 4
try:
    x = int(input("Enter number: "))
    print(100 / x)
except (ValueError, ZeroDivisionError) as e:
    print("Error:", e)


# Example 5
