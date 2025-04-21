print("Welcome to the Mad Libs Game!")

name = input("Enter a name: ")
place = input("Enter a place: ")
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb ending in -ing: ")
animal = input("Enter an animal: ")
emotion = input("Enter an emotion: ")

story = f"""
One day, {name} went to {place}. It was a very {adjective} day.
Suddenly, a {animal} appeared out of nowhere holding a {noun}!
{name} couldn't believe their eyes and started {verb}.
Everyone around was feeling {emotion} as they watched the scene unfold.
What a day to remember!
"""

print("\nHere's your Mad Libs story:")
print(story)
