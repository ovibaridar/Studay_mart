input_set = set(input("Enter elements of the set separated by spaces: ").split())

element_to_check = input("Enter the element to check: ")

if element_to_check in input_set:
    print("Found")
else:
    print("Not Found")
