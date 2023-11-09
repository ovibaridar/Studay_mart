def sum_main_diagonal(matrix):
    if not matrix:
        return 0  # Return 0 for an empty matrix

    if len(matrix) != len(matrix[0]):
        return None  # Return None for a non-square matrix

    diagonal_sum = 0
    for i in range(len(matrix)):
        diagonal_sum += matrix[i][i]

    return diagonal_sum


def main():
    try:
        matrix = eval(input(
            "Enter a square matrix represented as a nested list: "))

        diagonal_sum = sum_main_diagonal(matrix)
        if diagonal_sum is not None:
            print("The sum of the main diagonal elements is:", diagonal_sum)
        else:
            print("The input matrix is not square.")
    except SyntaxError:
        print("Invalid input. Please enter a valid square matrix as a nested list.")


if __name__ == "__main__":
    main()
