A = set(input("Enter elements of set A separated by spaces: ").split())
B = set(input("Enter elements of set B separated by spaces: ").split())

union_result = A.union(B)

union_list = list(union_result)

# Print all the distinct elements from both sets
print("Distinct elements from sets A and B (union):", union_list)
