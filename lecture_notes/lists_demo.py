#Lists
    # A collection of items stored in a single variable
    # Ordered, but can be changed unlike tuples
    # Python starts counting at 0
        # fruits = ["apple", "banana", "cherry"]
        # apple = 0, etc

fruits = ["apple", "banana", "cherry"]
print(fruits)

numbers = [1,2,3,4,5]
print(numbers)

mixed = ["hello", "5", "True", "None"]
print(mixed)

# Printing out single elements
#print(fruits(1))
#print(numbers(2))
#print(mixed(-2))

# Changing elements
#fruits[0]= "grape"
#print(fruits)

# Add to List
#print(numbers)
#numbers.append(7)
#print(numbers)

#print(mixed)
#mixed.insert(1, False)
#print(mixed)

# Remove from List
print(fruits)
#fruits.remove("banana")
#print(fruits)

fruits.pop(0)
print(fruits)

for fruits in fruits:
    print(fruits)
