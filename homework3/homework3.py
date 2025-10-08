# homework3.py
# 3. Print Functions
# 3.1 Say Goodbye
def say_goodbye(name):
	print("goodbye,", name)

# 3.2 Area of a Circle
def area_of_circle(radius):
	pi = 3.14
	print(pi * radius**2)

# 4. Return Functions
# 4.1 Subtract, Multiply, and Divide
def subtract(a, b):
	return a - b

def multiply(a, b):
	return a * b

def divide(a, b):
	return a / b

# 5. Conditionals
# 5.1 What Should I Wear?
def temp_range(readings):
	lowest = min(readings)
	highest = max(readings)
	return (lowest, highest)

# 5.2 Check if it's the Weekend
def is_weekend(day):
	if day == 6 or day == 7:
		return True
	else:
		return False

# 5.3 Fuel Efficiency Calculator
def fuel_efficiency(miles, gallons):
	return miles / gallons

# 5.4 Secret Code
def encryption(data):
	last_digit = data % 10
	rest_of_number = data // 10
	number_of_digits = len(str(rest_of_number))
	return last_digit * (10 ** number_of_digits) + rest_of_number

# 6. Loops
# 6.1 Oski Stole Your Power
def power(x, y):
	answer = 1
	for i in range(y):
		answer *= x
	return answer

# 6.2 Min and Max Loops
# 6.2.1 For Loops
def minimum(numbers):
	min_value = numbers[0]
	for number in numbers:
		if number < min_value:
			min_value = number
	return  min_value

def maximum(numbers):
	max_value = numbers[0]
	for number in numbers:
		if number > max_value:
			max_value = number
	return max_value

# 6.2.2 While Loops
def minimum2(numbers):
	a = 0
	minimum_value = numbers[0]
	while a < len(numbers):
		if numbers[a] < minimum_value:
			minimum_value = numbers[a]
		a += 1
	return minimum_value

def maximum2(numbers):
	a = 0
	maximum_value = numbers[0]
	while a < len(numbers):
		if numbers[a] > maximum_value:
			maximum_value = numbers[a]
		a += 1
	return maximum_value

# 6.3 Calculate the Sum
def sum_of_digits(number):
	sum = 0
	for digit in str(number):
		sum += int(digit)
	return sum

# Running Your Script
integer = 43265
result = sum_of_digits(integer) # sum of the digits in 43265
print(f"The result of Calculate the Sum (6.3) with integer = {integer} is {result}.")
