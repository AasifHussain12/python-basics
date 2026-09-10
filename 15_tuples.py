#Tuples in Python

print("Tuples in Python")

#Creating a tuple
fruits = ("Apple", "Banana", "Mango", "Orange", "Grapes")

print("\nOriginal tuple of fruits:")
print(fruits)

#Accessing elements in a tuple
print("\nFirst fruit in the tuple:", fruits[0])
print("Last fruit in the tuple:", fruits[-1])

#Length of the tuple
print("\nLength of the tuple:", len(fruits))

#Counting occurrences of an element in a tuple
print("\nCount of 'Banana' in the tuple:", fruits.count("Banana"))

#Finding the index of an element in a tuple
print("\nIndex of 'Mango' in the tuple:", fruits.index("Mango"))

#Iterating through a tuple
print("\nIterating through the tuple of fruits:")
for fruit in fruits:
    print(fruit)
    
#Checking if an element exists in the tuple
item = input("\nEnter a fruit to check if it exists in the tuple: ")
if item in fruits:
    print(item, "exists in the tuple.")
else:
    print(item, "does not exist in the tuple.")
    
print("\nAll tuple operations executed successfully.")