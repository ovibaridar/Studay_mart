A = set(input("Enter elements of set A separated by spaces: ").split())
B = set(input("Enter elements of set B separated by spaces: ").split())


print(A)
intersection_result = A.intersection(B)

intersection_list = list(intersection_result)

print("Common elements in sets A and B:", intersection_list)
