class IO_file:

    def __init__(self):

    def input_file(self, filename):

        with open(filename, "r") as file:
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
                polygon_lines.append(Line(prev, i))
                prev = i

        for i in polygon_lines:
            a, b = i.get_points()
            print(a.get_x(), a.get_y(), b.get_x(), b.get_y())

