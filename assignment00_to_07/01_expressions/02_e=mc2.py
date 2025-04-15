
C = 299792458
def main():
    mass_input = input("Enter kilos of mass: ")
    try:
        mass = float(mass_input)

        print("\ne = m * C^2...\n")
        print(f"m = {mass} kg")
        print(f"C = {C} m/s\n")

        energy = mass * C**2
        print(f"{energy} joules of energy!\n")
    except ValueError:
        print("Please enter a valid number for mass.")

if __name__ == '__main__':
    main()