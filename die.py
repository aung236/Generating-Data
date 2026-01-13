from random import randint


class Die:
    """A class representing a single die."""

    def __init__(self, num_sides=6):
        """Assume a six-sided die."""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between
        1 and number of sides"""
        return randint(1, self.num_sides)


die = Die()
results = []
frequencies = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
