from lab_python_oop.Figure import Figure
from lab_python_oop.FigureColor import FigureColor
import math


class Circle(Figure):
    """
    Класс «Круг» наследуется от класса «Геометрическая фигура».
    """
    FIGURE_TYPE = "Круг"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, color_param, r_param):
        self.r = r_param
        self.fc = FigureColor()
        self.fc.colorproperty = color_param

    def square(self):
        return math.pi*pow(self.r,2)

    def __repr__(self):
        return '\033[31m{}\033[0m {} цвета радиусом {} площадью {}.'.format(
            Circle.get_figure_type(),
            self.fc.colorproperty,
            self.r,
            self.square()
        )