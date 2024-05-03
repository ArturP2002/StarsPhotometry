import re  # Библиотека для работы с регулярными выражениями
import matplotlib.pyplot as plt  # Библиотека для работы с диаграммой


def center_area():
    """
    Функция для записи в файл всех хороших звезд из центра галактики, построения CMD центрального эллипса
    """
    # Отбираем хорошие звезды центра
    with open('good_stars.txt', 'r', encoding='UTF-8') as good:
        with open('good_stars_center.txt', 'w', encoding='UTF-8') as final_file:
            cmd_x_fin = []  # список для записи всех значений cmd по x
            F814_FIN = []  # список для записи всех значений фильтра F814
            while line := good.readline():
                new_line = line.rstrip()
                numbers = re.findall(r'-?\d+\.?\d*', new_line)
                if float(numbers[9]) < 0.5 and float(numbers[10]) <= 2.0 and float(numbers[21]) >= 5.0 and float(
                        numbers[22]) ** 2 <= 0.01 and float(numbers[24]) < 0.5 and float(numbers[25]) <= 2.0 and float(
                        numbers[36]) >= 5.0 and float(numbers[37]) ** 2 <= 0.01 and float(numbers[39]) < 0.5 and float(
                        numbers[40]) <= 2.0 and 1840.0 <= float(numbers[2]) <= 2578.0 and 2458.0 <= float(
                        numbers[3]) <= 3519.00:
                    cmd_x_fin.append(float(numbers[17]))
                    F814_FIN.append(float(numbers[32]))
                    final_file.write(f'{new_line} \n')

    F606_FIN = []  # список для записи всех значений фильтра F606

    for i_elem in range(len(cmd_x_fin)):
        cmd_x_end2 = cmd_x_fin[i_elem] - F814_FIN[i_elem]
        F606_FIN.append(cmd_x_end2)

    data3 = list(zip(F606_FIN, F814_FIN))  # Создаем кортеж значений двух фильтров для CMD
    x_coord3, y_coord3 = zip(*data3)
    plt.scatter(x_coord3, y_coord3, s=0.2)
    plt.xlabel('F606-F814')
    plt.ylabel('F814')
    plt.gca().invert_yaxis()
    plt.show()
