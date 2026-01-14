from matplotlib import pyplot as plt
import plotly.express as px
from random import randint


class Die:
    def __init__(self, die_side=6):
        self.die_side = die_side

    def roll_num(self):
        return randint(1, self.die_side)


die_1 = Die()
die_2 = Die()
results = []
frequecies = []
for roll in range(1000):
    result = die_1.roll_num() + die_2.roll_num()
    results.append(result)
max_value = die_1.die_side + die_2.die_side
poss_results = range(2, max_value+1)
for value in poss_results:
    frequecny = results.count(value)
    frequecies.append(frequecny)
plt.style.use('_mpl-gallery-nogrid')
fig, ax = plt.subplots(figsize=(15, 9), dpi=96)
ax.bar(poss_results, frequecies)
ax.set_title('Roll Die 1,000 Times', fontsize=24)
ax.set_xlabel('Results', fontsize=14)
ax.set_ylabel('Frequencies of Results', fontsize=14)
ax.set_xticks(poss_results)

plt.tight_layout()
plt.show()
