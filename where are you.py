# https://www.codewars.com/kata/5a0573c446d8435b8e00009f
import itertools as it


COORDINATES = [0, 0]
DIRECTION = 2


def create_path(path):
    """
    The function divides the path into subgroups:
    Where is the False flag - a subgroup of numbers
    Where is the flag True - a subgroup of letters
    Letters are separated from each other, numbers are combined
    :param path: raw way
    :return: a list where letters and numbers are separated
    """
    groups = it.groupby(path, lambda x: x.isalpha())
    res = []
    for flag, objs in groups:
        if flag:
            res.extend(objs)
        else:
            res.append(int(''.join(tuple(objs))))

    return res


def i_am_here(path):
    # Initial direction - south
    # l - Rotate 90 clockwise
    # L - Rotate 180 clockwise
    # r - Rotate 90 counterclock-wise
    # R - Rotate 180 counterclock-wise
    # Number - how far to go in the direction of view
    path = create_path(path)

    global DIRECTION
    directions = ['North', 'West', 'South', 'East']
    direction = DIRECTION
    for i in path:
        match i:
            case 'l': direction -= 1
            case 'L': direction -= 2
            case 'r': direction += 1
            case 'R': direction += 2

            # _ - means any 1 object, analogous to the "else" construct
            case _:
                # The viewing direction must be in the range [-4, 3] to stay within the list
                while direction < -4:
                    direction += 4
                while direction > 3:
                    direction -= 4

                direction = directions[direction]
                match direction:
                    case 'North': COORDINATES[0] += i
                    case 'South': COORDINATES[0] -= i
                    case 'West': COORDINATES[1] -= i
                    case 'East': COORDINATES[1] += i
                direction = directions.index(direction)
    DIRECTION = direction
    return COORDINATES
