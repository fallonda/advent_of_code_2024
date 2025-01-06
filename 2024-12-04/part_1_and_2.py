import re
import numpy as np

with open("./2024-12-04/input.txt", "r") as f:
    input_txt = f.read()
input_split = input_txt.split("\n")

# Part 1


def count_in_list_of_strings(input: list, pattern: str) -> list:
    """Given a list of strings containings the XMAS patterns, eg ["XMASSMAS", "SMXAXMAS"]
    return the number of times the pattern was found.
    """
    func_list = [len(re.findall(pattern=pattern, string=x)) for x in input]
    sum_ret = sum(func_list)
    return sum_ret


# Simple left to right and right to left matching of the input.
num_left_to_right = count_in_list_of_strings(input_split, "XMAS")
num_right_to_left = count_in_list_of_strings(input_split, "SAMX")

# Now go up/down. Transpose the input.
# as np array of characters
np_chars = np.array([[y for y in x] for x in input_split])
np_chars_t = np_chars.transpose()
transposed_list = ["".join(x) for x in np_chars_t]
num_top_to_bottom = count_in_list_of_strings(transposed_list, "XMAS")
num_bottom_to_top = count_in_list_of_strings(transposed_list, "SAMX")

# diagonals
ar_size = len(np_chars)
# Get the diagonals along the bottom left to top_right
bottom_left_to_top_right_diags = [
    np_chars.diagonal(x) for x in range(-ar_size + 1, ar_size)
]
bottom_left_to_top_right_list = ["".join(x) for x in bottom_left_to_top_right_diags]
num_diag_top_left_to_bottom_right = count_in_list_of_strings(
    bottom_left_to_top_right_list, "XMAS"
)
num_diag_bottom_right_to_top_left = count_in_list_of_strings(
    bottom_left_to_top_right_list, "SAMX"
)
# Get the diagonals along the other axis
np_chars_flipped = np.fliplr(np_chars)
diags_on_flip = [np_chars_flipped.diagonal(x) for x in range(-ar_size + 1, ar_size)]
diags_on_flip = ["".join(x) for x in diags_on_flip]
num_top_right_to_bottom_left = count_in_list_of_strings(diags_on_flip, "XMAS")
num_bottom_left_to_top_right = count_in_list_of_strings(diags_on_flip, "SAMX")
total_pt1 = sum(
    [
        num_left_to_right,
        num_right_to_left,
        num_top_to_bottom,
        num_bottom_to_top,
        num_diag_top_left_to_bottom_right,
        num_diag_bottom_right_to_top_left,
        num_top_right_to_bottom_left,
        num_bottom_left_to_top_right,
    ]
)
print(total_pt1)

# Part 2
windows = np.lib.stride_tricks.sliding_window_view(np_chars, window_shape=(3, 3))
windows_long = np.concatenate(windows, axis=0)
counter = 0

for pos, value in enumerate(windows_long):
    original_diags_bool = all(value.diagonal() == np.array(["M", "A", "S"])) | all(
        value.diagonal() == np.array(["S", "A", "M"])
    )
    flip_array = np.fliplr(value)
    flipped_diags_bool = all(flip_array.diagonal() == np.array(["M", "A", "S"])) | all(
        flip_array.diagonal() == np.array(["S", "A", "M"])
    )
    if original_diags_bool & flipped_diags_bool:
        counter += 1

print(counter)
