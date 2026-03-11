# Dictionary
    # A type of list, equipped with keys and values

students = {"name": "Ojiugo", "year": "1", "major": "BioE"}
print(students["major"])

# Change Key

students["major"] = "compsci"
print(students)

# New Key and Value
students["school"] = "UCB"
print(students)

# Delete Key
del students["year"]
print(students)

# Print Keys and Values

print(students.keys())
print(students.values())

for key, value in students.items():
    print(f"{key} = {value}")

#Slicing 
list = [1,2,3,4,5]
print(list[1:4])