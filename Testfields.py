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
    bou_dots = cate.boundary_check(idk_dots,polygon_lines)

    idk_dots_2 = {k:v for k,v in idk_dots.items() if k not in bou_dots}

    print(len(out_dots), "outdots") #DELETE
    print(len(bou_dots), "boundots") #DELETE
    print(len(idk_dots), "idkdots") #DELETE
    print(len(idk_dots_2), "idk_2 points") #DELETE

    classified_points = {**out_dots, **bou_dots, **idk_dots_2}
    print(classified_points) #DELETE

    print("write output.csv")
    io.output_pointfile("output.csv", classified_points.items())

    print("plot polygon and points")
    plotter = Plotter()
    plotter.add_polygon(x_polygon, y_polygon)  # plot Polygon

    #plt.plot([x_min, x_min, x_max, x_max, x_min], [y_min, y_max, y_max, y_min, y_min])  # plot MBR
    plotter.add_point(classified_points.items())

    #Can be deleted after tests
    """
    for key, value in classified_points.items():
        x = float(key.get_x())
        y = float(key.get_y())
        kind = value
        plotter.add_point(x,y,kind)
    
    for key, value in bou_dots.items():
        x = float(key.get_x())
        y = float(key.get_y())
        kind = value
        plotter.add_point(x,y, kind)

    for key, value in idk_dots_2.items():
        x = float(key.get_x())
        y = float(key.get_y())
        kind = value
        plotter.add_point(x, y, kind)
    """

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
