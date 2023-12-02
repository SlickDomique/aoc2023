import re

condition_string = "12 red, 13 green, 14 blue"
sum_of_all_matching = 0

def extract_values(i):
   output = {}
   for val in i.split(", "):
      output[val.split(" ")[1]] = int(val.split(" ")[0])
   
   return output

def check_has_enough(conditions, values):
   for key, value in values.items(): 
      if value > conditions[key]:
         return False
      
   return True

with open('input') as f:
   conditions = extract_values(condition_string)
   for line in f: 
      id = int(line.split(": ")[0].split(" ")[1])
      has_enough = True
      for toss in line.split(": ")[1].split("; "):
         values = extract_values(toss.replace("\n", ""))
         if not check_has_enough(conditions, values):
            has_enough = False
            break
      if has_enough:
         sum_of_all_matching += id

print(sum_of_all_matching)