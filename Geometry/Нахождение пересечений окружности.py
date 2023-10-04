import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#Функция для нахождения пересечений двух окружностей
def find_circle_intersections(x1, y1, r1, x2, y2, r2):
    d = np.sqrt((x2 - x1) * 2 + (y2 - y1) * 2)
    if d > r1 + r2:
        return "Окружности не пересекаются"
    elif d < np.abs(r1 - r2):
        return "Одна окружность находится внутри другой"
    elif d == 0 and r1 == r2:
        return "Окружности совпадают"
    else:
        a = (r1 * 2 - r2 * 2 + d * 2) / (2 * d)
        h = np.sqrt(r1 * 2 - a ** 2)
        x3 = x1 + a * (x2 - x1) / d
        y3 = y1 + a * (y2 - y1) / d

        x4_1 = x3 + h * (y2 - y1) / d
        y4_1 = y3 - h * (x2 - x1) / d
        x4_2 = x3 - h * (y2 - y1) / d
        y4_2 = y3 + h * (x2 - x1) / d

        return [(x4_1, y4_1), (x4_2, y4_2)]

#Координаты и радиусы окружностей
x1, y1, r1 = 0, 0, 2
x2, y2, r2 = 2, 0, 1.5

#Находим пересечения окружностей
intersections = find_circle_intersections(x1, y1, r1, x2, y2, r2)

#Создаем область для построения графика
fig, ax = plt.subplots()

#Построение графика окружностей
circle1 = plt.Circle((x1, y1), r1, color='red', fill=False)
circle2 = plt.Circle((x2, y2), r2, color='blue', fill=False)
ax.add_artist(circle1)
ax.add_artist(circle2)

#Построение графика пересечений
if isinstance(intersections, list):
    for intersection in intersections:
        ax.scatter(*intersection, color='green')
        ax.annotate(f'({round(intersection[0], 2)}, {round(intersection[1], 2)})', intersection)
    intersection_count = len(intersections)
else:
    intersection_count = 0

#Настройка осей и заголовка
ax.set_xlabel("X-ось")
ax.set_ylabel("Y-ось")
ax.set_title(f"Пересечения окружностей: {intersection_count}")

#Отображение графика
plt.axis('equal')
plt.show()

#Вывод количества пересечений
print("Количество пересечений:", intersection_count)












