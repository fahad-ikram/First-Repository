# Initialize two variables
a = 5
b = 10

# Print original values
print("Before swapping:")
print("a =", a)
print("b =", b)

# Swap using arithmetic operations
a = a + b  # Step 1: a now holds the sum of a and b
b = a - b  # Step 2: b now holds the original value of a
a = a - b  # Step 3: a now holds the original value of b

# Print swapped values
print("After swapping:")
print("a =", a)
print("b =", b)