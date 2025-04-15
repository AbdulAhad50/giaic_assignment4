def in_range(n, low, high):
    if n >= low and n <= high:
        return True
    else:
        return False

def main():
    print(in_range(1, 8, 9))    # False
    print(in_range(4, 0, 10))   # True
    print(in_range(10, 2, 6))   # False

if __name__ == '__main__':
    main()
