import matplotlib
import matplotlib.pyplot as plt
from Geometry import Point, Line, Polygon
from plotter import Plotter
from io_file import IO_file
from categoriser import Categoriser

matplotlib.use('TkAgg')


def main():
    print("read polygon.csv")
    io = IO_file()
    polygon_points, x_polygon, y_polygon, polygon_lines = io.input_polyfile("polygon.csv")

    print("read input.csv")
    input_points = io.input_pointfile("input.csv")

    print("categorize points")  # MBR boundaries
    cate = Categoriser()
    out_dots, idk_dots = cate.mbr(input_points, x_polygon, y_polygon)
    bou_dots = cate.boundary_check(idk_dots, polygon_lines)

    idk_dots_2 = {k: v for k, v in idk_dots.items() if k not in bou_dots}
    #print(idk_dots_2)

    in_dots = {}

    point1 = polygon_points[0]

    for i in idk_dots_2:
        x, y = i.get_x(), i.get_y()
        #print(x, y)
        count = 0
        for a in range(1, len(polygon_points)):
            point2 = polygon_points[a]
            #print(point1.get_x(), point1.get_y(), point2.get_x(), point2.get_y())
            if (point1.get_y() < y and point2.get_y() >= y) or (point1.get_y() >= y and point2.get_y() < y):
                # 求线段与射线交点 再和lat比较
                point12lng = point2.get_x() - (point2.get_y() - y) * (point2.get_x() - point1.get_x()) / (
                            point2.get_y() - point1.get_y())
                #print(point12lng)
                if point12lng < x:
                    count += 1
            point1 = point2
        if count % 2 == 0:
            out_dots[i] = "outside"
        else:
            in_dots[i] = "inside"


    classified_points = {**out_dots, **bou_dots, **in_dots}

    print("write output.csv")
    io.output_pointfile("output.csv", classified_points.items())

    print("plot polygon and points")
    plotter = Plotter()
    plotter.add_polygon(x_polygon, y_polygon)  # plot Polygon

    # plt.plot([x_min, x_min, x_max, x_max, x_min], [y_min, y_max, y_max, y_min, y_min])  # plot MBR
    plotter.add_all_point(classified_points.items())

    # Can be deleted after tests
    """
    #Ray test


    for key, value in idk_dots_2.items():
        y = float(key.get_y())
        xmin = float(key.get_x())
        xmax = 1
        plotter.add_ray(y, xmin, xmax)
    """
    plotter.show()


if __name__ == "__main__":
    main()
