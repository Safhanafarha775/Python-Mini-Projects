# Number Category Analyzer

# Taking input
num = float(input("Enter any number: "))

print("\n--- Number Category Analyzer Result ---\n")

# 1. Odd / Even
if num.is_integer():         # Check if number is whole number
    num_int = int(num)
    if num_int % 2 == 0:
        print("➡️ The number is Even.")
    else:
        print("➡️ The number is Odd.")
else:
    print("➡️ The number is not a whole number, so Odd/Even doesn't apply.")

# 2. Positive / Negative / Zero
if num > 0:
    print("➡️ The number is Positive.")
elif num < 0:
    print("➡️ The number is Negative.")
else:
    print("➡️ The number is Zero.")

# 3. Divisible by 5 or 10
if num.is_integer():
    if num_int % 5 == 0:
        print("➡️ The number is divisible by 5.")
    else:
        print("➡️ Not divisible by 5.")

    if num_int % 10 == 0:
        print("➡️ The number is divisible by 10.")
    else:
        print("➡️ Not divisible by 10.")
else:
    print("➡️ Divisibility checks apply only for whole numbers.")

# 4. Between 1–100
if 1 <= num <= 100:
    print("➡️ The number is between 1 and 100.")
else:
    print("➡️ The number is NOT between 1 and 100.")

# BONUS: Special Number (divisible by 6 or 9)
if num.is_integer():
    if num_int % 6 == 0 or num_int % 9 == 0:
        print("✨ Special Number!")
