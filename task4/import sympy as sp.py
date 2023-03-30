import sympy as sp

# Define the symbols
x = sp.Symbol('x')

# Define the function
y = sp.cos(x)

# Find the derivative
dy_dx = sp.diff(y, x)

# Print the derivative
print(f"The derivative of y = cos(x) is dy/dx = {dy_dx}")
