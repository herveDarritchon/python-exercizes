number_max_of_apples = 48
number_of_stacks = 5


def construct_initial_basket():
    apple_basket = []
    for index in range(1, number_max_of_apples + 1):
        item = build_apple_item(index)
        apple_basket.append(item)
    return apple_basket


def build_apple_item(index):
    label = build_apple_label(index)
    apple = {
        "label": label,
        "poisonous": is_poisonous(index)
    }
    return apple


def is_poisonous(index):
    return index < 46


def build_apple_label(index):
    return "Apple n°{}".format(index)


def split_in_5_stacks(basket):
    stacks = []
    stack_size = number_max_of_apples // 5
    current_apple_idx = 0

    for stack_idx in range(0, number_of_stacks - 1):
        stack = []
        for apple_in_stack_idx in range(0, stack_size):
            stack.append(basket[current_apple_idx])
            current_apple_idx = current_apple_idx + 1
        stacks.append(stack)
    stack = []
    while current_apple_idx < number_max_of_apples:
        stack.append(basket[current_apple_idx])
        current_apple_idx = current_apple_idx + 1
    stacks.append(stack)
    return stacks
