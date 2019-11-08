import matplotlib
import matplotlib.pyplot as plt
from Geometry import Point, Line, Polygon
from plotter import Plotter
from io_file import IO_file

matplotlib.use('TkAgg')


def main():

    print("read polygon.csv")

    io = IO_file()
    polygon_points, x_polygon, y_polygon, polygon_lines = io.input_polyfile("polygon.csv")


    print("read input.csv")

    input_points = io.input_pointfile("input.csv")


    print("categorize points")  # MBR boundaries

    x_max = max(x_polygon)
    x_min = min(x_polygon)
    y_max = max(y_polygon)
    y_min = min(x_polygon)

    print(x_max, x_min, y_max, y_min)  # print the MBR ranges (MBR done here


    # Check from this bit below
    # MRB identifier

    out_dots = {} # Outside points that are categorised
    bou_dots = {}
    idk_dots = {} # Points left need to be categorised
    idk_dots_2 = {} #unclassified points after boundary check
    for i in input_points:
        if float(i.get_x()) > x_max or float(i.get_x()) < x_min:
            out_dots[i] = "outside"
        elif float(i.get_y()) > y_max or float(i.get_y()) < y_min:
            out_dots[i] = "outside"
        else:
            idk_dots[i] = "idk"

    print(len(out_dots), "outdots")
    print(len(bou_dots), "boundots")
    print(len(idk_dots), "idkdots")

    for i in idk_dots:
        a, b = float(i.get_x()), float(i.get_y())
        print(a - b)
        for poly in polygon_lines:
            la, lb = poly.get_points()
            lax, lay, lbx, lby = float(la.get_x()), float(la.get_y()), float(lb.get_x()), float(lb.get_y())
            res = ""
            if max(lax, lbx) >= a >= min(lax, lbx) and max(lay, lby) >= b >= min(lay, lby):
                if lbx == lax: # means points on vertical line
                    res = "online"
                elif b == (a - lax)/(lbx - lax)*(lby - lay)+lay:
                    res = "online"
                else:
                    res = "not online"

            print(res)

            if res == "online":
                bou_dots[i] = "boundary"

    print(len(out_dots), "outdots")
    print(len(bou_dots), "boundots")
    print(len(idk_dots), "idkdots")
    print(len(idk_dots_2), "idk_2 points")

    idk_dots_2 = {k:v for k,v in idk_dots.items() if k not in bou_dots}
    print(idk_dots_2)


    print(len(out_dots), "outdots")
    print(len(bou_dots), "boundots")
    print(len(idk_dots), "idkdots")
    print(len(idk_dots_2), "idk_2 points")

    classified_points = {**out_dots, **bou_dots, **idk_dots_2}
    print(classified_points)

    print("write output.csv")
    with open("output.csv", "w") as f:
        f.writelines("x, y, classification" + "\n")
        for key, value in classified_points.items():
            x = key.get_x()
            y = key.get_y()
            kind = value
            f.writelines(str(x) + "," + str(y) + "," + str(kind)+"\n")



    print("plot polygon and points")
    plotter = Plotter()
    plotter.add_polygon(x_polygon, y_polygon)  # plot Polygon

    print("change to objectssssss")
    plt.plot([x_min, x_min, x_max, x_max, x_min], [y_min, y_max, y_max, y_min, y_min])  # plot MBR


    for key, value in out_dots.items():
        x = float(key.get_x())
        y = float(key.get_y())
        kind = value
        plotter.add_point(x,y,kind)

    for poly in polygon_lines:
        la, lb = poly.get_points()
        lax, lay, lbx, lby = float(la.get_x()), float(la.get_y()), float(lb.get_x()), float(lb.get_y())
        plotter.add_line(x_polygon, y_polygon)

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
    for key, value in idk_dots_2.items():
        y = float(key.get_y())
        xmin = float(key.get_x())
        xmax = 1
        plotter.add_ray(y, xmin, xmax)
    """
    



    plotter.show()



if __name__ == "__main__":
    main()
