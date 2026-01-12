import matplotlib.pyplot as plt
from run import RandomWalk


rw = RandomWalk(10000)
rw.fill_walk()
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(15, 9), dpi=96)
point_numbers = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, c=point_numbers,
           cmap=plt.cm.Blues, edgecolor='none', s=15)
ax.scatter(0, 0, c='red', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='green', s=100)
ax.set_aspect('equal')
plt.savefig(r'C:\Users\aungseinwin\Desktop\python_work\project photo\random_walking_A.png',
            bbox_inches='tight')
plt.show()
