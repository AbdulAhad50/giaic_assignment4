ADULT_AGE = 18  # Legal adult age in the U.S.

def is_adult(age):
    return age >= ADULT_AGE

def main():
    age = int(input("How old is this person?: "))
    print(is_adult(age))

main()

def main():
    name : str = input("What's your name? ")
    print(greet(name))

def greet(name):
    return "Greetings " + name + "!"
	
if __name__ == '__main__':
    main()
