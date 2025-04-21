import random

NUM_SIDE = 6

def orll_dice():
    die1 = random.randint(1, NUM_SIDE)
    die2 = random.randint(1, NUM_SIDE)

    total = die1 + die2
    print(f"Die 1 : {die1} Die 2: {die2} the total of dice is: {total}")



def main():
    die1: int = 10
    print("die1 in main() starts as: " + str(die1))
    for i in range(3):
        roll_dice()

    print("die1 in main() is: " + str(die1))


if __name__ == '__main__':
    main()