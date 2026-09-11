# Sets in Python

print("Sets in Python")

# Creating a set
fruits = {"Apple", "Banana", "Mango", "Orange"}

print("\nOriginal Set:")
print(fruits)

# Adding an element
fruits.add("Grapes")
print("\nAfter Adding Grapes:")
print(fruits)

# Removing an element
fruits.remove("Banana")
print("\nAfter Removing Banana:")
print(fruits)

# Length of the set
print("\nTotal Fruits:", len(fruits))

# Checking if an item exists
item = input("\nEnter a fruit to search: ")

if item in fruits:
    print(item, "is available in the set.")
else:
    print(item, "is not available in the set.")

# Another set
more_fruits = {"Pineapple", "Mango", "Apple"}

print("\nAnother Set:")
print(more_fruits)

# Union
print("\nUnion:")
print(fruits.union(more_fruits))

# Intersection
print("\nIntersection:")
print(fruits.intersection(more_fruits))

# Difference
print("\nDifference:")
print(fruits.difference(more_fruits))

print("\nProgram completed successfully!")