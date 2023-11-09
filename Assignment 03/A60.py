def flatten_list(nested_list):
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


user_input = input("Enter a nested list (e.g., [1, [2, 3], [4, [5, 6], 7]]): ")

try:
    nested_list = eval(user_input)  # Safely evaluate the user input as a Python expression
    if isinstance(nested_list, list):
        flat_list = flatten_list(nested_list)
        print("Flattened list:", flat_list)
    else:
        print("Input is not a valid nested list.")
except (SyntaxError, NameError):
    print("Invalid input. Please enter a valid nested list in Python syntax.")
