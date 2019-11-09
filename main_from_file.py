import matplotlib
import matplotlib.pyplot as plt
from plotter import Plotter
from io_file import IO_file
from categoriser import Categoriser

matplotlib.use('TkAgg')


def main():
    print("read polygon.csv")
    io = IO_file()
    polygon_points, x_polygon, y_polygon, polygon_lines = io.input_polyfile("polygon.csv")

    print("read input.csv")
    input_points = io.input_pointfile()

    print("categorize points")
    cate = Categoriser()
    out_dots, idk_dots = cate.mbr_check(input_points, x_polygon, y_polygon) #MBR
    bou_dots = cate.boundary_check(idk_dots, polygon_lines) # POL
    idk_dots_2 = {k: v for k, v in idk_dots.items() if k not in bou_dots} # get rest points to classify after POL
    in_dots, out_dots = cate.rca_check(idk_dots_2, polygon_points, out_dots) #RCA
    classified_points = {**out_dots, **bou_dots, **in_dots}

    print("write output.csv")
    io.output_pointfile(classified_points.items())

    print("plot polygon and points")
    plotter = Plotter()
    plotter.add_polygon(x_polygon, y_polygon)  # plot Polygon
    plotter.add_all_point(classified_points.items()) # plot results
    plt.savefig(str(input("Please enter preferred image name (i.e., file.png): ")))
    plotter.show()


if __name__ == "__main__":
    main()
