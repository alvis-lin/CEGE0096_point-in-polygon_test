from Geometry import Point, Line, Polygon


class IO_file:

    def input_polyfile(self, filename):

        with open(filename, "r") as file:
            next(file)  # skip the first line in csv
            polygon_points = []  # to store point objects
            x_polygon = []  # to store x coordinates of polygon
            y_polygon = []  # to store y coordinates of polygon
            for line in file:
                data = line.strip().split(",")
                polygon_points.append(Point(float(data[0]), float(data[1]), float(data[2])))  # get data into Point() objects
                x_polygon.append(float(data[1]))  # the list of x coordinates to plot polygon
                y_polygon.append(float(data[2]))  # the list of y coordinates to plot polygon

            polygon_lines = []
            prev = polygon_points[0]
            for i in polygon_points[1:]:
                polygon_lines.append(Line(prev, i))
                prev = i

        for i in polygon_lines:
            a, b = i.get_points()
            #print(a.get_x(), a.get_y(), b.get_x(), b.get_y())

        return polygon_points, x_polygon, y_polygon, polygon_lines


    def input_pointfile(self, filename):

        with open(filename, "r") as input_file:
            next(input_file)

            input_points = []
            for line in input_file:
                data = line.strip().split(",")
                input_points.append(Point(float(data[0]), float(data[1]), float(data[2])))

        return input_points

    def output_pointfile(self, filename, res):

        with open(filename, "w") as f:
            f.writelines("x, y, classification" + "\n")
            for key, value in res:
                x = key.get_x()
                y = key.get_y()
                kind = value
                f.writelines(str(x) + "," + str(y) + "," + str(kind) + "\n")







