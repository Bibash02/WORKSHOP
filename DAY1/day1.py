# print('hello world')

# --------- Variables --------
name = "RAM"
faculty = 'Computer Science'
dob = "01/01/2020"
print("Hello, " + name + ".") # string concatination

# print multiple variables using + sign 
print("Hello, "+ name + "."+ "You are a student of "+ faculty + " and your date of birth is "+ dob + ".")

# f -> f refers to f-string (formatted string literals)
print(f"Hello {name}.")


# print multiple variables using f string
print(f"Hello {name}. You are a student of {faculty} and you date of birth is {dob}.")

# ------ Data Types ------
age = 20
number = 56.3
hello = True

print(f"Type of name: {type(name)}")
print(f"Type of age: {type(age)}")
print(f"Type of number: {type(number)}")
print(f"Type of hello: {type(hello)}")

# ----- Swap Variables easily -----
x, y = 10, 20
print(f"Before swap: x = {x} and y = {y}")
x, y = y, x
print(f"After swap: x = {x} and y = {y}")

# ----- Unpack lists -----
student_info = ["Charlie", 21, 80.0]
name, age, score = student_info
print(f"Unpacked: {name, age, score}")

name1, *others = student_info
print("Name:", name1) # This will be a list containing name
print("Others:", others) # this will be a list containing age and score


# ----- Creating lists ------

student_names = ['Alice', 'Bob', 'Charlie', "Diana"]
student_numbers = [85, 92, 78, 95]
print(f"Student names: {student_names}.")
print(f"Student numbers: {student_numbers}")

# Accessing elements (indexing starts at 0)
print(f"First Student: {student_names[0]}") # First student
print(f"Last student name:{student_names[-1]}") # Last Student
print(f"First three student name: {student_names[0:3]}") # First three student
print(f"Student from index 1 to end: {student_names[:]}") # All students getting first to last
print(f"Student ignore by space: {student_names[::2]}") # Ignore two spaces names

# ----- List Operations -----
student_names.append("Eve") # append -> Add t end
print(f"After adding name: {student_names}")


student_names.insert(1, "Frank") # insert -> Insert at position in list
print(f"After insert name: {student_names}")

student_names.remove("Bob") # remove -> Remove the values from list
print(f"After removing Bob: {student_names}")

# List compreshension (powerful feature)
passing_scores = [score for score in student_numbers if score >= 80]
print("\nPassing scores (>=80):", passing_scores)

# ----- Common methods -----
print('NUmber of students:', len(student_names))
print("Higher student score:", max(student_numbers))
print("Lowest student score:", min(student_numbers))

