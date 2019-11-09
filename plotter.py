from collections import OrderedDict

import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')


class Plotter:

    def __init__(self):
        plt.figure()

    def add_polygon(self, xs, ys):
        plt.fill(xs, ys, 'lightblue', label='Polygon')


    def add_line(self, x, y):
        plt.plot(x, y, 'orange')


    def add_ray(self,res,x_max):
        for key, value in res:
            x = key.get_x()
            y = key.get_y()
            plt.axhline(y,x, x_max)


    def add_all_point(self,res):
        for key, value in res:
            x = key.get_x()
            y = key.get_y()
            kind = value
            if kind == "outside":
                plt.plot(x, y, "ro", label='Outside')
            elif kind == "boundary":
                plt.plot(x, y, "bo", label='Boundary')
            elif kind == "inside":
                plt.plot(x, y, "go", label='Inside')
            else:
                plt.plot(x, y, "ko", label='Unclassified')


    def add_point(self, x, y, kind=None):
        if kind == "outside":
            plt.plot(x, y, "ro", label='Outside')
        elif kind == "boundary":
            plt.plot(x, y, "bo", label='Boundary')
        elif kind == "inside":
            plt.plot(x, y, "go", label='Inside')
        else:
            plt.plot(x, y, "ko", label='Unclassified')


    def show(self):
        handles, labels = plt.gca().get_legend_handles_labels()
        by_label = OrderedDict(zip(labels, handles))
        plt.legend(by_label.values(), by_label.keys()) # loc needs to be adjusted
        plt.show()


