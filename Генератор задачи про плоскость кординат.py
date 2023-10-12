import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
from scipy import interpolate

'''Генератор аналогичных задач: https://ege.sdamgia.ru/problem?id=27489'''
fig = plt.figure()
ax = plt.axes()
fig.add_axes(ax)
ax.spines[["left", "bottom"]].set_position('zero')
ax.spines[["top", "right"]].set_visible(False)
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
plt.xticks(np.arange(-10, 11, 1), fontsize=8)
plt.yticks(np.arange(-10, 11, 1), fontsize=8)
ax.grid(True)
arrow_length = 10
ax.annotate('x', xy=(1, 0), xycoords=('axes fraction', 'data'),
          xytext=(0, arrow_length), textcoords='offset points',
          ha='center', va='bottom')
ax.annotate('y', xy=(0, 1), xycoords=('data', 'axes fraction'),
          xytext=(arrow_length, 0), textcoords='offset points',
          ha='center', va='bottom')

points = []
left_count = 0
right_count = 0
tangent_count = 0
while left_count < 2 or right_count < 2:
    x = np.random.uniform(-10.0, 10.0, size=1)[0]
    y = np.random.uniform(-10.0, 10.0, size=1)[0]
    m = random.randint(-10, 10)

    if x < 0 and left_count < 2:
        left_count += 1
        points.append((x, y))

    elif x > 0 and right_count < 2:
        right_count += 1
        points.append((x, y))


points.sort()  # Сортировка точек по возрастанию

x_coords, y_coords = zip(*points)
x_coords_list = np.array(x_coords)
x_coords_list.sort()
y_coords_list = np.array(y_coords)
y_coords_list.sort()

spl = make_interp_spline(x_coords_list, y_coords_list)
x_smooth = np.linspace(min(x_coords_list), max(x_coords_list), 150)
y_smooth = spl(x_smooth)

ax.plot(x_smooth, y_smooth, color='blue', linewidth=1)  # Построение сглаженной кривой

x_start = np.round(points[0][0], 2)
x_end = np.round(points[-1][0], 2)


plt.gca().autoscale(False)
plt.gca().set_xlim([-10, 10])
plt.gca().set_ylim([-10, 10])

# Добавляем код для проверки параллельных касательных
for point in points:
    x = point[0]
    y = point[1]
    if x != 0 and y/x == m:
        tangent_count += 1

print(f'На рисунке изображен график функции y = f(x), определенной на интервале ({x_start} : {x_end}).'
        f'\nНайдите количество точек, в которых касательная к графику функции параллельна прямой y = {m} или совпадает с ней.')

plt.show()


