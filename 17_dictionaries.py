# Dictionaries in Python

print("Dictionaries in Python")

# Creating a dictionary
student = {
    "Name": "Aasif Hussain",
    "Age": 24,
    "Course": "MSc IT",
    "CGPA": 8.2
}

print("\nStudent Dictionary:")
print(student)

# Accessing values
print("\nName:", student["Name"])
print("Course:", student["Course"])

# Adding a new key-value pair
student["University"] = "IUST"

print("\nAfter Adding University:")
print(student)

# Updating a value
student["CGPA"] = 8.5

print("\nAfter Updating CGPA:")
print(student)

# Removing a key
student.pop("Age")

print("\nAfter Removing Age:")
print(student)

# Displaying keys
print("\nDictionary Keys:")
for key in student.keys():
    print(key)

# Displaying values
print("\nDictionary Values:")
for value in student.values():
    print(value)

# Displaying key-value pairs
print("\nDictionary Items:")
for key, value in student.items():
    print(f"{key}: {value}")

# Searching for a key
search_key = input("\nEnter a key to search (Name, Course, CGPA, University): ")

if search_key in student:
    print(f"{search_key}: {student[search_key]}")
else:
    print("Key not found!")

print("\nProgram completed successfully!")