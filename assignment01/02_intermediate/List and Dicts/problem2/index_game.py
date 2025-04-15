def access_element(my_list, index):
    if 0 <= index < len(my_list):
        return my_list[index]
    else:
        return "Index out of range."

def modify_element(my_list, index, new_value):
    if 0 <= index < len(my_list):
        my_list[index] = new_value
        return f"Element at index {index} modified to {new_value}."
    else:
        return "Index out of range."

def slice_list(my_list, start, end):
    if 0 <= start <= len(my_list) and 0 <= end <= len(my_list):
        return my_list[start:end]
    else:
        return "Invalid slice indices."

def index_game():
    # Initial list
    my_list = ['cat', 'dog', 'bird', 'fish', 'hamster']
    print("Initial list:", my_list)

    while True:
        print("\nChoose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Quit")
        
        choice = input("Enter 1, 2, 3, or 4: ")

        if choice == '1':
            idx = int(input("Enter index to access: "))
            result = access_element(my_list, idx)
            print("Result:", result)

        elif choice == '2':
            idx = int(input("Enter index to modify: "))
            new_val = input("Enter new value: ")
            result = modify_element(my_list, idx, new_val)
            print(result)
            print("Updated list:", my_list)

        elif choice == '3':
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            result = slice_list(my_list, start, end)
            print("Sliced list:", result)

        elif choice == '4':
            print("Thanks for playing!")
            break

        else:
            print("Invalid choice. Try again.")

# Start the game
index_game()
