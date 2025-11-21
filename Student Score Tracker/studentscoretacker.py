# Student Score Tracker

marks = []  # empty list to store 5 marks

# Taking input for 5 subjects
for i in range(1, 6):
    mark = float(input(f"Enter mark {i}: "))
    marks.append(mark)

print("\n--- Student Score Report ---\n")

# Total
total = sum(marks)
print("Total Marks:", total)

# Average
average = total / 5
print("Average Marks:", average)

# Highest mark
print("Highest Mark:", max(marks))

# Lowest mark
print("Lowest Mark:", min(marks))

# Pass / Fail
if average >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")
