import matplotlib
import matplotlib.pyplot as plt
from Geometry import Point, Line, Polygon
from plotter import Plotter

matplotlib.use('TkAgg')


class Categoriser():

    def __init__(self, polygon):
        self.polygon = polygon

    """    def outside_mbr(self):
        for point in point:
    """

    def categorise_point(self):
        if outside_mbr(point):
            return "outside"


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

        polygon_lines = []
        prev = polygon_points[0]
        for i in polygon_points[1:]:
            polygon_lines.append(Line(prev,i))
            prev = i

    for i in polygon_lines:
        a, b = i.get_points()
        print(a.get_x(),a.get_y(), b.get_x(), b.get_y())




    print("TESTTTTTT")



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
        if float(i.get_x()) > x_max or float(i.get_x()) < x_min:
            cate_dots[i] = "outside"
        elif float(i.get_y()) > y_max or float(i.get_y()) < y_min:
            cate_dots[i] = "outside"
        else:
            cate_dots[i] = "idk"






    print("write output.csv")

    print("plot polygon and points")
    plotter = Plotter()
    plotter.add_polygon(x_polygon, y_polygon)  # plot Polygon
    plotter.add_line(x_polygon, y_polygon)
    #plt.plot([x_min, x_min, x_max, x_max, x_min], [y_min, y_max, y_max, y_min, y_min])  # plot MBR


    for key, value in cate_dots.items():
        x = key.get_x()
        y = key.get_y()
        kind = value
        plotter.add_point(float(key.get_x()), float(key.get_y()), value)


    plotter.show()


if __name__ == "__main__":
    main()