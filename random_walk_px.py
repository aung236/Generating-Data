from random import choice
import plotly.express as px


class RandomWalk:
    def __init__(self, point_num=1000):
        self.point_num = point_num
        self.x_set = [0]
        self.y_set = [0]

    def random_step(self):
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        return direction * distance

    def random_walk(self):
        rw = RandomWalk()
        while len(self.x_set) < self.point_num:
            x_step = rw.random_step()
            y_step = rw.random_step()

            x = self.x_set[-1] + x_step
            y = self.y_set[-1] + y_step
            self.x_set.append(x)
            self.y_set.append(y)


rw = RandomWalk(50000)
rw.random_walk()
steps = range(rw.point_num)
title = 'Randomm Walk with 1,000 Steps'
labels = {'x': 'X_Coordinate_Steps',
          'y': 'Y_Coordinate_Steps', 'Color': 'Step'}
fig = px.scatter(x=rw.x_set, y=rw.y_set, color=steps,
                 color_continuous_scale='Blues', title=title, labels=labels)
fig.add_scatter(x=[rw.x_set[0]], y=[rw.y_set[0]], mode='markers',
                marker=dict(size=14, color='green'), name='Start')
fig.add_scatter(x=[rw.x_set[-1]], y=[rw.y_set[-1]], mode='markers',
                marker=dict(size=14, color='red'), name="End")
fig.show()
