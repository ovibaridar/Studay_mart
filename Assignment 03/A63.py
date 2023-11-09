def transpose_matrix(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    transposed = [[0] * num_rows for _ in range(num_cols)]

    for i in range(num_rows):
        for j in range(num_cols):
            transposed[j][i] = matrix[i][j]

    return transposed


user_input = input("Enter a matrix as a nested list (e.g., [[1, 2, 3], [4, 5, 6], [7, 8, 9]]): ")

try:
    matrix = eval(user_input)  # Safely evaluate the user input as a Python expression
    if isinstance(matrix, list) and all(isinstance(row, list) for row in matrix) and all(
            len(row) == len(matrix[0]) for row in matrix):
        transposed_matrix = transpose_matrix(matrix)
        print("Transposed Matrix:")
        for row in transposed_matrix:
            print(row)
    else:
        print("Input is not a valid matrix (nested list).")
except (SyntaxError, NameError):
    print("Invalid input. Please enter a valid matrix in Python list syntax.")
