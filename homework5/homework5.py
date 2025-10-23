# 3 Homework 1 + 2 Review
# 3.1 Vocabulary Review
'''
1. Git is a program that runs on your computer and allows you to manage code and repositories. GitHub is a platform that allows you to share repositories online, kind of like google drive but for code.
2. The terminal is the program (for me git bash) that opens a window where you can manage code / files. The command line is the place on the terminal where you write commands.
3. A local repository is a folder / project that is saved on your computer, while a remote repository is saved on a server like GitHub.
4. Version control is something that tracks the changes to a file over time so you can revisit its history.
5. The staging area is the area where changes are stored before you do git commit and save changes to your history.
6. Git add is the first command to save work where you add changes to the staging area.
7. Git commit saves the changes in the staging area locally.
8. Git push saves the commited changes remotely.
9. Git status shows the status or the items in a repository and whether those items are modified or staged.
10. Git pull takes changes from a remote repository and merges them with a local repository.
11. Pwd shows you where you are within your repository tree and shows the path to get to your current location.
12. ls shows all the items in the repository you are in.
13. cd is used to switch what directory you are in.
14. nano opens a text editor and can be used to make new files.
15. touch creates new empty files.
16. mv moves or renames files and directories.
17. rm removes files.
18. cat shows the contents of a file in the terminal.
'''

# 3.2 A Directory Tree
'''
1. pwd

2. ls

3. cd ../brianna_repo
git pull

4. mv homework.py ../judy_decal/homework

5. cd ../judy_decal/homework

6. cat homework.py

7. git add .
git commit -m "finished homework"
git push origin main

8. The error means that Judy did not pull all of the most recent changes from git hub before trying to save her work. She should therefore call:
git pull origin main
git push origin main

9. cd ~/Recent
'''


# 4 Homework 3 Review
# 4.1 Data Types
def checkDataType(input):
	return type(input).__name__

# 4.2 Conditionals
def evenOrOdd(number):
	if number % 2 == 0:
		return 'Even'
	else:
		return 'Odd'

# 5 Loops
def sumWithLoop(numbers):
	total = 0
	for number in numbers:
		total += number
	return total

# 6 Homework 4 Review
# 6.1 Lists
def duplicateList(list):
	new_list = []
	for element in list:
		new_list.append(element)
		new_list.append(element)
	return new_list

# 6.2 Debugging
# The function is missing a colon after defining the function. The corrected version would be:
def square(num):
	return num * num

print(evenOrOdd(5))