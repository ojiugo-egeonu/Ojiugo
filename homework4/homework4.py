                                                                    # Lists
#3.1
foods = ["burger", "fries", "pasta", "soup", "veggies"]
print(foods)

#print(foods(1))

#print(foods(-1))

foods.append("rice")
print(foods)

foods.insert(0, "apple")
print(foods)

foods.remove("pasta")
print(foods)

print(len(foods))

foods = ["burger", "fries", "pasta", "soup", "veggies"]

first_last = [foods[0], foods[-1]]
print(first_last)

if "potato" in foods:
    print("A potato!")
else:
    print("No potato!")

#3.2
numbers = list(range(0,21))
print(numbers)

def get_first_15(numbers):
    return numbers[:15]

def get_every_5th(lst):
    return lst[::5]

def reverse_and_stride(lst):
    reversed_list = lst[::-1]
    return reversed_list[::3]

numbers = list(range(0, 21))

step1 = get_first_15(numbers)
step2 = get_every_5th(step1)
step3 = reverse_and_stride(step2)

print(step3)

#3.3
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(numbers)

print(numbers[2])

print(numbers[1][1])

numbers.append([10,11,12])
print(numbers)

def sum_nested(lst):
    total = 0
    for row in lst:
        for num in row:
            total += num
    return total

print(sum_nested(numbers))

#3.4
def create_5x5():
    grid = []
    num = 1
    
    for i in range(5):
        row = []
        for j in range(5):
            row.append(num)
            num += 1
        grid.append(row)
        
    return grid

numbers = create_5x5()
print(numbers)

def replace_multiples_of_3(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] % 3 == 0:
                lst[i][j] = "?"
    return lst

updated_list = replace_multiples_of_3(numbers)
print(updated_list)

def sum_not_question(lst):
    total = 0
    
    for row in lst:
        for item in row:
            if item != "?":
                total += item
                
    return total

result = sum_not_question(updated_list)
print(result)

                                                            # Dictionarys
#4.1
ages = {"Katie": 30,"Mariam": 42,"Safia": 25,"Mira": 48}
print(ages)

print(ages["Katie"])

ages["Mira"] = "100"
print(ages)

ages["Milana"] = 52
print(ages)

del ages["Mariam"]
print(ages)

for key, value in ages.items():
    print(f"{key} = {value}")

#5.2
foods = ["burger", "fries", "pasta", "soup", "veggies"]
print(len(foods))