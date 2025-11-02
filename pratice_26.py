secret_number = 7
attempts = 0

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 10. Type 0 to quit.\n")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == 0:
        print("You chose to quit the game.")
        break

    if guess < 0 or guess > 10:
        print("Invalid guess! Please enter a number between 1 and 10.\n")
        continue

    if guess == secret_number:
        print(f"🎉 Correct! You guessed it in {attempts} attempts.")
        break
    elif guess < secret_number:
        print("Too low! Try again.\n")
    else:
        print("Too high! Try again.\n")

print("Game Over!")
