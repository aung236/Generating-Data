import plotly.express as px
from pathlib import Path
from two_d8s import Die
path = Path('two_die_multiplication.html')
die_1 = Die(6)
die_2 = Die(6)
results = []
frequencies = []
for roll in range(1000):
    result = die_1.roll_die() * die_2.roll_die()
    results.append(result)
max_value = die_1.num_side * die_2.num_side
poss_results = range(1, max_value+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
title = "Results of Rolling Two D6 Dice 1,000 Times by each time with multiplication"
labels = {'x': 'Results', 'y': 'Frequencies of Results'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.write_html(path)
fig.show()
