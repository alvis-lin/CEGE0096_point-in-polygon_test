class Categoriser():

    def mbr_check(self, inputpoints, x_polygon, y_polygon):

        # get the boundary of mbr
        x_max = max(x_polygon)
        x_min = min(x_polygon)
        y_max = max(y_polygon)
        y_min = min(y_polygon)

        out_dots = {}  # outside points will be stored here
        idk_dots = {}  # points unclassified will be stored here

        for i in inputpoints:
            if float(i.get_x()) > x_max or float(i.get_x()) < x_min:
                out_dots[i] = "outside"
            elif float(i.get_y()) > y_max or float(i.get_y()) < y_min:
                out_dots[i] = "outside"
            else:
                idk_dots[i] = "idk"

        return out_dots, idk_dots


    def mbr_check_user(self, x, y, x_polygon, y_polygon):

        # get the boundary of mbr
        x_max = max(x_polygon)
        x_min = min(x_polygon)
        y_max = max(y_polygon)
        y_min = min(y_polygon)

        out_dots = {}  # outside points will be stored here
        idk_dots = {}  # points unclassified will be stored here

        if x > x_max or x < x_min:
            out_dots[i] = "outside"
        elif y > y_max or y < y_min:
            out_dots[i] = "outside"
        else:
            idk_dots[i] = "idk"

        return out_dots, idk_dots


    def pol_check(self, idk, polyline):

        bou_dots = {}  # boundary points will be stored here

        for i in idk:
            a, b = float(i.get_x()), float(i.get_y())
            for poly in polyline:
                la, lb = poly.get_points()
                lax, lay, lbx, lby = la.get_x(), la.get_y(), lb.get_x(), lb.get_y()
                res = ""
                if max(lax, lbx) >= a >= min(lax, lbx) and max(lay, lby) >= b >= min(lay, lby):
                    if lbx == lax:  # means points are on vertical line
                        res = "online"
                    elif b == (a - lax) / (lbx - lax) * (lby - lay) + lay:
                        res = "online"
                    else:
                        res = "not online"

                if res == "online":
                    bou_dots[i] = "boundary"

        return bou_dots


    def rca_check(self, idk2, polypoints, out_dot):

        in_dots = {}  # inside points will be stored here
        point1 = polypoints[0]

        for i in idk2:
            x, y = i.get_x(), i.get_y()
            count = 0
            for a in range(1, len(polypoints)):
                point2 = polypoints[a]
                #  check if the points of segment is on the either side of ray,
                #  if not, ray and segment do not intersect
                if (point1.get_y() < y and point2.get_y() >= y) or (point1.get_y() >= y and point2.get_y() < y):
                    # find the intersection of ray and segment, then compare with x
                    point12lng = point2.get_x() - (point2.get_y() - y) * (point2.get_x() - point1.get_x()) / (
                                point2.get_y() - point1.get_y())
                    if point12lng < x:
                        count += 1
                point1 = point2
            if count % 2 == 0:
                out_dot[i] = "outside"
            else:
                in_dots[i] = "inside"

        return in_dots, out_dot

