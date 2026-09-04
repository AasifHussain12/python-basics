print("Strins in Python")

#Taking input from the user
name = input("Enter your full name: ")

print("\nOriginal String:", name)

#String length
print("Length:", len(name))

#Case conversion
print("Upper Case:", name.upper())
print("Lower Case:", name.lower())
print("Title Case:", name.title())
print("Capitalize:", name.capitalize())

#String indexing
print("\nFirst Character:", name[0])  #Positive Indexing
print("Last Character:", name[-1])    #Negative Indexing

#String slicing
print("\nFirst 4 Characters:", name[:4])
print("Last 4 Characters:", name[-4:])

#Searching in a string
print("\nDoes the name contain 'a'?", "a" in name.lower())

#Replacing characters
print("Replace 'a' with '@':", name.replace("a","@"))

#Repeating a string
print("\nRepeated Name:")
print(name * 2)