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
    print("fun_one(Point(-3,4), Point(2,7), Point(5,-1), Point(0,-5) = ",
          fun_one(Point(-3,4), Point(2,7), Point(5,-1), Point(0,-5)))
    print("fun_one(Point(0,0), Point(0,8), Point(-4,4), Point(4,4) = ",
          fun_one(Point(0,0), Point(0,8), Point(-4,4), Point(4,4)))
    print("Execution Time: ", timeit.default_timer() - start_time)


### a function to check that the four given points represent a rectangle
Point = collections.namedtuple("Point", ("x", "y"))

### a function to calculate cosine similarity of given two points
def cosine_similarity(p_main, p1, p2):
    new_p1 = Point(p_main.x - p1.x, p_main.y - p1.y)
    new_p2 = Point(p_main.x - p2.x, p_main.y - p2.y)
    return new_p1.x * new_p2.x + new_p1.y * new_p2.y

### there should be 4 right angles
def fun_one(p1, p2, p3, p4):
    ### get the closest two points to the p1
    dist2 = (p1.x - p2.x)**2 + (p1.y - p2.y)**2
    dist3 = (p1.x - p3.x)**2 + (p1.y - p3.y)**2
    dist4 = (p1.x - p4.x)**2 + (p1.y - p4.y)**2
    dist_max = max(dist2, dist3, dist4)

    isRectangle = False

    ### the most-far point is diagonal to the p1, and the other two also should be diagonal
    if dist_max == dist2:
        if cosine_similarity(p1, p3, p4) == 0 and cosine_similarity(p2, p3, p4) == 0 and cosine_similarity(p3, p1, p2) == 0 and cosine_similarity(p4, p1, p2) == 0:
            isRectangle = True
    elif dist_max == dist3:
        if cosine_similarity(p1, p2, p4) == 0 and cosine_similarity(p3, p2, p4) == 0 and cosine_similarity(p2, p1, p3) == 0 and cosine_similarity(p4, p1, p3) == 0:
            isRectangle = True
    else:
        if cosine_similarity(p1, p2, p3) == 0 and cosine_similarity(p4, p2, p3) == 0 and cosine_similarity(p2, p1, p4) == 0 and cosine_similarity(p3, p1, p4) == 0:
            isRectangle = True

    return isRectangle


start()
