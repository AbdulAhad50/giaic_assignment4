DAYS_PER_YEAR: int = 365
HOURS_PER_DAY: int = 24
MIN_PER_HOUR: int = 60
SEC_PER_MIN: int = 60


SEC_IN_YEAR = str(DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN)

def main():
    print(f"There are  {SEC_IN_YEAR} seconds in a year!")



if __name__ == '__main__':
    main()