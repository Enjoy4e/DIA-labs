class FigureColor:
    """
    Класс «Цвет фигуры»
    """

    def __init__(self):
        self.__color = None

    @property
    def colorproperty(self):

        return self.__color

    @colorproperty.setter
    def colorproperty(self, value):

        self.__color = value