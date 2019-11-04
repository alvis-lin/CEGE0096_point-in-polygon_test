from collections import OrderedDict

import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')


class Plotter:

    def __init__(self):
        plt.figure()

    def add_polygon(self, xs, ys):
        plt.fill(xs, ys, "b", label='Polygon')

    def add_point(self, x, y, kind=None):
        if kind == "outside":
            plt.plot(x, y, "ro", label='Outside')
        elif kind == "boundary":
            plt.plot(x, y, "yo", label='Boundary')
        elif kind == "inside":
            plt.plot(x, y, "go", label='Inside')
        else:
            plt.plot(x, y, "ko", label='Unclassified')

    def show(self):
        handles, labels = plt.gca().get_legend_handles_labels()
        by_label = OrderedDict(zip(labels, handles))
        plt.legend(by_label.values(), by_label.keys())
        plt.show()


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
        x_polygon = []
        y_polygon = []
        for line in file:
            data = line.strip().split(",")
            x_polygon.append(float(data[1]))
            y_polygon.append(float(data[2]))

        print(x_polygon, y_polygon)

        """
            id, x, y = data[0], data[1], data[2]
            x_polygon.append(float(line[1]))  # the list of x coordinates to plot polygon
            y_polygon.append(float(line[2]))  # the list of y coordinates to plot polygon
            print(line)
        """

    print("read input.csv")
    with open("input.csv", "r") as input_file:
        next(input_file)  # skip the first line in csv

        input_point = []
        x_input = []
        y_input = []
        for line in input_file:
            data = line.strip().split(",")
            x_input.append(float(data[1]))
            y_input.append(float(data[2]))

        print(x_input, y_input)

    print("categorize points")  # MBR boundaries

    x_max = max(x_polygon)
    x_min = min(x_polygon)
    y_max = max(y_polygon)
    y_min = min(x_polygon)

    print(x_max, x_min, y_max, y_min)  # print the MBR ranges (MBR done here

    """
    # Check from this bit below

    cate_dots = {}
    for i in poly_point:
        if poly_point.get_y(i) > x_max:
            poly_point[i] = "outsideeeeeee"

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
    plotter.add_point(x_input, y_input)  # plot points which need to be categorised
    plt.savefig('test.png')  # save fig as png file
    plt.show()


if __name__ == "__main__":
    main()