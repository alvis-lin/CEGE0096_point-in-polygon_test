class Point():

    def __init__(self, id, x, y):
        self.__id = id
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

class Line():

    def __init__(self, point_1, point_2):
        self.__point_1 = point_1
        self.__point_2 = point_2

    def get_points(self):
        return self.__point_1, self.__point_2


class Polygon():

    def __init__(self, points):
        self.__points = points