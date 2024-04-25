# https://www.codewars.com/kata/5c2256acb26767ff56000047


def knapsack(items, w_limit):
    print(items)
    # Creating an array for the shared values of the backpack
    array = [[0] * (w_limit + 1) for _ in range(len(items) + 1)]
    items.insert(0, 0)
    # Creating an array to store lists of the values of the items used
    x = []
    for i in range(len(items)):
        x.append([])
        for _ in range(w_limit + 1):
            x[i].append([])

    # We write in the array the maximum value of the values of the items for each weight limit and set of items
    for i in range(1, len(items)):
        item = items[i]
        if item == 0:
            continue
        for j in range(1, w_limit + 1):
            array[i][j] = array[i - 1][j]
            x[i][j].extend(x[i - 1][j])

            if j - item[0] >= 0:
                x[i][j] = []
                array[i][j] = max(array[i - 1][j], array[i - 1][j - item[0]] + item[1])

                # We write a set of values of objects to the array x
                if array[i - 1][j - item[0]] + item[1] >= array[i - 1][j]:
                    x[i][j].append(item[1])
                    x[i][j].extend(x[i - 1][j - item[0]])

                else:
                    x[i][j].extend(x[i - 1][j])

    # We run through the array x, sorting and selecting all the lists where the maximum weight is used
    # and where the sum of values is equal to the maximum
    rez = []
    for i in range(len(x)):
        for j in range(len(x[i])):
            x[i][j].sort()
            if array[i][j] == array[-1][-1] and x[i][j] not in rez:
                rez.append(x[i][j])
    rez.sort()

    return [array[-1][-1], list(rez)]