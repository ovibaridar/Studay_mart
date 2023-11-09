
A = set(input("Enter elements of set A separated by spaces: ").split())
B = set(input("Enter elements of set B separated by spaces: ").split())

symmetric_difference_result = A.symmetric_difference(B)

symmetric_difference_list = list(symmetric_difference_result)

print("Symmetric difference between sets A and B:", symmetric_difference_list)
