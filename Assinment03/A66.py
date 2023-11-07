def find_max_in_nested_list(nested_list):
    if not nested_list:
        return float('-inf')

    max_element = float('-inf')

    for item in nested_list:
        if isinstance(item, list):
            max_in_sublist = find_max_in_nested_list(item)
            max_element = max(max_element, max_in_sublist)
        elif isinstance(item, int):
            max_element = max(max_element, item)

    return max_element


def main():
    try:
        nested_list = eval(
            input("Enter a nested list of integers: "))
        max_value = find_max_in_nested_list(nested_list)
        print("The maximum element in the nested list is:", max_value)
    except SyntaxError:
        print("Invalid input. Please enter a valid nested list.")


if __name__ == "__main__":
    main()
