import plotly.express as px
from pathlib import Path
from two_d8s import Die
path = Path('die_comprehension.html')
die_1 = Die(6)
die_2 = Die(6)
results = []
frequencies = []
for roll in range(1000):
    results.append(die_1.roll_die() * die_2.roll_die())
max_value = die_1.num_side * die_2.num_side
for value in range(1, max_value+1):
    frequencies.append(results.count(value))
title = "Results of Rolling Two D6 Dice 1,000 Times by each time with multiplication"
labels = {'x': 'Results', 'y': 'Frequencies of Results'}
fig = px.bar(x=range(1, max_value+1), y=frequencies,
             title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.write_html(path)
fig.show()
