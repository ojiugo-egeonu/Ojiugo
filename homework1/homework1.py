                                    # 3.1 Variables and Data Types

a=10
print(a)
print(type(a)) #integrer, number w/o decimals

b=1.5
print(b)
print(type(b)) #float, number with decimals

c=3j
print(c)
print(type(c)) #complex

d="hello"
print(d)
print(type(d)) #string, words

e=[1,2,3]
print(e)
print(type(e)) #list: multiple items in same square brackets

f={"name": "Ojiugo", "favorite fruit": "strawberry"}
print(f)
print(type(f)) #dict

g=(1,2)
print(g)
print(type(g)) #tuple: multiple items in single variable

h=["apple", "bannana", "strawberry"]
print(h)
print(type(h)) #list

i=True
print(i)
print(type(i)) #boolean: represents true/false

j=None
print(j)
print(type(j)) #None type
 
k=[True, "blue", 12]
print(k)
print(type(k)) #list

l=str(14)
print(l)
print(type(l)) #string

m=1e4
print(m)
print(type(m))

n=range(20)
print(n)
print(type(n))

#Questions:
#1. I found 9 different data types
#2. These include: string, float, integer, complex, tuple, boolean, list, None, dict
#3. The variables with the same data types: List - k,h,e and String - l,d
#4. Data type of l = string not integer because str(14) says what are the strings in number 14
#5. n=range(20)

                                        #3.2 Booleans
print("10＞9") #10 greater than 9
print("10==9") #10 isn't equal to 9
print("10<=9") #10 isn't less than or equal to 9
print(bool("abc")) #True
print(bool(123)) #True
print(bool(["apple","cherry","banana"])) #True
print(bool(True)) #True
print(bool(False)) #False
print(bool(0)) #False
print(bool("")) #False
print("hello")
print(bool(" ")) #True
print(bool(())) #False
print(bool([])) #False
print(bool({})) #False
print(bool(True and False)) #False
print(bool(True and True)) #True
print(bool(False and False)) #False
print(bool(True or False)) #True
print(bool(True or True)) #True
print(bool(False or False)) #False
print(bool(not(False))) #True
print(bool(not(True))) #False

#Questions:
#1. Values that are empty come out as false, and values that aren't empty come out as True
#2. bool(" ") came out as True seemingly because a space counts as not empty
#3. True: print(bool(5=5)) because 5 is equal to 5
#4. False: print(bool(5=3)) because 5 isn't equal to five

                                    #3.3 Operators
#3.3.1 Arithmic Operators
print(10+5) #15, addition
print(10-5) #5, subtraction
print(2*4) #8, Multiplication
print(6/3) #2, Division
print(5/2) #2.5, Division
print(3**2) #9, to the power of . . .
print(15//2)

#3.3.2 Comparison Operators
print(5==2) #False, determines equality
print(10 !=10) #False, 10 is not not equal to 10
print(2<5) #True, less than...
print(12>5) #True, greater than ...
print(5<=6) #True, less than or equal to ...
print(1>=10) #False, greater than or equal to ...

#3.3.3 Assignment Operators
x = 5
x += 5
print(x)   # 10, adds 5 to x
x -= 4
print(x)   # 6, subtracts 4 from x
x *= 3
print(x)   # 18, multiplies x by 3

#3.3.4 Logical Operators
#1. Operator and answers true only if both conditions are true. True: print(True and True) False: print(True and False)
#2. Operator or answers true if at least one condition is true. True: print(True or False) False: print(False and False)
#3. Operator not reverses the boolean value. True: print(not False) False:print(not True)

#More Questions
#1. / = division as a float, // = division rounded down to integer
#2. % = remainder of division, // = whole number quotient of division
#3. %, print(10 % 3) = 1
#4. Assignment operators get new values for their variable after applying an operation to them

#3.4 Strings
my_string= "hello"
print(my_string) #Print: "hello"
print(my_string[0]) #Print: h
print(my_string[1]) #Print: e
print(my_string[2]) #Print: l
print(my_string[3]) #Print: l
print(my_string[4]) #Print: o
print(my_string[-1]) #Print: o
print(my_string[1:3]) #Print: el
print(my_string[0:5:2]) #Print: hlo
print(len(my_string)) #Print: 5
print(my_string+"goodbye") #Print: hellogoodbye
print(my_string*7) #Print: hello five times

#Questions:
#1. Slicing is using only a specific part of a string using [] done on my_string [1:3] and [0:5:2]
#2 and 3
name= "Oski"
print("Hello, my name is", name) #Print: Hello, my name is Oski
print(f"Hello, my name is {name}") #Print: Hello, my name is Oski
#4. The first seperates the different values with commas while the second uses an f-string which embeddes the value in the string 

#3.5 Terminal Commands
#cd = change directories
#ls = list files and folders in current working directory
#ls-a = lists all files, including hidden
#mkdir = make a new directory
#cat = displays contents of a file in the terminal
#pwd = print current working directory
#cd .. = moves up one directory level
#cd . = 
#cd ∼ = Changes directory to home directory
#cp = copies files or directories
#mv = moves or renames files and directories
#rm = deletes files or directories 
#clear = clears the terminal screen
#grep = searches for specific text inside files

#Questions
#1. touch: creates a new empty file, echo: prints text/variables to the terminals, man: displays manual for command
#2. ls lists all files and ls -a lists all files even the hidden ones
#3. A hidden file is a file/folder that is not shown by default when you ls in your terminal
#4. grep -i: ignores lowercase/uppercase differences, mkdir -p: creates parent directories if they don't exist, cp -v: shows what files are copied