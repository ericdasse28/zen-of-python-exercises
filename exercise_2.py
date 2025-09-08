"""There should be one obvious way.

Refactor this code to a clearer solution
"""

def intersect_lists(list_1: list, list_2: list) -> set:
    """Returns the intersection of two lists.

    Args:
        list_1 (list): First list
        list_2 (list): Second list

    Returns:
        set: Intersection of `list_1` and `list_2`
    """

    common_elements = []
    for el in list_1:
        if el in list_2:
            common_elements.append(el)
    
    return set(common_elements)

if __name__ == "__main__":
    list_1 = [3, "Zen", 9, 80, "Food", "Sakazuki"]
    list_2 = ["Food", 9, 13, 14, 15, 3]
    common_elements = intersect_lists(list_1, list_2)
    print(common_elements) # {3, 9, "Food"}