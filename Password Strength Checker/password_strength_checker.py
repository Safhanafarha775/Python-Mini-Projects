import re

def password_strength(password):
    strength = 0
    remarks = ""

    # Conditions
    if len(password) >= 8:
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"[0-9]", password):
        strength += 1
    if re.search(r"[@$!%*?&]", password):
        strength += 1

    # Remarks
    if strength == 5:
        remarks = "Strong 💪"
    elif 3 <= strength < 5:
        remarks = "Medium ⚡"
    else:
        remarks = "Weak ❌"

    return remarks

# Example usage
pwd = input("Enter your password: ")
print("Password Strength:", password_strength(pwd))
