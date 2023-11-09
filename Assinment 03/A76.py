
A = set(input("Enter elements of set A separated by spaces: ").split())
B = set(input("Enter elements of set B separated by spaces: ").split())


is_superset = A.issuperset(B)




if is_superset:
    print("Set A is a superset of set B.")
else:
    print("Set A is not a superset of set B.")
