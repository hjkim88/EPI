###
#   File name  : 5_12_variant.py
#   Author     : Hyunjin Kim
#   Date       : Nov 13, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : The rand() function in the standard C library returns a uniformly random number in [0, RAND_MAX-1].
#                Does rand() mod n generate a number uniformly distributed in [0, n-1]?
#
#   Background : This is related to the "5_12_p54.py".
#
#   Instruction
#               1. import 5_12_variant
#               2. Run the function 5_12_variant.start()
#               3. The results will be generated in the console
###

### import modules
import timeit
import numpy
import seaborn
import matplotlib.pyplot as plt

### a function starting this script
def start():
    print("5_12_variant.py")

    start_time = timeit.default_timer()
    plt.show(printRandDist(100, 10000))
    print("Execution Time: ", timeit.default_timer() - start_time)


### print a barplot of random numbers
def printRandDist(max, n):
    numpy.random.seed(0)
    x = numpy.random.rand(n) * (max-1)
    bar_plot = seaborn.distplot(x)

    return bar_plot


start()
