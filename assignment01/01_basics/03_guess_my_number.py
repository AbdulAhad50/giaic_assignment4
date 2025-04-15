import random

secret_number = random.randint(0, 99)

print("I am thinking of a number between 0 and 99...")

while True:
    try:
        guess = int(input("Enter a guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if guess > secret_number:
        print("Your guess is too high")
    elif guess < secret_number:
        print("Your guess is too low")
    else:
        print(f"Congrats! The number was: {secret_number}")
        break