# Exercise: Extracting all the Students With Marks Greater Than Ten
# Let’s try to get the names of all students who received combined marks greater than ten
# in all their quizzes.

# Problem statement
# You have been provided with a text file that contains the names of students along with
# their marks for four different quizzes, each graded out of five (5). This text file has
# content similar to the following:
# Jim : 1 5 4 3
# Andrew : 5 2 3 0
# Tom : 0 3 4 1
# Therefore, your task is to write the student_names() function, which takes in the text
# file’s filename and returns a list of those students that have combined marks of all
# their quizzes greater than 10.
# Input filename = 'test.txt'
# Output ["Jim"]

from pathlib import Path


def extract_student_names(filename):
    result = []
    with open(filename) as f:
        for line in f:
            if ":" not in line:
                continue
            data = line.split(":")
            name = data[0].strip()
            marks = data[1].strip()
            total_marks = 0
            for score in marks.split():
                total_marks += int(score)
            if total_marks > 10:
                result.append(name)
    return result


filename = Path("coreprogramming") / "basic_tutorial_exercises" / "marks_file.txt"
print(extract_student_names(filename))

# Feedback
# 1. Avoid Repetition in Stripping
# You're doing data[1].strip() and then marks.split() — you could simplify and directly
# parse the scores:
# scores = list(map(int, data[1].split()))
# 2. Use sum() Instead of Manual Accumulation
# This is more Pythonic and cleaner:
# total_marks = sum(int(score) for score in marks.split())
# 3. File Encoding (Optional but Safer)
# It's good practice to specify encoding, especially when dealing with diverse systems:
# with open(filename, encoding='utf-8') as f


def extract_student_names_improved(filename):
    result = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            if ":" not in line:
                continue
            name_part, scores_part = line.split(":", maxsplit=1)
            name = name_part.strip()
            scores = list(map(int, scores_part.split()))
            if sum(scores) > 10:
                result.append(name_part.strip())
    return result


print(extract_student_names_improved(filename))
