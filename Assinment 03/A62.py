def convert_coordinates_to_lists(nested_list):
    x_coordinates = [coord[0] for coord in nested_list]
    y_coordinates = [coord[1] for coord in nested_list]
    return x_coordinates, y_coordinates


user_input = input("Enter a nested list of (x, y) coordinates as a Python list (e.g., [(1, 2), (3, 4), (5, 6)]): ")

try:
    nested_list = eval(user_input)
    if isinstance(nested_list, list) and all(isinstance(coord, tuple) and len(coord) == 2 for coord in nested_list):
        x_coords, y_coords = convert_coordinates_to_lists(nested_list)
        print("X-Coordinates:", x_coords)
        print("Y-Coordinates:", y_coords)
    else:
        print("Input is not a valid nested list of (x, y) coordinates.")
except (SyntaxError, NameError):
    print("Invalid input. Please enter a valid nested list in Python list syntax with (x, y) tuples.")
