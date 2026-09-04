print("String Methods")

text = input("Enter a sentence:")

print("\nOriginal String:", text)

#Length of the string
print("Length:", len(text))

#Case conversion
print("Upper Case:", text.upper())
print("Lower Case:", text.lower())
print("Title Case:", text.title())

#Removing whitespace
print("\nString after removing whitespace:", text.strip())

#Find a word in the string
word = input("Enter a word to find in the sentence: ")
print("Position of the word in the sentence:", text.find(word))

#Count Occurrences of a word
count_word = input("Enter a word to count its occurrences in the sentence: ")
print("Occurrences of the word in the sentence:", text.count(count_word))

#Starting and ending of the string
print("Starts with 'Hello': ", text.startswith("Hello"))
print("Ends with '.': ", text.endswith("."))

#Splitting the string into a list of words
words = text.split()
print("\nList of words in the sentence:", words)

#Join Words
joined = "-".join(words)
print("Joined words with '-':", joined)