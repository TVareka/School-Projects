# Author: Ty Vareka
# Date: 4/20/2020
# Description: Create a box class with parameters length, width, and height.  Each box class will have a method
# volume which returns the volume of the box.  Then a separate function will use insertion sorting to sort a list
# of boxes from greatest volume to least volume of the box

class Box:
    """Box class with parameters length, width, and height.  Also has a method for calculating volume of the box"""

    def __init__(self, length, width, height):
        self._length = length
        self._width = width
        self._height = height

    def get_length(self):
        return self._length

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def volume(self):
        return (self._length * self._width * self._height)

def box_sort(a_list):
    """sorts a_list in descending order"""

    for index in range(1, len(a_list)):
        value = a_list[index].volume()
        box = a_list[index]
        pos = index - 1
        while pos >= 0 and a_list[pos].volume() < value:
            a_list[pos + 1] = a_list[pos]
            pos -= 1
        a_list[pos + 1] = box


def main():
    '''simple test parameters'''
    b1 = Box(3.4, 19.8, 2.1)
    b2 = Box(1.0, 1.0, 1.0)
    b3 = Box(8.2, 8.2, 4.5)
    box_list = [b1, b2, b3]
    box_sort(box_list)
    print(box_list[0].volume(), box_list[1].volume(), box_list[2].volume())

if __name__ == "__main__":
    main()

