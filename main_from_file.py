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
        return self. __y

class Polygon():

    def __init__(self, points):
        self.points = points

class Categoriser():

    def __init__(self, polygon):
        self.polygon = polygon

    def categorise_point(self):

        if outside_mbr(point):
            return "outside"





from plotter import Plotter


import csv # The package to read csv files

def main():
    plotter = Plotter()
    print("read polygon.csv")
    with open("polygon.csv", "r") as file:
        data = csv.reader(file) # read the csv file

        next(data) # skip the first line in csv
        poly_point = []
        x_polygon =[] # need these x coordinates to plot polygon
        y_polygon =[] # need these y coordinates to plot polygon
        for line in data:
            id, x, y = line[0], line[1], line[2]
            poly_point = Point(id, x, y)
            print([float(poly_point.get_x()), float(poly_point.get_y())]) # just print out
            x_polygon.append(float(line[1]))  # the list of x coordinates to plot polygon
            y_polygon.append(float(line[2]))  # the list of y coordinates to plot polygon







    print("read input.csv")
    with open("input.csv", "r") as input_file:
        input_data = csv.reader(input_file)  # read the csv file

        next(input_data)  # skip the first line in csv
        x_input = []
        y_input = []
        for line in input_data:
            x_input.append(float(line[1]))
            y_input.append(float(line[2]))

        print(x_input, y_input)




    print("categorize points") # MBR boundaries

    x_max = max(x_polygon)
    x_min = min(x_polygon)
    y_max = max(y_polygon)
    y_min = min(x_polygon)

    print(x_max, x_min, y_max, y_min) # print the MBR ranges (MBR done here




    print("write output.csv")

    print("plot polygon and points")
    plotter = Plotter()
    plotter.add_polygon(x_polygon, y_polygon) # plot Polygon
    plt.plot([x_min, x_min, x_max, x_max, x_min], [y_min, y_max, y_max, y_min, y_min]) # plot MBR
    plotter.add_point(x_input, y_input) # plot points which need to be categorised
    plotter.show()


if __name__ == "__main__":
    main()
