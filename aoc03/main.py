import re

sum_of_all_matching = 0

text_file = open("input", "r")
lines =  [line.rstrip() for line in text_file.readlines()]
text_file.close()

number_is_valid = False
parsed_temp = ""

gear_positions = []

def is_symbol_valid(x, y, check_for_gear = False):
	has_number_for_gear = False
	for checking_x in range(-1, 2, 1):
		for checking_y in range(-1, 2, 1):
			if ((checking_x == 0 and checking_y == 0) or
					checking_x + x < 0 or 
					checking_y + y < 0 or
					checking_x + x >= len(lines[0]) or
					checking_y + y >= len(lines)
				): 
				continue

			checked_char = lines[y + checking_y][x + checking_x]
			if check_for_gear:
				if checked_char.isdigit():
					if has_number_for_gear:
						return True
					has_number_for_gear = True
			else:
				if not checked_char.isdigit() and checked_char != ".":
					return True

	return False

def parse_all_numbers_around(x, y): 
	numbers = []
	parsed_temp = ""
	started_pos = -1

	if y > 0: 
		for pos, char in enumerate(lines[y - 1]):
			if char.isdigit():
				if started_pos == -1:
					started_pos = pos
				parsed_temp += char
			if not char.isdigit() or pos == len(lines[y-1]) - 1:
				if len(parsed_temp) > 0:
					if (
						(started_pos < x and started_pos + len(parsed_temp) > x - 1) or
						started_pos == x or 
						started_pos == x + 1
					):
						numbers.append(int(parsed_temp))
					started_pos = -1
				parsed_temp = ""
	
	if (x > 0 and lines[y][x - 1].isdigit()):
		parsed_temp = ""
		for i in range(x - 1, -1, -1):
			if lines[y][i].isdigit():
				parsed_temp += lines[y][i]
			if not lines[y][i].isdigit() or i == 0:
				numbers.append(int(parsed_temp[::-1]))
				parsed_temp = ""
				break

	if (x < len(lines[y]) and lines[y][x + 1].isdigit()):
		parsed_temp = ""
		for i in range(x + 1, len(lines[y]), 1):
			if lines[y][i].isdigit():
				parsed_temp += lines[y][i]
			if not lines[y][i].isdigit() or i == len(lines[y]) - 1:
				numbers.append(int(parsed_temp))
				parsed_temp = ""
				break

	parsed_temp = ""
	started_pos = -1
	if y < len(lines):
		for pos, char in enumerate(lines[y + 1]):
			if char.isdigit():
				if started_pos == -1:
					started_pos = pos
				parsed_temp += char
			if not char.isdigit() or pos == len(lines[y-1]) - 1:
				if len(parsed_temp) > 0:
					if (
						(started_pos < x and started_pos + len(parsed_temp) > x - 1) or
						started_pos == x or 
						started_pos == x + 1
					):
						numbers.append(int(parsed_temp))
					
					started_pos = -1
				parsed_temp = ""
	
	return numbers

def not_parsing_number():
	global number_is_valid
	global parsed_temp
	global sum_of_all_matching

	if number_is_valid:
		sum_of_all_matching += int(parsed_temp)
	parsed_temp = ""
	number_is_valid = False

for y, line in enumerate(lines):
	not_parsing_number()
	for x, char in enumerate(line):
		if char == "*" and is_symbol_valid(x, y, True): 
			gear_positions.append({
				"x": x,
				"y": y,
			})

		if char.isdigit():
			parsed_temp += char

			if not number_is_valid:
				number_is_valid = is_symbol_valid(x, y)
		else:
			not_parsing_number()

sum_of_gears = 0

for gear in gear_positions:
	numbers = parse_all_numbers_around(gear["x"], gear["y"])
	print(numbers)
	if len(numbers) == 2:
		print(numbers)
		sum_of_gears = sum_of_gears + numbers[0] * numbers[1]
	

print(sum_of_all_matching)
print(sum_of_gears)