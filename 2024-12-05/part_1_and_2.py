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


def create_orders(order_rules: list, pages: list) -> dict:
    """Create a dict with the first key:value being the answer for pt1.
    The second key:value contains a list of lists, being the incorrect orders

    Args:
        order_rules (list): From get_codes()
        pages (list): From parse_bottom()

    Returns:
        dict: {pt1_answer: int, incorrect_orders: list of lists}
    """
    middle_num_of_correct_orders = list()
    incorrect_orders = list()
    incorrect_bool_vec = list()
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
        # print(f"vec_bool: {vec_bool}")
        check_val = all(vec_bool)
        # print(f"allowed: {check_val}")
        if check_val:
            middle_val = i[len(i) // 2]
            middle_num_of_correct_orders.append(middle_val)
        else:
            incorrect_orders.append(i)
            incorrect_bool_vec.append(vec_bool)
    ret = {
        "pt1_answer": sum(middle_num_of_correct_orders),
        "incorrect_orders": incorrect_orders,
        "incorrect_bool_vec": incorrect_bool_vec,
    }
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
pt1_num = pt1_sorting["pt1_answer"]
print(pt1_num)

# ----------
# Part 2
# ----------

incorrect_orders = pt1_sorting["incorrect_orders"]


def get_pages_that_cannot_be_after(order_rules: list, single_order: list, page: int):
    pages_not_allowed = [
        x[0] for x in order_rules if (x[1] == page) & (x[0] in single_order)
    ]
    return pages_not_allowed


def reorder_pages(order_rules: list, single_order: list):
    mut_list = single_order.copy()
    for i, page in enumerate(single_order):
        pages_after = single_order[i + 1 :]
        pages_that_cannot_be_after = get_pages_that_cannot_be_after(
            order_rules=order_rules, single_order=single_order, page=page
        )
        num_of_pages_that_cannot_be_after = len(pages_that_cannot_be_after)
        # print({"page": page, "new_pos": num_of_pages_that_cannot_be_after})
        mut_list[num_of_pages_that_cannot_be_after] = page
    return mut_list


corrected_lists = [
    reorder_pages(order_rules=pt1_allowed_orders, single_order=x)
    for x in incorrect_orders
]
pt2_answer = create_orders(pt1_allowed_orders, corrected_lists)
print(pt2_answer)
