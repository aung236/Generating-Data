from random import randint
import plotly.express as px
from pathlib import Path


class Die:
    def __init__(self, num_side=8):
        self.num_side = num_side

    def roll_die(self):
        return randint(1, self.num_side)


path = Path('two_d8s.html')
die_1 = Die()
die_2 = Die()

results = []
frequencies = []
for roll in range(1000):
    result = die_1.roll_die() + die_2.roll_die()
    results.append(result)
max_value = die_1.num_side + die_2.num_side
poss_result = range(2, max_value+1)
for value in poss_result:
    frequency = results.count(value)
    frequencies.append(frequency)
title = "Results of Rolling Two D8 Dice 1,000 Times"
labels = {'x': 'Results', 'y': 'Frequency of Results'}
fig = px.bar(x=poss_result, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.write_html(path)
fig.show()
