def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Test the function to display the Fibonacci sequence up to the nth term
n = 10
print(f"Recursive Fibonacci sequence up to {n} terms:")
for i in range(n):
    print(fibonacci_recursive(i))
