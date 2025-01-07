import random

# Try the example input in the question
with open("./2024-12-05/test_input.txt", "r") as f:
    example_input_txt = f.read()

example_split_top_and_bottom = example_input_txt.split("\n\n")


def get_codes(input: str) -> list:
    """Get the allowed patterns as a list of tuples.

    Args:
        input (str): The top half of the input text.

    Returns:
        list: list of tuples of the allowed codes. E.g. [(1,2), (3,4)]
    """
    split_by_line_end = input.split("\n")
    ret = [tuple([int(y) for y in x.split("|")]) for x in split_by_line_end]
    return ret


example_allowed_orders = get_codes(example_split_top_and_bottom[0])


def parse_bottom(input: str) -> list:
    """Format the bottom half of the input into a list of lists.

    Args:
        input (str): The bottom half of the input

    Returns:
        list: list of lists (ints).
    """
    split_by_line_end = input.split("\n")
    as_int_list = [[int(y) for y in x.split(",")] for x in split_by_line_end]
    return as_int_list


example_bottom = parse_bottom(example_split_top_and_bottom[1])


def create_orders(order_rules: list, pages: list) -> list:
    middle_num_of_correct_orders = list()
    incorrect_orders = list()
    for i in pages:
        # print(f"page_instructions: {i}")
        page_orderings = list()
        list_to_pop = i.copy()
        while len(list_to_pop) > 0:
            popped_val = list_to_pop.pop(0)
            for k in list_to_pop:
                to_append = tuple([popped_val, k])
                page_orderings.append(to_append)
        # print(f"page_orderings: {page_orderings}")
        # Check that the page orders are allowed
        vec_bool = [(x in order_rules) for x in page_orderings]
        print(f"vec_bool: {vec_bool}")
        check_val = all(vec_bool)
        # print(f"allowed: {check_val}")
        if check_val:
            middle_val = i[len(i) // 2]
            middle_num_of_correct_orders.append(middle_val)
        else:
            incorrect_orders.append(i)
    ret = [sum(middle_num_of_correct_orders), incorrect_orders]
    return ret


example_sorting = create_orders(
    order_rules=example_allowed_orders, pages=example_bottom
)
example_num = example_sorting[0]
print(example_num)

# Try part 1
with open("./2024-12-05/input.txt", "r") as f:
    input_txt = f.read()
pt1_split_top_and_bottom = input_txt.split("\n\n")

pt1_allowed_orders = get_codes(pt1_split_top_and_bottom[0])
pt1_bottom = parse_bottom(pt1_split_top_and_bottom[1])
pt1_sorting = create_orders(order_rules=pt1_allowed_orders, pages=pt1_bottom)
pt1_num = pt1_sorting[0]
print(pt1_num)

# Part 2
# Try on the example input
