A = set(input("Enter elements of set A separated by spaces: ").split())
B = set(input("Enter elements of set B separated by spaces: ").split())
C = set(input("Enter elements of set C separated by spaces: ").split())

intersection_AB = A.intersection(B)

union_BC = B.union(C)

difference_CA = C.difference(A)

intersection_list = list(intersection_AB)
union_list = list(union_BC)
difference_list = list(difference_CA)

# Print the results
print("Intersection of sets A and B:", intersection_list)
print("Union of sets B and C:", union_list)
print("Difference between set C and A:", difference_list)
