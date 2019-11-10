import matplotlib
import matplotlib.pyplot as plt
from plotter import Plotter
from io_file import IoFile
from categoriser import Categoriser

matplotlib.use('TkAgg')


def main():
    print("read polygon.csv")
    io = IoFile()
    polygon_points, x_polygon, y_polygon, polygon_lines = io.input_polyfile()

    print("read input.csv")
    input_points = io.input_pointfile()

    print("categorize points")
    cate = Categoriser()
    out_dots, idk_dots = cate.mbr_check(input_points, x_polygon, y_polygon)
    bou_dots = cate.pol_check(idk_dots, polygon_lines)
    idk_dots_2 = {k: v for k, v in idk_dots.items() if k not in bou_dots}  # get rest points to classify after POL
    in_dots, out_dots = cate.rca_check(idk_dots_2, polygon_points, out_dots)
    classified_points = {**out_dots, **bou_dots, **in_dots}  # merge the result into one dictionary

    print("write output.csv")
    io.output_pointfile(classified_points.items())

    print("plot polygon and points")
    plotter = Plotter()
    plotter.add_polygon(x_polygon, y_polygon)
    plotter.add_all_point(classified_points.items())
    plt.savefig(str(input("Please enter preferred image name (i.e., file.png): ")))
    plotter.show()


if __name__ == "__main__":
    main()
