import matplotlib
from plotter import Plotter
from io_file import IO_file
from categoriser import Categoriser

matplotlib.use('TkAgg')


def main():

    print("read polygon.csv")
    io = IO_file()
    polygon_points, x_polygon, y_polygon, polygon_lines = io.input_polyfile()

    print("Insert point information")
    x = float(input("x coordinate: "))
    y = float(input("y coordinate: "))
    input_points = io.input_pointfile_user(x, y)  # convert input point to point object

    print("categorize point")
    cate = Categoriser()
    out_dots, idk_dots = cate.mbr_check(input_points, x_polygon, y_polygon)
    bou_dots = cate.pol_check(idk_dots, polygon_lines)
    idk_dots_2 = {k: v for k, v in idk_dots.items() if k not in bou_dots}  # get the rest points to classify after POL
    in_dots, out_dots = cate.rca_check(idk_dots_2, polygon_points, out_dots)
    classified_points = {**out_dots, **bou_dots, **in_dots}  # merge the result into one dictionary
    io.output_user(classified_points.items())  # export the file after user enters the filename

    print("plot polygon and point")
    plotter = Plotter()
    plotter.add_polygon(x_polygon, y_polygon)
    plotter.add_all_point(classified_points.items())
    plotter.show()


if __name__ == "__main__":
    main()
