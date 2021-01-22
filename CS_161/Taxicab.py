# Author: Ty Vareka
# Date: 1/28/2020
# Description: Taxicab program with private data members.  Program holds current x/y coordinates and odometer reading
class Taxicab:
    """Represents the Taxicab's x/y coordinate and odometer reading"""
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._odometer = 0
    def get_x_coord(self):
        return self._x
    def get_y_coord(self):
        return self._y
    def get_odometer(self):
        return self._odometer
    def move_x(self, x):
        self._x += x
        self._odometer += abs(x)
    def move_y(self, y):
        self._y += y
        self._odometer += abs(y)


