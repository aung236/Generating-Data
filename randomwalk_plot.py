import matplotlib.pyplot as plt
from rw_visiblel import RandomWalks

rw = RandomWalks()
rw.fill_walk()
plt.style.use('classic')
point_numbers = range(rw.num_point)
fig, ax = plt.subplots(figsize=(15, 9), dpi=96)
ax.plot(rw.x_values, rw.y_values, color=(
    0, 0.2, 0.1), linewidth=3)
ax.plot(0, 0, c='red')
ax.plot(rw.x_values[-1], rw.y_values[-1], c='green')
# ax.get_xaxis().set_visible(False)
# ax.get_yaxis().set_visible(False)

plt.show()
