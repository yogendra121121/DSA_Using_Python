def generate_fibonacci(n):
    fibonacci_sequence = []
    a, b = 0, 1

    for i in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b

    return fibonacci_sequence

# Input the number of terms you want in the Fibonacci series
n = input("Enter a number: ")
fibonacci_series = generate_fibonacci(n)
print("Fibonacci Series:")
print(fibonacci_series)
