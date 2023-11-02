def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b


x = int(input("Enter 1st number : "))
y = int(input("Enter 2nd number : "))

x, y = swap(x, y)

print("After swapping:")
print("1st = ", x)
print("2nd = ", y)
