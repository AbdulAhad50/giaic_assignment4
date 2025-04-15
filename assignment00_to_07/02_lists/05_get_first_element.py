def get_first_element(lst):
    print("The first element is:", lst[0])

def main():
    lst = []
    num_elements = int(input("How many elements would you like to enter? "))

    for i in range(num_elements):
        element = input(f"Enter element #{i + 1}: ")
        lst.append(element)

    get_first_element(lst)

if __name__ == '__main__':
    main()