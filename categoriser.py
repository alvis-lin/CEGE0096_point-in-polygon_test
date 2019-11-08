from Geometry import Point, Line, Polygon

class Categoriser():

    def mbr(self, inputpoints, x_polygon, y_polygon):

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
            print(a - b)
            for poly in polyline:
                la, lb = poly.get_points()
                lax, lay, lbx, lby = float(la.get_x()), float(la.get_y()), float(lb.get_x()), float(lb.get_y())
                res = ""
                if max(lax, lbx) >= a >= min(lax, lbx) and max(lay, lby) >= b >= min(lay, lby):
                    if lbx == lax:  # means points on vertical line
                        res = "online"
                    elif b == (a - lax) / (lbx - lax) * (lby - lay) + lay:
                        res = "online"
                    else:
                        res = "not online"

                print(res)

                if res == "online":
                    bou_dots[i] = "boundary"

        return bou_dots
