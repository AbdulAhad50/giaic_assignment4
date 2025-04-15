def mars_weight():
    earth_weight = float(input("Enter a weight on Earth: "))
    mars_gravity = 0.378
    mars_weight = round(earth_weight * mars_gravity, 2)
    
    print("The equivalent on Mars:", mars_weight)

mars_weight()
