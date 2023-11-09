A = set(input("Enter elements of set A separated by spaces: ").split())
B = set(input("Enter elements of set B separated by spaces: ").split())

difference_result = A.difference(B)

difference_list = list(difference_result)

print("Elements in set A but not in set B:", difference_list)