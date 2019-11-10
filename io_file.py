from Geometry import Point, Line


class IoFile:

    def input_polyfile(self):
        filename = str(input("Please insert polygon csv filename(i.e., file.csv): "))
        with open(filename, "r") as file:
            next(file)
            polygon_points = []  # store point objects of the polygon points
            x_polygon = []  # store x coordinates of polygon
            y_polygon = []  # store y coordinates of polygon
            for line in file:
                data = line.strip().split(",")
                # use data to make point objects
                polygon_points.append(Point(float(data[0]), float(data[1]), float(data[2])))
                x_polygon.append(float(data[1]))
                y_polygon.append(float(data[2]))
            polygon_lines = []
            prev = polygon_points[0]
            for i in polygon_points[1:]:
                polygon_lines.append(Line(prev, i))
                prev = i
        return polygon_points, x_polygon, y_polygon, polygon_lines

    def input_pointfile(self):

        filename = str(input("Please enter your points csv filename (i.e., file.csv): "))
        with open(filename, "r") as input_file:
            next(input_file)
            input_points = [] # store point objects of the input points
            for line in input_file:
                data = line.strip().split(",")
                input_points.append(Point(float(data[0]), float(data[1]), float(data[2])))
        return input_points

    def output_pointfile(self, res):
        filename = str(input("Please insert preferred export filename(i.e., file.csv): "))
        with open(filename, "w") as f:
            f.writelines("x, y, classification" + "\n")
            for key, value in res:
                x = key.get_x()
                y = key.get_y()
                kind = value
                f.writelines(str(x) + "," + str(y) + "," + str(kind) + "\n")

    def input_pointfile_user(self, x, y):

        input_points = []
        input_points.append(Point("user", x, y))
        return input_points

    def output_pointfile_user(self, res):

        for key, value in res:
            kind = str(value)
            if kind == "inside":
                print("Inside!")
            elif kind == "boundary":
                print("Boundary!")
            elif kind == "outside":
                print("Outside!")
