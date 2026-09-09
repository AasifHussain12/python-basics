#Lists in Python

print("Lists in Python")

#Creating a list
fruits = ["Apple", "Banana", "Mango", "Orange"]

print("\nOriginal list of fruits:")
print(fruits)

#Accessing elements in a list
print("\nFirst fruit in the list:", fruits[0])
print("Last fruit in the list:", fruits[-1])

#Adding elements to a list
fruits.append("Grapes")
print("\nList after adding Grapes:")
print(fruits)

#Removing elements from a list
fruits.remove("Banana")
print("\nList after removing Banana:")
print(fruits)

#Inerting an element
fruits.insert(1, "Pineapple")
print("\nList after inserting Pineapple at index 1:")
print(fruits)

#List Length
print("\nLength of the list:", len(fruits))

#Iterating through a list
print("\nIterating through the list of fruits:")
for fruit in fruits:
    print(fruit)
    
#Checking if an element exists in the list
item = input("\nEnter a fruit to check if it exists in the list: ")
if item in fruits:
    print(item, "exists in the list.")
else:
    print(item, "does not exist in the list.")
    
print("\nAll list operations executed successfully.")