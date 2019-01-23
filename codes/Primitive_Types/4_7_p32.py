###
#   File name  : 4_7_p32.py
#   Author     : Hyunjin Kim
#   Date       : Jan 23, 2018
#   Email      : firadazer@gmail.com
#   Purpose    : Write a program that takes a double x and an integer y
#                and returns x**y. You can ignore overflow and underflow.
#   Example    : 2**3 = 8, 5**0 = 1, 23**2 = 529
#
#   Instruction
#               1. import 4_7_p32
#               2. Run the function 4_7_p32.start()
#               3. The results will be generated in the console
###

### import modules
import timeit


### a function starting this script
def start():
    print("4_7_p32.py")

    start_time = timeit.default_timer()
    print()
    print("Execution Time: ", timeit.default_timer() - start_time)


### a brute-force function to calculate x**y without using **
def getExponent(x, y):
    return(x**y)

