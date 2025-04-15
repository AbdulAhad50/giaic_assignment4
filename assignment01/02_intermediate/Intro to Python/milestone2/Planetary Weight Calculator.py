def planetary_weight():
    gravity = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }

    earth_weight = float(input("Enter a weight on Earth: "))
    planet = input("Enter a planet: ")

    if planet in gravity:
        planet_weight = round(earth_weight * gravity[planet], 2)
        print(f"The equivalent weight on {planet}: {planet_weight}")
    else:
        print("That planet is not in the list.")

planetary_weight()
