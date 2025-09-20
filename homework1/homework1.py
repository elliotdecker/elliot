# File: homework1.py
# -- Variables and Data Types --
a=10
print(a)
print(type(a))
# a is an integer, a whole number with no decimals
b=1.5
print(b)
print(type(b)) # b is a float, which is a number that is a decimal or fraction
c=3j
print(c)
print(type(c)) # c is a complex, which is when multiple different types of data types are combined
d="hello"
print(d)
print(type(d)) # d is a string, which means it is composed of characters / words
e=[1,2,3]
print(e)
print(type(e)) # e is a list, which means it is a list of ordered things
f={"name":"Ellen","favorite fruit":"strawbery"}
print(f)
print(type(f)) # f is a dict, short for dictionary, which is a data type that stores listed in formation in pairs
g=(1,2)
print(g)
print(type(g)) # g is a tuple, which is like a list except once you have created it you cannot edit the items it contains
h=["apple","banana","strawberry"]
print(h)
print(type(h)) # h, like e, is also a list because it is a list of ordered items
i=True
print(i)
print(type(i)) # i is a bool, which means it is one of two possible values (either true or false)
j=None
print(j)
print(type(j)) # j is a nonetype datatype, meaning it is something that has no value
k=[True,"blue",12]
print(k)
print(type(k)) # k is also a list because it contains an assorted list of different ordered things
l=str(14)
print(l)
print(type(l)) # l is a string, because while 14 is a number, the str command converted the value to be a string data type
m=1e4
print(m)
print(type(m)) # m is a float, because it is scientific notation of the number 10,000. Because it is in scientific notation, though, it is a float not an integer.
# 1. I found 9 different data types.
# 2. int, float, complex, str, list, dict, tuple, bool, and NoneType
# 3. b and m are floats, d and l are strings, e, h, and k are lists
# 4. l is a string, not an integer, because str() makes the data contained in it a string
# 5.
x=range(4)
print(x)
print(type(x)) # x is a range data type, meaning it represents a range of values with an upper and lower bound
# -- Booleans --
print(10>9) # true, 10 is greater than 9
print(10==9) # false, 10 does not equal 9
print(10<=9) # false, 10 is not less than or equal to 9
print(bool("abc")) # true, a string data type is true
print(bool(123)) # true, an integer data type is true
print(bool(["apple","cherry","banana"])) # true, a list data type is true
print(bool(True)) # true, the word true represents something true
print(bool(False)) # false, the word false is used to represent something false
print(bool(0)) # false, meaning the value 0 represents something being false
print(bool("")) # false, meaning if quotes are empty then like 0 the value is false
print(bool(" ")) # true, meaning a space within the quotation is enough to make it true
print(bool(())) # false, meaning when there is no values in the parenthesis it is considered false
print(bool([])) # false, same as parenthesis and quotations
print(bool({})) # false, same as above
print(bool(True and False)) # false, meaning false overwrites true
print(bool(True and True)) # true, multiple trues are true
print(bool(False and False)) # false, multiple falses are false
print(bool(True or False)) # true, when it is or not and, true overwrites false
print(bool(True or True)) # true, multiple trues are true
print(bool(False or False)) # false, multiple falses are false
print(bool(not(False))) # true, something not false is true
print(bool(not(True))) # false, something not true is false
# I notice that empty things are considered false, whereas mostly everything else is true.
# I was surprised that True and False is false, but True or False is true
print(9==9) # This is true because the expression is true mathematically
print(1>1) # This is false because the expression is not true mathematically
# -- Operators --
# - Arithmetic Operators -
print(10+5) # 15, + performs addition
print(10-5) # 5, - performs subtraction
print(2*4) # 8, * performs multiplication
print(6/3) # 2.0, / performs division
print(5%2) # 1, % gives the remainder when the first number is divided by the second
print(3**2) # 9, ** raises the first number to the power of the second
print(15//2) # 7, // represents division where it rounds to the next smaller integer
# - Comparison Operators -
print(5==2) # False, == tells you if two values are equal or not
print(10!=10) # False, != tells you if if two values are different, if they are the same it is false
print(2<5) # True, < tells you if the first number is smaller than the second
print(12>5) # True, > tells you if the first number is greater than the second
print(5<=6) # True, <= tells you if the first number is less than or equal to the second
print(1>=10) # False, >= tells you if the first number is greater than or equal to the second
# - Assignments Operators -
x=5
x+=5
print(x) # 10, += adds the second value to the variable and stores the variable as the result
x-=4
print(x) # 6, -= subtracts the second value from the varaible and stores the variable as the new result
x*=3
print(x) # 18, *= multiplies the second value by the variable and stores the variable as the new result
# - Logical Operators -
# 1. The operator and returns the expression as true only if both parts are true.
print(10==5+5 and 5==5) # True
print(10==5+5 and 5==4) # False
# 2. The operator or returns the expression as true if at least one of the parts are true.
print(10==5+5 or 5==4) # True
print(10==2 or 2==3) # False
# 3. The not operator returns the opposite answer as the same expression without not
print(not 10==2*2+6) # False
print(not 10==2) # True
# - More Questions -
# 1. / divides the two terms and // divides the two terms but rounds the answer down to the next smaller integer
# 2. % gives the remainder when the first term is divided by the second
# 3. I would use the % operator. For example, print(10%3) gives 1 because the remainder is 1.
# 4. Assignment operators perform an operation on a preexisting variable and change that original variable to be the new answer.
# -- Strings --
my_string="hello"
print(my_string) # prints: hello
print(my_string[0]) # prints: h
print(my_string[1]) # prints: e
print(my_string[2]) # prints: l
print(my_string[3]) # prints: l
print(my_string[4]) # prints: o
print(my_string[-1]) # prints: o
print(my_string[1:3]) # prints: el
print(my_string[0:5:2]) # prints: hlo
print(len(my_string)) # prints: 5
print(my_string+"goodbye") # prints: hellogoodbye
print(7*my_string) # prints: hellohellohellohellohellohellohello
# - Questions -
# 1. Slicing is when you get specific values from a string. I sliced my string when I put square brackets next to my_string, and specified which characters I wanted.
name="oski"
print("hello, my name is", name)
# 2. Doing that printed: hello, my name is oski
print(f"hello, my name is {name}")
# 3. Doing that printed: hello, my name is oski
# 4. The second printed statement is an f-string, which is a way to embed a variable in a string using curly brackets instead of using a comma.
# -- Terminal Commands --
# cd
# changes directories. Use it to move between folders
# ex: cd Desktop
# ls
# list: shows the files and folders in the current directory
# ex: ls
# ls -a
# list all: shows all the files in the current directory including hiddne ones
# ex: ls -a
# mkdir
# make directory: this command allows you to create folders in your current directory
# ex: mkdir somethingsometing_folder
# cat
# concatenate: shows the contents of a file
# ex: cat somethingfile.txt
# pwd
# print working directory: this shows you the full path to get to the directory you are in
# ex: pwd
# cd ..
# This command changes directories to the directory that the current directory is inside
# ex: cd ..
# cd .
# This command keeps you in the directory that your already in
# ex: cd .
# cd ~
# This command brings you to the home directory
# ex: cd ~
# cp
# copy: this command is used to copy folders or files from one place to another
# ex: cp filelbeh.txt blahblhbalhb_txt
# mv
# move: this command moves a file or folder to a new location
# ex: mv blahlewih.txt /User/gibbons/
# rm
# remove: deletes files and directories
# ex: rm trashfile.png
# clear
# this command clears the terminal of your past commands
# ex: clear
# grep
# this command is used to search for specific text inside files
# ex: grep "trail_mix" yummyfood.txt
# - Questions -
# 1.
# touch: this command creates a new blank file or updates the timestamp of a current file. ex: touch alalal.txt
# head: shows the first 10 lines of a file. ex: head ghtututu.txt
# tail: shows the last 10 lines of a file. ex: tail zoxow.txt
# 2. both commands list the folders and files in a directory but ls -a also shows hidden files while ls doesn't
# 3. a hidden file is a file that starts with a . and doesn't normally show up in the contents of a directory
# 4.
# ls -lh: the -lh makes the long form of a file or direcotry easily readable in a list. ex: ls -lh wreezer.txt
# rm -f: the -f makes it so that you can remove files without having to be asked for confirmation. ex: rm -f badfile.png
# grep -r: the -r makes it so that the command looks for specific characters in all the directories and files within the current directory. ex: grep -r "buenisosos"