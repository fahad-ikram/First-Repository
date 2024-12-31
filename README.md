# Swap Two Variables Using Arithmetic Operations

This repository demonstrates a simple Python script to swap the values of two variables without using a temporary variable. The script utilizes basic arithmetic operations (addition and subtraction) to achieve the swapping.

## Code Explanation

### Initial Values

The program starts by initializing two variables:

```python
# Initialize two variables
a = 5
b = 10
```

Here, `a` is assigned the value `5`, and `b` is assigned the value `10`.

### Printing Original Values

The original values of `a` and `b` are displayed using:

```python
print(f"Before swapping:\na :-> {a}\nb :-> {b}")
```

Output:

```\
Before swapping:
a :-> 5
b :-> 10
```

### Swapping Logic

The swapping is performed in three steps using arithmetic operations:

1. Add the values of `a` and `b` and store the result in `a`:

   ```python
   a = a + b  # a now holds the sum of a and b
   ```

   After this step:
   - `a = 15` (sum of `5` and `10`)
   - `b = 10`

2. Subtract the new value of `b` from `a` and assign the result to `b`:

   ```python
   b = a - b  # b now holds the original value of a
   ```

   After this step:
   - `a = 15`
   - `b = 5` (original value of `a`)

3. Subtract the new value of `b` from `a` and assign the result to `a`:

   ```python
   a = a - b  # a now holds the original value of b
   ```

   After this step:
   - `a = 10` (original value of `b`)
   - `b = 5`

### Printing Swapped Values

Finally, the swapped values of `a` and `b` are displayed:

```python
print(f"After swapping:\na :-> {a}\nb :-> {b}")
```

Output:

```\
After swapping:
a :-> 10
b :-> 5
```

## Key Advantages

- **No Temporary Variable**: The swapping is achieved without introducing an additional variable.
- **Efficient and Compact**: Uses simple arithmetic operations.

## Usage

This script can be executed in any Python environment. Simply copy and paste the code into a `.py` file and run it.

## Example Output

```\
Before swapping:
a = 5
b = 10
After swapping:
a = 10
b = 5
