###
#   File name  : 4_11_variant.py
#   Author     : Hyunjin Kim
#   Date       : Feb 22, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : 1. Given four points in the plane, how would you check if they are the vertices of a rectangle?
#                2. How would you check if two rectangles, not necessarily aligned with the X and Y axes, intersect?
#
#   Background : This is related to the "4_11_p35.py".
#
#   Instruction
#               1. import 4_11_variant
#               2. Run the function 4_11_variant.start()
#               3. The results will be generated in the console
###

### import modules
import timeit
import collections


###
Point = collections.namedtuple("Point", ("x", "y"))


### a function starting this script
def start():
    print("4_11_p35.py")

    start_time = timeit.default_timer()
    print("fun_one(Point(1,7), Point(4,2), Point(1,2), Point(4,7) = ",
          fun_one(Point(1,7), Point(4,2), Point(1,2), Point(4,7)))
    print("fun_one(Point(2,4), Point(6,4), Point(4,8), Point(3,9) = ",
          fun_one(Point(2,4), Point(6,4), Point(4,8), Point(3,9)))
    print("fun_one(Point(8,6), Point(3,2), Point(3,6), Point(8,2) = ",
          fun_one(Point(8,6), Point(3,2), Point(3,6), Point(8,2)))
    print("Execution Time: ", timeit.default_timer() - start_time)


### a function to check that the four given points represent a rectangle
### first, sort the x-axis points and y-axis points each,
### then check point pairs are clustered
def fun_one(p1, p2, p3, p4):
    a = [p1.x, p2.x, p3.x, p4.x]
    b = [p1.y, p2.y, p3.y, p4.y]
    a.sort()
    b.sort()

    if(a[0] == a[1] and a[2] == a[3] and b[0] == b[1] and b[2] == b[3]):
        return True
    else:
        return False


start()
