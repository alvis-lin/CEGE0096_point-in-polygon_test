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

    print(len(out_dots), "outdots")  # DELETE
    print(len(bou_dots), "boundots")  # DELETE
    print(len(idk_dots), "idkdots")  # DELETE
    print(len(idk_dots_2), "idk_2 points")  # DELETE

    """
    in_dots = {}
    count = 0
    point1x = x_polygon[0]
    point1y = y_polygon[0]
    for key, value in idk_dots_2.items():
        x = float(key.get_x())
        y = float(key.get_y())
        #print(x,y)
        for i in range(1, len(polygon_points)):
            point2 = polygon_points[i]
            if (point1.get_y() < y and point2.get_y() >= y) or (point1.get_y() >= y and point2.get_y() < y):
            # 求线段与射线交点 再和lat比较
                point12lng = point2.get_x() - (point2.get_y() - y) * (point2.get_x() - point1.get_x()) / (point2.get_y() - point1.get_y())
                print(point12lng)

                if (point12lng == x):
                    print("点在多边形边上")
                    return False
                if (point12lng < x):
                    count += 1
            point1x = point2x
            point1y = point2y
        print(count)
        if count % 2 == 0:
            out_dots[i] = "outside"
        else:
            in_dots[i] = "inside"


    """

    print(len(out_dots), "outdots") #DELETE
    print(len(bou_dots), "boundots") #DELETE
    print(len(idk_dots), "idkdots") #DELETE
    print(len(idk_dots_2), "idk_2 points") #DELETE
    #print(len(in_dots), "new points")  # DELETE


    classified_points = {**out_dots, **bou_dots, **idk_dots_2}
    #classified_points = {**out_dots, **bou_dots, **in_dots}
    print(classified_points) #DELETE
    """
    print("write output.csv")
    io.output_pointfile("output.csv", classified_points.items())
    """
    print("plot polygon and points")
    plotter = Plotter()
    plotter.add_polygon(x_polygon, y_polygon)  # plot Polygon

    #plt.plot([x_min, x_min, x_max, x_max, x_min], [y_min, y_max, y_max, y_min, y_min])  # plot MBR
    plotter.add_all_point(classified_points.items())

    #Can be deleted after tests
    """
    for key, value in classified_points.items():
        x = float(key.get_x())
        y = float(key.get_y())
        kind = value
        plotter.add_point(x,y,kind)
    
    for key, value in out_dots.items():
        x = float(key.get_x())
        y = float(key.get_y())
        kind = value
        plotter.add_point(x, y, kind)

    
    for key, value in in_dots.items():
        x = float(key.get_x())
        y = float(key.get_y())
        kind = value
        plotter.add_point(x, y, kind)
    """

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
