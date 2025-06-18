# Mini Challenge: Unpack Me If You Can!
# You have this list of tuples representing students and their grades:

students = [
    ("Alice", 85, 92, 78),
    ("Bob", 90, 88, 95),
    ("Charlie", 70, 85, 80),
]


# Task:
# Write code to unpack each student's name and their three grades, then calculate and '
# 'print the student's average grade, all using sequence unpacking inside a loop.

# Bonus: Print the name in uppercase and the average rounded to 1 decimal place.

for student_record in students:
    student_name, grade1, grade2, grade3 = student_record
    print(f"{student_name.upper()} : {(grade1 + grade2 + grade3)/3:.1f}")

# If you want to level-up that code, here are two quick tips (optional,
# because you’re already rocking it):

# Use tuple unpacking in the loop itself:

for name, grade1, grade2, grade3 in students:
    print(f"{name.upper()} : {(grade1 + grade2 + grade3)/3:.1f}")

# Use sum() and len() for scalability:
# If your grades grow beyond three, this’ll save your fingers:

for name, *grades in students:
    grade = sum(grades) / len(grades)
    print(f"{name.upper()} : {grade:.1f}")

# Quirky unpacking examples
# 1. Ignoring values with underscore
x, _, z = (1, 99, 3)
print(x, z)  # 1 3

# 2. Unpack with * for variable-length chunks
a, *b, c = [10, 20, 30, 40, 50]
print(a, b, c)  # 10 [20, 30, 40] 50


# 3. Swap with unpacking
a, b = 5, 10
a, b = b, a
print(a, b)  # 10 5

# 4. Unpack dict items
d = {"name": "Eve", "age": 30}
for k, v in d.items():
    print(f"{k}: {v}")

# prints
# name: Eve
# age: 30

# 5. Nested unpacking
nested = (1, (2, 3), 4)
a, (b, c), d = nested
print(a, b, c, d)  # 1 2 3 4

# 6 spiral unpacking
a, b, *c, d, e = [1, 2, 3, 4, 5, 6, 7]
print(a, b, c, d, e)

# 🧩 Challenge 10: Unpacking Dictionary Items
# You’re given a dictionary like this:
student_scores = {
    "Alice": [92, 88, 95],
    "Sol": [81, 79, 85],
    "Alex": [100, 100, 100],
}
# Your task:

# 1. Loop through student_scores.items() using unpacking:
# Unpack both the key (name) and the value (which is a list of grades).

# Further unpack the grades inside the loop, assuming there are always 3 grades.

# Print each student's name in uppercase, and their highest grade.

# Expected output:
# ALICE: 95
# SOL: 85
# ALEX: 100

for name, scores in student_scores.items():
    print(f"{name.upper()}: {max(scores)}")

# 🧪 (If You Really Want to Unpack the 3 Scores):
for name, (s1, s2, s3) in student_scores.items():
    print(f"{name.upper()}: {max(s1, s2, s3)}")

# 🧠💥 Head-Twister Challenge: Unpack This
# You are given a nested list of students and their scores, but the structure is...
# not nice. Not at all.
data = [
    ("Alice", (91, 92, 93)),
    ("Sol", (84, 81, 79)),
    ("Alex", (100, 100, 100)),
    ("Otto", (88,)),
    ("Rin", (90, 95)),
]
# Your mission:
# Loop through data and print the name, number of scores, and the average score.
# But here's the twist:
# Unpack everything in the for loop header — no indexing inside the loop!
# Handle any number of scores (1, 2, 3, ...).
# Format average to one decimal place.
data = [
    ("Alice", (91, 92, 93)),
    ("Sol", (84, 81, 79)),
    ("Alex", (100, 100, 100)),
    ("Otto", (88,)),
    ("Rin", (90, 95)),
]


for name, scores in data:
    print(f"{name.upper()} ({len(scores)}): {(sum(scores)/len(scores)):.1f}")


list_comprehension_version = [
    f"{name.upper()} ({len(scores)}): {(sum(scores)/len(scores)):.1f}"
    for name, scores in data
]
print(list_comprehension_version)

# 🪄 Super Bonus Trick (just for fun):
# Want to see the weird wizardry version? Here's a dense, unreadable-but-legal one-liner
# (for the sake of fun, not for real use):
print(
    "\n".join(
        f"{n.upper()} ({l}): {s/l:.1f}"
        for n, sc in data
        if (l := len(sc)) and (s := sum(sc))
    )
)
