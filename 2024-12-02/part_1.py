import pandas as pd
import numpy as np

input = open("./2024-12-02/input.txt", "r")
input_list = input.read()
input.close()
input_list_split = input_list.split("\n")

# Part 1
num_safe = 0
allowed_diffs = set([-3, -2, -1, 1, 2, 3])
for i in input_list_split:
    as_array = np.array(i.split(" ")).astype(int)
    diff = list()
    for pos, value in enumerate(as_array[0:-1]):
        diff.append(int(as_array[pos + 1] - as_array[pos]))
    diff_as_set = set(diff)
    if len(diff_as_set.difference(allowed_diffs)) == 0:
        signs = set(np.sign(list(diff_as_set)))
        if len(signs) == 1:
            print(as_array)
            num_safe += 1

# Part 1 answer
print(num_safe)

# Part 2

num_safe = 0
allowed_diffs = set([-3, -2, -1, 1, 2, 3])
for i in input_list_split:
    as_array = np.array(i.split(" ")).astype(int)
    diff = list()
    for pos, value in enumerate(as_array[0:-1]):
        diff.append(int(as_array[pos + 1] - as_array[pos]))
    diff_as_set = set(diff)
    if len(diff_as_set.difference(allowed_diffs)) == 0:
        signs = set(np.sign(list(diff_as_set)))
        if len(signs) == 1:
            print(as_array)
            num_safe += 1
