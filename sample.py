def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n! = n * (n-1)!
        return n * factorial(n - 1)

# Test the function with some examples
num = 5
result = factorial(num)
print(f"The factorial of {num} is {result}")
