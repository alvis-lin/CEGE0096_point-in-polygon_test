from collections import OrderedDict

import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')



class Point():

    def __init__(self, id, x, y):
        self.__id = id
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y


class Polygon():

    def __init__(self, points):
        self.__points = points


class Categoriser():

    def __init__(self, polygon):

        self.polygon = polygon

    """    def outside_mbr(self):
        for point in point:
    """

    def categorise_point(self):
        if outside_mbr(point):
            return "outside"





from plotter import Plotter

def main():
    plotter = Plotter()
    print("read polygon.csv")
    with open("polygon.csv", "r") as file:
        next(file)  # skip the first line in csv
        polygon_points = []  # to store point objects
        x_polygon = []  # to store x coordinates of polygon
        y_polygon = []  # to store y coordinates of polygon
        for line in file:
            data = line.strip().split(",")
            polygon_points.append(Point(data[0], data[1], data[2]))  # get data into Point() objects
            x_polygon.append(float(data[1]))  # the list of x coordinates to plot polygon
            y_polygon.append(float(data[2]))  # the list of y coordinates to plot polygon

        print(x_polygon, y_polygon)

        print("test")

        """
        id, x, y = data[0], data[1], data[2]
        print(line)
        """

    print("read input.csv")
    with open("input.csv", "r") as input_file:
        next(input_file)  # skip the first line in csv

        input_points = []  # nothing so far
        x_input = []
        y_input = []
        for line in input_file:
            data = line.strip().split(",")
            input_points.append(Point(data[0], data[1], data[2]))  # get data in to points(hopefully)
            x_input.append(float(data[1]))
            y_input.append(float(data[2]))

        print(x_input, y_input)


    print("categorize points")  # MBR boundaries

    x_max = max(x_polygon)
    x_min = min(x_polygon)
    y_max = max(y_polygon)
    y_min = min(x_polygon)

    print(x_max, x_min, y_max, y_min)  # print the MBR ranges (MBR done here


    # Check from this bit below
    # MRB identifier
    
    cate_dots = {}
    for i in input_points:
        if float(i.get_x()) > x_max:
            cate_dots[i] = "outside"
        elif float(i.get_x()) < x_min:
            cate_dots[i] = "outside"
        elif float(i.get_y()) > y_max:
            cate_dots[i] = "outside"
        elif float(i.get_y()) < y_min:
            cate_dots[i] = "outside"
        elif float(i.get_x()) == x_max and float(i.get_y()) <= y_max and float(i.get_y()) >= y_min:
            cate_dots[i] = "boundary"
        elif float(i.get_x()) == x_min and float(i.get_y()) <= y_max and float(i.get_y()) >= y_min:
            cate_dots[i] = "boundary"
        elif float(i.get_y()) == y_max and float(i.get_x()) <= x_max and float(i.get_x()) >= x_min:
            cate_dots[i] = "boundary"
        elif float(i.get_y()) == y_min and float(i.get_x()) <= x_max and float(i.get_x()) >= x_min:
            cate_dots[i] = "boundary"
        else:
            cate_dots[i] = "idk"


    """
    # Below are not done yet

        def mbr_xpoint_finder():
            kind = ""


        def mbr_ypoint_finder():
            kind = ""
            for i in y_input:
                if i < y_min:
                    kind = "outside"
                elif i > y_max:
                    kind = "outside"
                else:
                    kind = "YYYunclassidied"
            return kind

    
    """
    print("write output.csv")

    print("plot polygon and points")
    plotter = Plotter()
    plotter.add_polygon(x_polygon, y_polygon)  # plot Polygon
    plt.plot([x_min, x_min, x_max, x_max, x_min], [y_min, y_max, y_max, y_min, y_min])  # plot MBR
    for key, value in cate_dots.items():
        x = key.get_x()
        y = key.get_y()
        kind = value
        plotter.add_point(float(key.get_x()),float(key.get_y()), value)

    plt.savefig('test.png') # save fig as png file
    plotter.show()
    


if __name__ == "__main__":
    main()