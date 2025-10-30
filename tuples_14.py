fruits = ("apple", "banana", "cherry", "mango")

print("Tuple of fruits:", fruits)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
print("First two fruits:", fruits[:2])

print("All fruits:")
for fruit in fruits:
    print(fruit)

if "banana" in fruits:
    print("Yes, banana is in the tuple!")

print("Number of fruits:", len(fruits))

more_fruits = ("orange", "grape")
all_fruits = fruits + more_fruits
print("Combined tuple:", all_fruits)

nested = (fruits, more_fruits)
print("Nested tuple:", nested)


