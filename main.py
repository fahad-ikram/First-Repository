# Initialize two variables
a = 5
b = 10
print(f"Before swapping:\na: {a}\nb: {b}")
# Swap using arithmetic operations
a = a + b  # Step 1: a now holds the sum of a and b
b = a - b  # Step 2: b now holds the original value of a
a = a - b  # Step 3: a now holds the original value of b
print(f"After swapping:\na: {a}\nb: {b}")
