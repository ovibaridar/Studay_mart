
def calculate_sphere_volume(radius):
    pi = 3.14159
    volume = (4/3) * pi * (radius**3)
    return volume


radius = float(input("Enter the radius of the sphere: "))


volume = calculate_sphere_volume(radius)


print("Volume of the sphere:", volume)
