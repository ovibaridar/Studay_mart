A = set(input("Enter elements of set A separated by spaces: ").split())
B = set(input("Enter elements of set B separated by spaces: ").split())

is_subset = A.issubset(B)

if is_subset:
    print("Set A is a subset of set B.")
else:
    print("Set A is not a subset of set B.")
