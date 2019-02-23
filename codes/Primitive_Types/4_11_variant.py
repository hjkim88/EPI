###
#   File name  : 4_11_variant.py
#   Author     : Hyunjin Kim
#   Date       : Feb 22, 2018
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


### a function starting this script
def start():
    print("4_11_p35.py")

    start_time = timeit.default_timer()
    print("fun_one(Point(1,7), Point(4,2), Point(1,2), Point(4,7) = ",
          fun_one(Point(1,7), Point(4,2), Point(1,2), Point(4,7)))
    print("Execution Time: ", timeit.default_timer() - start_time)


### a function to check that the four given points represent a rectangle
Point = collections.namedtuple("Point", ("x", "y"))

def fun_one(p1, p2, p3, p4):
    return None


start()
