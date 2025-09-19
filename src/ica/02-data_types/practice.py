print("=== INTEGER vs FLOAT OPERATIONS ===")
print("add 1", 4 + 9)        # Both int → int result
print("add 2", 4 + 9.0)      # One float → float result
print("sub 1", 3.2 - 1.1)    # Both float → float result
print("sub 2", 3 - 1)        # Both int → int result
print("sub 3", 3 - 1.0)      # One float → float result
print("mul 1", 4 * 5)        # Both int → int result
print("mul 2", 4 * 6.5)      # One float → float result
print("div 1", 25 / 3)       # Regular division ALWAYS returns float
print("div 2", 25 / 3.0)     # Regular division ALWAYS returns float
print("div 3", 25 // 3)      # Floor division with ints → int
print("div 4", 25.0 // 3.0)  # Floor division with floats → float
print("rem 1", 25 % 3)       # Remainder with ints → int
print("rem 2", 40 % 11.0)    # Remainder with float → float
print("exp 1", 3 ** 2)       # Power with ints → int
print("exp 2", 2.0 ** 3)     # Power with float → float