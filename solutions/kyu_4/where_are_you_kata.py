"""Solution for kata https://www.codewars.com/kata/5a0573c446d8435b8e00009f."""
import itertools as it


class Explorer:
    def __init__(self):
        self.coordinates = [0, 0]
        self.direction = 2

    @staticmethod
    def __create_path(path):
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

    def i_am_here(self, path):
        # Initial direction - south
        # l - Rotate 90 clockwise
        # L - Rotate 180 clockwise
        # r - Rotate 90 counterclock-wise
        # R - Rotate 180 counterclock-wise
        # Number - how far to go in the direction of view
        path = self.__create_path(path)

        directions = ['North', 'West', 'South', 'East']
        direction = self.direction
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
                        case 'North': self.coordinates[0] += i
                        case 'South': self.coordinates[0] -= i
                        case 'West': self.coordinates[1] -= i
                        case 'East': self.coordinates[1] += i
                    direction = directions.index(direction)
        self.direction = direction
        return self.direction
