import pandas as pd
import numpy as np

input = open("./2024-12-02/input.txt", "r")
input_list = input.read()
input_list_split = input_list.split("\n")

for i in input_list_split:
    as_array = np.array(i.split(" ")).astype(int)
    for pos, value in enumerate(as_array):
        print(pos, value)
