
def rectangle_area(length, width):
    area = length * width
    return area


# Input: Length and width of the rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = rectangle_area(length, width)


print("The area of the rectangle is:", area)
