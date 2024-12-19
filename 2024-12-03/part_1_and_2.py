import re

with open("./2024-12-03/input.txt", "r") as f:
    input_txt = f.read()

# Part 1
mul_patterns = re.findall(pattern="mul\\(\d{1,3},\d{1,3}\\)", string=input_txt)

total_sum = 0
for i in mul_patterns:
    split_by_comma = i.split(",")
    first_digit = re.search(pattern="\d{1,3}", string=split_by_comma[0]).group(0)
    second_digit = re.search(pattern="\d{1,3}", string=split_by_comma[1]).group(0)
    mult_res = int(first_digit) * int(second_digit)
    total_sum += mult_res
# Answer part 1
print(total_sum)

# Part 2
