"""Solution for kata https://www.codewars.com/kata/5c2256acb26767ff56000047"""


class ArrayElement:
    """It is an array element containing all variations of
    objects that can be used to obtain the corresponding weight"""

    def __init__(self, items_list=((),)):
        self.items_list = items_list

    def __repr__(self):
        return f'{sum(self.items_list[0])}'

    def __eq__(self, other):
        if not isinstance(other, ArrayElement):
            raise NotImplemented
        return sum(self.items_list[0]) == sum(other.items_list[0])

    def __lt__(self, other):
        if not isinstance(other, ArrayElement):
            raise NotImplemented
        return sum(self.items_list[0]) < sum(other.items_list[0])

    def __add__(self, other):
        if not isinstance(other, int):
            raise NotImplemented
        return ArrayElement(items_list=tuple(items + (other,) for items in self.items_list))


def knapsack(items, w_limit):
    array = [[ArrayElement()] * (w_limit + 1) for _ in range(len(items) + 1)]

    for i_item in range(0, len(items)):
        for weight in range(1, w_limit + 1):
            # One is added to the item index, since the numbering in the list starts from 0
            old_elem = array[i_item][weight]
            array[i_item + 1][weight] = old_elem

            item_w, item_v = items[i_item]
            if weight - item_w >= 0:
                new_elem = array[i_item][weight - item_w] + item_v

                if old_elem < new_elem:
                    array[i_item + 1][weight] = new_elem

                # If item weights are the same, we need to keep track of all item variations
                elif old_elem == new_elem:
                    new_elem.items_list = new_elem.items_list + old_elem.items_list
                    array[i_item + 1][weight] = new_elem

    # We sort the lists in accordance with the task and remove identical sets of items
    items_list = array[-1][-1].items_list
    items_list = [sorted(lst) for lst in items_list]
    items_list.sort()
    res = []
    for lst in items_list:
        if lst not in res:
            res.append(lst)
    return [sum(res[0]), res]
