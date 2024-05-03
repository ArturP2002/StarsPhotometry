# Импортируем библиотеки для работы
import re  # Библиотека для работы с регулярными выражениями
import numpy as np  # Библиотека для работы с матрицами
import matplotlib.pyplot as plt  # Библиотека для работы с диаграммой
from CMD_Diagrams.High_youbochka import high_area
from CMD_Diagrams.Center_ellipse import center_area
from CMD_Diagrams.Low_youbochka import low_area
from CMD_Diagrams.Full_custom_CMD import full_area
from Semicirle_function.draw import draw_semicircle


count = 0  # Переменная, введенная для порядкового номера строки при записи в тестовый файл

# Для первого и второго фильтра отбираем хорошие звезды
with open('testing.txt', 'w', encoding='UTF-8') as test:
    with open('result.phot', 'r', encoding='UTF-8') as file:
        cmd_x = []  # список для записи всех значений cmd по x
        F814 = []  # список для записи всех значений фильтра F814
        with open('good_stars.txt', 'w', encoding='UTF-8') as good:
            while line := file.readline():
                count += 1
                new_line = line.rstrip()
                numbers = re.findall(r'-?\d+\.?\d*', new_line)
                if float(numbers[9]) < 0.5 and float(numbers[10]) <= 2.0 and float(numbers[21]) >= 5.0 and float(
                        numbers[22])**2 <= 0.01 and float(numbers[24]) < 0.5 and float(numbers[25]) <= 2.0 and float(
                        numbers[36]) >= 5.0 and float(numbers[37])**2 <= 0.01 and float(numbers[39]) < 0.5 and float(
                        numbers[40]) <= 2.0:
                    good.write(f'{new_line} \n')  # Записываем хорошие звезды в файл
                    cmd_x.append(float(numbers[17]))  # Добавляем значение CMD по x в массив
                    F814.append(float(numbers[32]))  # Добавляем значение F814 в массив
                test.write(f'{count}) {new_line} \n\n')  # Переписываем строки всех звезд в файл для проверки себя

F606 = []  # список для записи всех значений фильтра F606

for i_elem in range(len(cmd_x)):
    cmd_x_end = cmd_x[i_elem] - F814[i_elem]
    F606.append(cmd_x_end)

with open('good_stars.txt', 'r', encoding='UTF-8') as find_coord:
    coordinates_y = []
    coordinates_x = []
    while line := find_coord.readline():  # Получаем координаты x и y всех хороших звезд
        new_line = line.rstrip()
        numbers = re.findall(r'-?\d+\.?\d*', new_line)  # Регулярное выражение для поиска всех чисел в строке
        coordinates_x.append(float(numbers[2]))
        coordinates_y.append(float(numbers[3]))

data1 = list(zip(coordinates_x, coordinates_y))  # Создаем кортеж значений двух фильтров для CMD
x_coord1, y_coord1 = zip(*data1)

cov = np.cov(x_coord1, y_coord1)
val, rot = np.linalg.eig(cov)
val = np.sqrt(val)
center = np.mean([x_coord1, y_coord1], axis=1)[:, None]   # Находим центр галактики

t = np.linspace(0, 2.0 * np.pi, 1000)
xy = np.stack((np.cos(t), np.sin(t)), axis=-1)

plt.scatter(x_coord1, y_coord1, s=0.2)  # Строим точечную диаграмму для звезд
plt.xlabel('X')  # Называем ось абсцисс
plt.ylabel('Y')  # Называем ось ординат
plt.gca().invert_yaxis()  # Направляем ось ординат в противоположную сторону
plt.plot(*(0.7 * rot @ (val * xy).T + center), color='black')  # Строим эллипс в центре
plt.plot([2021, 1665], [3544, 4153], 'k-', linewidth=2)  # Проводим прямую линию, выбранную визуально
draw_semicircle(2021, 3544, 1655, 4153, color='black', lw=2)  # Строим дугу для соответствующей линии
plt.plot([2454, 2965], [2489, 1949], 'k-', linewidth=2)  # Проводим прямую линию, выбранную визуально
draw_semicircle(2454, 2489, 2965, 1949, color='black', lw=2)  # Строим дугу для соответствующей линии
plt.show()  # Выводим график

data2 = list(zip(F606, F814))  # Создаем кортеж значений двух фильтров для CMD
x_coord2, y_coord2 = zip(*data2)
plt.scatter(x_coord2, y_coord2, s=0.2)  # Строим точечную диаграмму для звезд
plt.xlabel('F606-F814')  # Называем ось абсцисс
plt.ylabel('F814')  # Называем ось ординат
plt.gca().invert_yaxis()  # Направляем ось ординат в противоположную сторону
plt.show()

full_area()
low_area()
center_area()
high_area()
