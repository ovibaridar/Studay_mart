def flatten_nested_list(nested_list):
    flat_list = []
    stack = [nested_list]

    while stack:
        current = stack.pop()
        for item in current:
            if isinstance(item, list):
                stack.append(item)
            else:
                flat_list.append(item)

    return flat_list


# Input from the user
user_input = input("Enter a list of nested lists (e.g., [[1, 2, 3], [4, 5], [6, 7, 8, 9]]): ")

try:
    nested_list = eval(user_input)  # Safely evaluate the user input as a Python expression
    if isinstance(nested_list, list):
        flat_list = flatten_nested_list(nested_list)
        print("Concatenated Flat List:", flat_list)
    else:
        print("Input is not a valid list of nested lists.")
except (SyntaxError, NameError):
    print("Invalid input. Please Input valid input")
