input_list = input("Enter a list of elements separated by spaces: ").split()

unique_set = set()

for element in input_list:
    unique_set.add(element)

unique_list = list(unique_set)

print("Unique elements in the list:", unique_list)
