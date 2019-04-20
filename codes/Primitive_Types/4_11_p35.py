###
#   File name  : 4_11_p35.py
#   Author     : Hyunjin Kim
#   Date       : Jan 28, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : Write a program which tests if two rectangles have a nonempty intersection.
#                If the intersection is nonempty, return the rectangle formed by their intersection.
#
#   Background : This problem is concerned with rectangles whose sides are parallel to the X-axis and Y-axis.
#
#   Instruction
#               1. import 4_11_p35
#               2. Run the function 4_11_p35.start()
#               3. The results will be generated in the console
###

### import modules
import timeit
import collections


### a function starting this script
def start():
    print("4_11_p35.py")

    start_time = timeit.default_timer()
    print("rect_intersect(1, 6, 7, 10, 4, 12, 2, 8) = ", rect_intersect(1, 6, 7, 10, 4, 12, 2, 8))
    print("rect_intersect(20, 36, 5, 12, 2, 25, 4, 15) = ", rect_intersect(20, 36, 5, 12, 2, 25, 4, 15))
    print("rect_intersect(3, 17, 7, 13, 8, 25, 2, 11) = ", rect_intersect(3, 17, 7, 13, 8, 25, 2, 11))
    print("rect_intersect(1, 7, 5, 10, 11, 19, 2, 7) = ", rect_intersect(1, 7, 5, 10, 11, 19, 2, 7))
    print("rect_intersect(7, 12, 2, 8, 3, 16, 5, 14) = ", rect_intersect(7, 12, 2, 8, 3, 16, 5, 14))
    print("Execution Time: ", timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    print("intersect_rectangle(Rectangle(1, 7, 5, 3), Rectangle(4, 2, 8, 6)) = ",
          intersect_rectangle(Rectangle(1, 7, 5, 3), Rectangle(4, 2, 8, 6)))
    print("intersect_rectangle(Rectangle(20, 5, 11, 7), Rectangle(2, 4, 23, 11)) = ",
          intersect_rectangle(Rectangle(20, 5, 11, 7), Rectangle(2, 4, 23, 11)))
    print("intersect_rectangle(Rectangle(3, 7, 14, 6), Rectangle(8, 2, 17, 9)) = ",
          intersect_rectangle(Rectangle(3, 7, 14, 6), Rectangle(8, 2, 17, 9)))
    print("intersect_rectangle(Rectangle(1, 5, 6, 5), Rectangle(11, 2, 8, 5)) = ",
          intersect_rectangle(Rectangle(1, 5, 6, 5), Rectangle(11, 2, 8, 5)))
    print("intersect_rectangle(Rectangle(7, 2, 5, 6), Rectangle(3, 5, 13, 12)) = ",
          intersect_rectangle(Rectangle(7, 2, 5, 6), Rectangle(3, 5, 13, 12)))
    print("Execution Time: ", timeit.default_timer() - start_time)


### a function to return intersection of two rectangles
### a brute-force approach: check all the 9 cases
### won't implement this since it is a waste of time

### a more efficient approach
### if there is an intersection between two rectangles,
### order x-axis points and y-axis points separately
### take the middle two points each from the ordered x-axis points
###  and the ordered y-axis points, and return the 4 points
### otherwise, return NULL
### a = first rectangle's first x-axis point
### b = first rectangle's second x-axis point
### c = first rectangle's first y-axis point
### d = first rectangle's second y-axis point
### e = second rectangle's first x-axis point
### f = second rectangle's second x-axis point
### g = second rectangle's first y-axis point
### h = second rectangle's second y-axis point
###
### (Example)
### h         |--------------|
### d  |--------------|      |
###    |      |       |      |
### c  |--------------|      |
### g         |--------------|
###    a      e       b      f
###
def rect_intersect(a, b, c, d, e, f, g, h):
    if a >= f or e >= b or c >= h or g >= d:
        return None
    else:
        x = [a, b, e, f]
        y = [c, d, g, h]
        x.sort()
        y.sort()
        return x[1], x[2], y[1], y[2]


### hint: think of the X and Y dimensions independently.

### a function described in the book
### but mine is faster...
Rectangle = collections.namedtuple("Rectangle", ("x", "y", "width", "height"))

def intersect_rectangle(R1, R2):
    def is_intersect(R1, R2):
        return(R1.x <= R2.x + R2.width and R1.x + R1.width >= R2.x and
               R1.y <= R2.y + R2.height and R1.y + R1.height >= R2.y)

    if not is_intersect(R1, R2):
        return Rectangle(0, 0, -1, -1)
    return Rectangle(
        max(R1.x, R2.x),
        max(R1.y, R2.y),
        min(R1.x + R1.width, R2.x + R2.width) - max(R1.x, R2.x),
        min(R1.y + R1.height, R2.y + R2.height) - max(R1.y, R2.y))


start()
