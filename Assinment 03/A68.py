def find_element_position(matrix, element):
    for row_index, row in enumerate(matrix):
        if element in row:
            col_index = row.index(element)
            return row_index, col_index
    return None  # Element not found

def main():
    try:
        matrix = eval(input("Enter a nested list representing a matrix: "))
        element = int(input("Enter the element to search for: "))

        position = find_element_position(matrix, element)
        if position is not None:
            row, col = position
            print(f"The element {element} is found at position (row: {row}, column: {col}).")
        else:
            print(f"The element {element} was not found in the matrix.")
    except SyntaxError:
        print("Invalid input. Please enter a valid nested list representing a matrix.")

if __name__ == "__main__":
    main()
