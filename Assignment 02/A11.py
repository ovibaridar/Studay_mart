def print_natural_numbers(n):
    for i in range(1, n + 1):
        print(i)


n = int(input("Enter the number: "))
print_natural_numbers(n)


# Question 12: Calculate the factorial of a number
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


n = int(input("Enter the number: "))
print(factorial(n))
