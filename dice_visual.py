import plotly.express as px
from die import Die
die_1 = Die()
die_2 = Die()

results = []
frequencies = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
max_value = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_value+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
title = 'Results of Rolling Two D6 Dice 1,000 Times'
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.show()
