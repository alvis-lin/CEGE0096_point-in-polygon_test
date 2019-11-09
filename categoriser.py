from Geometry import Point, Line, Polygon

class Categoriser():

    def mbr_check(self, inputpoints, x_polygon, y_polygon):

        x_max = max(x_polygon)
        x_min = min(x_polygon)
        y_max = max(y_polygon)
        y_min = min(y_polygon)

        out_dots = {}  # Outside points that are categorised
        idk_dots = {}  # Points left need to be categorised

        for i in inputpoints:
            if float(i.get_x()) > x_max or float(i.get_x()) < x_min:
                out_dots[i] = "outside"
            elif float(i.get_y()) > y_max or float(i.get_y()) < y_min:
                out_dots[i] = "outside"
            else:
                idk_dots[i] = "idk"

        return out_dots, idk_dots

    def boundary_check(self, idk, polyline):

        bou_dots = {}

        for i in idk:
            a, b = float(i.get_x()), float(i.get_y())
            for poly in polyline:
                la, lb = poly.get_points()
                lax, lay, lbx, lby = la.get_x(), la.get_y(), lb.get_x(), lb.get_y()
                res = ""
                if max(lax, lbx) >= a >= min(lax, lbx) and max(lay, lby) >= b >= min(lay, lby):
                    if lbx == lax:  # means points on vertical line
                        res = "online"
                    elif b == (a - lax) / (lbx - lax) * (lby - lay) + lay:
                        res = "online"
                    else:
                        res = "not online"

                #print(res)

                if res == "online":
                    bou_dots[i] = "boundary"

        return bou_dots

    def rca_check(self, idk2, polypoints, out_dot):

        in_dots = {}

        point1 = polypoints[0]

        for i in idk2:
            x, y = i.get_x(), i.get_y()
            count = 0
            for a in range(1, len(polypoints)):
                point2 = polypoints[a]
                if (point1.get_y() < y and point2.get_y() >= y) or (point1.get_y() >= y and point2.get_y() < y):
                    # 求线段与射线交点 再和lat比较
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

