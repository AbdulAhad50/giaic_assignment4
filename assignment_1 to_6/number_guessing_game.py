import random

low = 1
high = 100

number_to_guess = random.randint(low, high)

print(f"🎮 Welcome to the Guess the Number Game!")
print(f"I'm thinking of a number between {low} and {high}. Can you guess it?")

while True:
    guess = int(input("Enter your guess: "))
    
    if guess < number_to_guess:
        print("Too low! Try again 🔽")
    elif guess > number_to_guess:
        print("Too high! Try again 🔼")
    else:
        print(f"🎉 Correct! The number was {number_to_guess}. You win!")
        break
