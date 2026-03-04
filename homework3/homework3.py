#3.1 Say Googbye
#def say_goodbye(ojiugo):
    #print("Goodbye", ojiugo)   
 
#say_goodbye(ojiugo)

#3.2 Area of Circle
def area_of_circle(radius):
    area = 3.14 * radius ** 2
    print(area)

area_of_circle(5)   

#4.1 Subtract, Multiply and Divide
def add(a,b):
    return a + b
print(add(1,2))

def subtract(a,b):
    return a - b
print(subtract(1,2))

def multiply(a,b):
    return a * b
print(multiply(1,2))

def divide(a,b):
    return a / b
print(divide(1,2))

#5.1 What Should I Wear?
def min_max_temperatures(readings):
    return (min(readings), max(readings))

readings = [15, 14, 17, 20, 23, 28, 20]

print(min_max_temperatures(readings))

#5.2 Check if it's the Weekend
Monday = 1
Tuesday = 2
Wednesday = 3
Thursday = 4
Friday = 5
Saturday = 6
Sunday = 7
def is_weekend(day):
    if day == "6" or day == "7":
        return "Weekend!"
    else: 
        return "Not Weekend"  
print(is_weekend("Thursday")) 

#5.3 Fuel Efficiency Calculator
def fuel_efficiency(distance, fuel):
    return distance / fuel
mpg = fuel_efficiency(300, 10)
print(mpg)

#5.4 Secret Code
def secret_code(num):
    last_digit = num % 10
    rest = num // 10
    multiplier = 10 ** len(str(rest))
    return last_digit * multiplier + rest

print(secret_code(12345))

#6.1 Oski Stole Your Power
def power(x, y):
    result = 1
    for i in range(y):
        result *= x
    return result

print(power(2, 3))

#6.2.1
def min_for(numbers):
    smallest = numbers[0]
    
    for num in numbers:
        if num < smallest:
            smallest = num
            
    return smallest

def max_for(numbers):
    largest = numbers[0]
    
    for num in numbers:
        if num > largest:
            largest = num
            
    return largest

#6.2.2
def min_while(numbers):
    smallest = numbers[0]
    i = 0
    
    while i < len(numbers):
        if numbers[i] < smallest:
            smallest = numbers[i]
        i += 1
        
    return smallest

def max_while(numbers):
    largest = numbers[0]
    i = 0
    
    while i < len(numbers):
        if numbers[i] > largest:
            largest = numbers[i]
        i += 1
        
    return largest

nums = [15, 14, 17, 20, 23, 28, 20]

print(min_for(nums))
print(max_for(nums))
print(min_while(nums))
print(max_while(nums))

#6.2.3
def sum_of_digits(num):
    total = 0
    
    while num > 0:
        digit = num % 10
        total += digit
        num = num // 10
        
    return total

print(sum_of_digits(2468))

#7.1
day = 6   # Saturday

result = is_weekend(day)

print(f"The result of Check if it's the Weekend (5.2) with day = {day} is {result}.")