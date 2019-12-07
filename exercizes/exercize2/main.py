number_of_elt = 90


def popule_circle_for(size):
    return [n + 1 for n in range(size)]


def __compute_idx_elt_to_delete(start_elt_idx, off_set_elt, elements):
    size = len(elements)
    elt_idx = (start_elt_idx + off_set_elt) % size
    return elt_idx


def suppress_an_elt(start_elt_idx, off_set_elt, elements):
    idx_elt_to_suppress = __compute_idx_elt_to_delete(start_elt_idx, off_set_elt, elements)
    elt_to_extract = elements.pop(idx_elt_to_suppress)

    return idx_elt_to_suppress, elt_to_extract, elements


def main():
    remaining_list = []
    current_list = popule_circle_for(number_of_elt)
    start_elt_idx = 0
    elt = 1
    while len(current_list) != 1:
        start_elt_idx, elt, remaining_list = suppress_an_elt(start_elt_idx, elt - 1, current_list)
    print("last_elt = ", remaining_list[0])


if __name__ == "__main__":
    # execute only if run as a script
    main()
