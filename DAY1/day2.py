# Tuples are similar to lists but are immutable (cannot be changed after creation)

# Tuples cannot be changed after creation
student_records = ('Alice', 20, 85.5, "Computer Science")
print(f"Name of Student {student_records[0]}, ")

print("Name:", student_records[0])
print("Age:", student_records[1])

# Tuple unpacking
name, age, score, deparment = student_records
print("\nUnpacked:", name, "is", age, "years old, scored", score, "in", deparment)


# When to use tuples?

# -> Fixed data that shouldn't change
# -> Dectionary keys (lists cannot be keys)
# -> Returning multiple values from a function

# ----- Sets -----

# -> Sets are unordered collections of unique items (no duplicates allowed)
# Sets automatically remove duplicates
course_A = {"Alice", "Bob", "Charlie", "Diana"}
course_B = {"Charlie", "Diana", "Eve", "Frank"}

# Set operations (great for finding overlaps)
print("Students in both courses:", course_A & course_B)
print("Student in either course:", course_A | course_B)
print("Only in Course A:", course_A - course_B)
print("Only in one course:", course_A ^ course_B)

# Removes duplicates from list using set
scores_with_duplicates = [85, 92, 85, 78, 92, 95, 85]
unique_scores = list(set(scores_with_duplicates))
print("Original scores:", scores_with_duplicates)
print("Unique scores:", unique_scores)