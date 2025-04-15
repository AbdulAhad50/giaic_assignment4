def get_last_element(lst):
    print("\nThe last element is:", lst[-1])

def main():
    lst = []
    num_elements = int(input("How many elements would you like to enter? "))

    for i in range(num_elements):
        element = input(f"Enter element #{i + 1}: ")
        lst.append(element)

    get_last_element(lst)

if __name__ == '__main__':
    main()