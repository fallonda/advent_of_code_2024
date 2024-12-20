import re

with open("./2024-12-03/input.txt", "r") as f:
    input_txt = f.read()

# Part 1
mul_patterns = re.findall(pattern="mul\\(\d{1,3},\d{1,3}\\)", string=input_txt)


def get_sum(list_of_mul_patterns: list) -> int:
    # Get the total sum of multiplied patterns.
    # Input is a list of [mul(123,456),...] etc.
    total_sum = 0
    for i in list_of_mul_patterns:
        split_by_comma = i.split(",")
        first_digit = re.search(pattern="\d{1,3}", string=split_by_comma[0]).group(0)
        second_digit = re.search(pattern="\d{1,3}", string=split_by_comma[1]).group(0)
        mult_res = int(first_digit) * int(second_digit)
        total_sum += mult_res
    return total_sum


# Answer part 1
print(get_sum(mul_patterns))

# Part 2
# Append do() and don't() to input txt
pt2_input = "do()" + input_txt + "don't()"
pt2_patterns = re.findall(pattern="do\\(\\)(.*)don't\\(\\)", string=pt2_input)
pt2_patterns_one_string = "".join(pt2_patterns)
pt2_mul_patterns = re.findall(
    pattern="mul\\(\d{1,3},\d{1,3}\\)", string=pt2_patterns_one_string
)
pt2_sum = get_sum(pt2_mul_patterns)
print(pt2_sum)
