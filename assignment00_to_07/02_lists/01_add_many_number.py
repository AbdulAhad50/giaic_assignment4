def add_many_numbers(numbers)-> int:
    
    Total: int = 0
    for number in numbers:
        Total += number

    return Total

def main():
    numbers: list[int] = [1, 2, 3, 4, 5]
    sumOfNumbers: int = add_many_numbers(numbers)  
    print(sumOfNumbers) 
    

if __name__ == '__main__':
    main()