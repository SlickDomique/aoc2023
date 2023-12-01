import re

regex = re.compile("\d")
sum_of_all = 0
with open('input') as f:
	for line in f: 
		numbers = regex.findall(line)
		sum_of_all = sum_of_all + int(numbers[0] + numbers[-1])
  
print(sum_of_all)