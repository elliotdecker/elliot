# 3 Lists
# 3.1 List Operations
favorite_foods = ["pancakes","steak","burrito","pasta","seaweed"]

print(favorite_foods[1])

print(favorite_foods[-1])

favorite_foods.append("brownies")

favorite_foods.insert(0, "apple")

# I got the error:
# TypeError: insert expected 2 arguments, got 1
# I originally wrote: favorite_foods.insert("apple")
# I forgot to include the place in the list I wanted apple to be inserted, which I amended by changing it to: favorite_foods.insert(0, "apple")

del favorite_foods[2]

print(len(favorite_foods))

for food in favorite_foods:
	print(food.upper())

first_last_foods = [favorite_foods[0], favorite_foods[-1]]

if "potato" in favorite_foods:
	print("A potato!")
else:
	 print("No potato!")

# I encountered the error:
# SyntaxError: expected ':'
# I originally wrote else print("No potato!")
# I forgot to put the print statement in another indented line, and forgot to add a : after else

# 3.2 Slicing and Striding
numbers = list(range(0,21))

def get_first_15(numbers):
	return numbers[:15]
print(get_first_15(numbers))
def get_every_5th(lst):
	return lst[::5]
print(get_every_5th(numbers))
# I encounted this error:
# SyntaxError: invalid decimal literal
# I originally misread the question and thought it said 1st instead of lst
# Python doesn't allow variables to begin with a number, so I fixed it by changing the 1 to an l

def reverse_and_stride(lst):
	return lst[::-1]
print(reverse_and_stride(numbers))
# 3.3 Nest Lists
numbers = [[1, 2, 3], [4, 5, 6,], [7, 8, 9]]

print(numbers[2])

numbers.append([10, 11, 12])

def sum_nested(list):
	total = 0
	for row in list:
		for number in row:
			total += number
	return total
print(sum_nested(numbers))

# 3.4 Create a 5x5 List
def make_5x5():
	numbers = []
	count = 1
	for i in range(5):
		row = []
		for j in range(5):
			row.append(count)
			count += 1
		numbers.append(row)
	return numbers
five_by_five = make_5x5()
print(five_by_five)

def replace_multiples_of_3(list):
	updated = []
	for row in list:
		new_row = []
		for num in row:
			if num % 3 == 0:
				new_row.append("?")
			else:
				new_row.append(num)
		updated.append(new_row)
	return updated
updated = replace_multiples_of_3(five_by_five)
print(updated)

def sum_of_not_question_marks(list):
	total = 0
	for row in list:
		for item in row:
			if item != "?":
				total += item
	return total

sum = sum_of_not_question_marks(updated)
print(sum)

#4 Dictionaries
#4.1 Dictionary Operations
ages = {"Katie": 30,"Mariam": 42,"Safia": 25,"Mira": 48}

print(ages["Katie"])

ages["Mira"] = 100

ages["Milana"] = 52

del ages["Mariam"]

for name, age in ages.items():
	print(name, "is", age)

print(make_5x5())

print(get_first_15(numbers))
