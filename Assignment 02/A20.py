def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
print(gcd(n1, n2))