number_max_of_apples = 48
number_of_stacks = 5
stack_size = number_max_of_apples // 5


def construct_initial_basket():
    return [_build_apple_item(index + 1) for index in range(number_max_of_apples)]


def _build_apple_item(index):
    label = _build_apple_label(index)
    apple = {
        "label": label,
        "poisonous": _is_poisonous(index)
    }
    return apple


def _is_poisonous(index):
    return index < 46


def _build_apple_label(index):
    return "Apple n°{}".format(index)


def split_in_5_stacks(basket):
    stacks = [[basket[_compute_index(stack, index)] for index in range(stack_size)] for stack in
              range(number_of_stacks)]

    for idx in range((stack_size * number_of_stacks), number_max_of_apples):
        stacks[4].append(basket[idx])
    return stacks


def _compute_index(stack, index):
    return stack * stack_size + index


def shuffle_and_flatten(stacks):
    shuffled_basket = [stacks[stack_idx] for stack_idx in [4, 0, 2, 1, 3]]
    return [val for sublist in shuffled_basket for val in sublist]


def main():
    basket = construct_initial_basket()
    for step in range(0, 102):
        stacks = split_in_5_stacks(basket)
        basket = shuffle_and_flatten(stacks)
        print("step:", step, basket, "p21", basket.index({'label': 'Apple n°21', 'poisonous': True}),
              "p31", basket.index({'label': 'Apple n°31', 'poisonous': True}),
              "p8", basket.index({'label': 'Apple n°8', 'poisonous': True}))


if __name__ == "__main__":
    # execute only if run as a script
    main()
