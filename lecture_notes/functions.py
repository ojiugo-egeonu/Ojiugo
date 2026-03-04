                                        #CLASS 5    
#What is a Function?
    # We define a function with, Def then give it a name, then in parenthesis put your input parameters, then add a colon
    # def is_weekend(day):

#Print Statements
def add(a,b):
    print(a+b)
add (1,2)

#Return Statements
def add(a,b):
    return a+b
print(add(1,2))

#Define 
c = add(1,2)
print(c)

#If, Elif, Else
    #if: checks if its true, elif checks if its flase, else catches everything else if none of statements are true
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero" 
print(check_number(1)) #True

#And, Or Conditionals
    #And both conditions met equals True, or one condition met equal True
def can_vote(age, is_citizen):
    if age > 18 and is_citizen:
        print("You can vote!")
    else: 
        print("You cannot Vote")  
can_vote(17, True) #Cannot vote
can_vote(19, True) #Can Vote!

def is_weekend(day):
    if day == "Saturday" or day == "Sunday":
        return "Weekend!"
    else: 
        return "Not Weekend"  
print(is_weekend("Monday")) 

#Loops
l = [1,2,3,4,5]
for number in l:
    print(number)

for i in range (0,5,1):
    print(i)

start = 10
while start > 0:
    print(start)
    start = start - 1
