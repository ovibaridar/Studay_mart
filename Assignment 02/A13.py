def generate_fibonacci_sequence(n):
    fibonacci_sequence = [0, 1]
    for i in range(2, n):
        next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_value)
    return fibonacci_sequence

n = int(input("Enter the number of terms: "))
print(generate_fibonacci_sequence(n))