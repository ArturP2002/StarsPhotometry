import numpy as np  # Библиотека для работы с матрицами
import matplotlib.pyplot as plt  # Библиотека для работы с диаграммой
from matplotlib.patches import Arc


def draw_semicircle(x1, y1, x2, y2, color='black', lw=1, ax=None):
    """
    Функция для построения дуги между двумя точками для выделения необходимой области юбочки галактики
    :param x1: значение x первой точки
    :param y1: значение y первой точки
    :param x2: значение x второй точки
    :param y2: значение y второй точки
    :param color: цвет линии
    :param lw: толщина линии
    :param ax: область рисования
    """
    ax = ax or plt.gca()
    start_angle = np.degrees(np.arctan2(y2 - y1, x2 - x1))  # Точки начала дуги полуокружности
    diameter = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)  # Диаметр дуги полуокружности
    ax.add_patch(Arc(((x1 + x2) / 2, (y1 + y2) / 2), diameter, diameter, theta1=start_angle, theta2=start_angle + 180,
                     edgecolor=color, facecolor='none', lw=lw, zorder=0))
