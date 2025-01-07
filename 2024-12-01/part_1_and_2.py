import pandas as pd
import os

os.listdir()

input = pd.read_csv("./part_1_input.txt", sep="   ", header=None)

first_series = input[0].sort_values(ignore_index=True)
second_series = input[1].sort_values(ignore_index=True)

difference = abs(second_series - first_series)

sum_difference = sum(difference)

# Part 1 answer
print(sum_difference)

# Part 2
cumul_sim_score = 0
for i in first_series:
    sim_score = i * sum(second_series == i)
    cumul_sim_score += sim_score

# Part 2 answer
print(cumul_sim_score)
