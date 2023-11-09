def sort_sublists_by_length(nested_list):

    sorted_list = sorted(nested_list, key=len)
    return sorted_list


user_input = input("Enter a nested list as a Python list (e.g., [[1, 2, 3], [4, 5], [6, 7, 8, 9], [10]]): ")

try:
    nested_list = eval(user_input)  # Safely evaluate the user input as a Python expression
    if isinstance(nested_list, list) and all(isinstance(sublist, list) for sublist in nested_list):
        sorted_nested_list = sort_sublists_by_length(nested_list)
        print("Sorted Nested List:")
        for sublist in sorted_nested_list:
            print(sublist)
    else:
        print("Input is not a valid nested list.")
except (SyntaxError, NameError):
    print("Invalid input. Please enter a valid nested list in Python list syntax.")
