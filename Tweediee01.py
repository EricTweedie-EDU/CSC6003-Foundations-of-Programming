import math
# importing math module to use pi
# Program asking for the user to provide a number for the radius of a circle/sphere
r = float(input("Please provide the radius for a circle/sphere: "))

# taking the users input and implementing it into 3 formulas to calculate the circumference, area, and volume with the given radius

circ = round(2*math.pi*r, 5)  # calculating the circumference, using the given radius

area = round(math.pi*r**2, 5)  # calculating the area, using the given radius

vol = round(4/3*math.pi*r**3, 5)  # calculating the volume of a sphere, using the given radius

# After calculating the circumference, area, and volume the ansers are displayed back to the user
# Rounding to 5 decimal places to keep the results looking neater
#circumference
print(f"The circumference of a circle with radius {r} is {circ}!")

#area
print(f"The area of a circle with radius {r} is {area}")

#volume
print(f"The volume of a sphere with radius {r} is {vol}")