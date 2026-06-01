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

# ----- Dictionaries -----
# 
# -> Dictionaries sore key-value pairs and are very useful for structured data
# # Dictionaries store data with keys

student = {
    "name": "Alice",
    "age": 20,
    "scores": [85, 98, 72],
    "departmentt": "Computer Science",
    "is_active": True
}

print("Student Dictonary:")
print(student)

# Accessing values
print("Studentt name:", student['name'])
print('Student scores:', student['scores'])
print("Average scores:", sum(student['scores'])/len(student['scores']))

# Student's Dictionaries

college = {
    "name": "Sahid Smarak College",
    "Address": "Kirtipur",
    "faculty": {
        "BCA": {
            "sem1": 20
        },
        "BM": {
            "sem2": 15
        },
        "BBA": {
            "sem3": 30
        }
    }
}

print(college)
print(f"Name of College: {college['name']}")
print(f"Address of College: {college['Address']}")
print(f"faculty of college: {college['faculty']}")
print(f"example: {college['faculty']['BCA']['sem1']}")

# Adding/ updating values

student['grade'] = "A"
student ['age'] = 21
print("After update:", student)

score = [score for score in student['scores'] if score > 80]
print(f"score of student > 80: {score}.")

"Looping through dictionaries"
for key, value in student.items():
    print(" ", key, ":", value)

# Dictionary comprehension
# scores_dict = {}
# for i in range(1, 6):
#     scores_dict["Student_" + str(i)] = np.random.randint(60, 100)
# print("\nGenerated scores:", scores_dict)# Dictionary comprehension
# scores_dict = {}

# ----- Conditional Statement -----
# Function to determine grade based on score
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "Invalid"
# Test the function

# Test the function
test_scores = [95, 85, 75, 65, 55]
for score in test_scores:
    grade = get_grade(score)
    print("Score:", score, "→ Grade:", grade)

# Multiple conditions
def check_eligibility(score, attendance):
    if score >= 60 and attendance >= 75:
        return "Eligible for exam"
    elif score >= 60 and attendance < 75:
        return "Low attendance - Not eligible"
    elif score < 60 and attendance >= 75:
        return "Low score - Need improvement"
    else:
        return "Not eligible - Both score and attendance low"

print("\nEligibility Check:")
print("Score 85, Attendance 80%:", check_eligibility(85, 80))
print("Score 85, Attendance 70%:", check_eligibility(85, 70))
print("Score 55, Attendance 80%:", check_eligibility(55, 80))