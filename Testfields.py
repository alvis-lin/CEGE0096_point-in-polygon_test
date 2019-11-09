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

    print("categorize points")
    cate = Categoriser()
    out_dots, idk_dots = cate.mbr_check(input_points, x_polygon, y_polygon) #MBR
    bou_dots = cate.boundary_check(idk_dots, polygon_lines) # POL
    idk_dots_2 = {k: v for k, v in idk_dots.items() if k not in bou_dots} # get rest points to classify after POL
    print(idk_dots_2)
    in_dots, out_dots = cate.rca_check(idk_dots_2, polygon_points, out_dots) #RCA

    classified_points = {**out_dots, **bou_dots, **in_dots}

    print("write output.csv")
    io.output_pointfile("output.csv", classified_points.items())

    print("plot polygon and points")
    plotter = Plotter()
    plotter.add_polygon(x_polygon, y_polygon)  # plot Polygon
    plotter.add_all_point(classified_points.items()) # plot results
    #plotter.add_line(x_polygon, y_polygon)
    #plotter.add_ray(idk_dots_2.items()) # problems
    # Can be deleted after tests

    #Ray test
    """

    for key, value in idk_dots_2.items():
        y = float(key.get_y())
        xmin = float(key.get_x())
        xmax = 1
        plotter.add_ray(y, xmin, xmax)
    """
    plotter.show()


if __name__ == "__main__":
    main()

