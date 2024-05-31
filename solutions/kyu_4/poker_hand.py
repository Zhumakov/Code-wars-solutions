"""Solution for kata https://www.codewars.com/kata/5739174624fc28e188000465."""
import collections


class PokerHand(object):
    RESULT = ['Loss', 'Tie', 'Win']

    COST_COMB = {'Royal Flush': 10, 'Straight Flush': 9, 'Four of a Kind': 8, 'Full Hause': 7, 'Flush': 6,
                 'Straight': 5, 'Three of a Kind': 4, 'Two Pair': 3, 'Pair': 2, 'High card': 1}

    SUITS = ['S', 'H', 'D', 'C']

    def __init__(self, hand):
        """
        Сonverts the cards in your hand into two lists:
        The first one stores the card values
        The second stores the suits of the corresponding cards
        :param hand: accepts a list of cards in hand
        """
        cards = hand.split(' ')
        print(cards)

        advantages = [i[0] for i in cards]
        for i in range(5):
            match advantages[i]:
                case 'T': advantages[i] = 10
                case 'J': advantages[i] = 11
                case 'Q': advantages[i] = 12
                case 'K': advantages[i] = 13
                case 'A': advantages[i] = 14
                case _:
                    advantages[i] = int(advantages[i])

        self.advantages = advantages
        count_advantages = dict(collections.Counter(advantages))

        suits_list = [i[1] for i in cards]
        suits = dict(collections.Counter(suits_list))

        self.__calc_comb(advantages, suits, count_advantages)

    def __calc_comb(self, advantages, suits, count_advantages):
        """
        The function determines the combination and its value
        :param advantages: list of card meanings
        :param suits: list of card suits
        :param count_advantages: list of number of matching card values
        """
        # If in a list of values all values are in the range from 10 to 14 and there are 5 identical suits
        if sorted(advantages) == [i for i in range(10, 15)] and 5 in suits.values():
            self.comb = 'Royal Flush'

        # If in a list of values, the values are in ascending order in increments of 1, and there are 5 identical suits
        elif sorted(advantages) == [i for i in range(sorted(advantages)[0], sorted(advantages)[-1] + 1, 1)]\
                and 5 in suits.values():
            self.comb = 'Straight Flush'

        # If there are 4 identical values
        elif 4 in count_advantages.values():
            self.comb = 'Four of a Kind'

        # If there are 3 identical values and 2 other identical values
        elif 3 in count_advantages.values() and 2 in count_advantages.values():
            self.comb = 'Full Hause'

        # If there are 5 identical suits
        elif 5 in suits.values():
            self.comb = 'Flush'

        # If in a list of values, the values are in order
        elif sorted(advantages) == [i for i in range(sorted(advantages)[0], sorted(advantages)[-1] + 1, 1)]:
            self.comb = 'Straight'

        # If there are 3 identical values
        elif 3 in count_advantages.values():
            self.comb = 'Three of a Kind'

        # If there are two pairs of the same values (Then Counter.values() will have the value 2)
        elif 2 in collections.Counter(count_advantages.values()).values():
            self.comb = 'Two Pair'

        # If there are 2 identical values
        elif 2 in count_advantages.values():
            self.comb = 'Pair'

        else:
            self.comb = 'High card'

    def compare_with(self, other):
        """
        The function receives and compares card combinations by cost
        :param other: Hand with opponent's cards
        :return: round result
        """
        my_comb = self.comb
        other_comb = other.comb
        print(my_comb)
        print(other_comb)

        if self.COST_COMB[my_comb] > self.COST_COMB[other_comb]:
            return self.RESULT[2]

        elif self.COST_COMB[my_comb] < self.COST_COMB[other_comb]:
            return self.RESULT[0]

        # Если комбинации одинаковые, сравниваются следующие старшие карты
        else:
            while len(self.advantages) >= 1:
                i = max(self.advantages)
                self.advantages.remove(i)
                j = max(other.advantages)
                other.advantages.remove(j)

                if i > j:
                    return self.RESULT[2]

                elif i < j:
                    return self.RESULT[0]

                else:
                    continue

            return self.RESULT[1]


def run_kata(hand, other):
    player, opponent = PokerHand(hand), PokerHand(other)
    return player.compare_with(opponent)
