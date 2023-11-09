def count_even_numbers(nested_list):
    even_count = 0
    for sublist in nested_list:
        for item in sublist:
            if isinstance(item, int) and item % 2 == 0:
                even_count += 1
    return even_count


def main():
    try:
        nested_list = eval(
            input("Enter a nested list: "))
        even_count = count_even_numbers(nested_list)
        print("The number of even numbers in the nested list is:", even_count)
    except SyntaxError:
        print("Invalid input. Please enter a valid nested list.")


if __name__ == "__main__":
    main()
