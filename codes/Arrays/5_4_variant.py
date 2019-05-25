###
#   File name  : 5_4_variant.py
#   Author     : Hyunjin Kim
#   Date       : May 25, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : 1. Write a program to compute the minimum number of steps needed to advance
#                to the last location.
#
#   Background : This is related to the "5_4_p44.py".
#
#   Example    : if A = [3, 3, 1, 0, 2, 0, 1], return 4
#                if A = [3, 2, 0, 0, 2, 0, 1], return 0
#                if A = [10, 3, 1, 0, 2, 0, 1], return 1
#                if A = [1, 1, 1, 1, 1, 1, 1], return 7
#
#
#   Instruction
#               1. import 5_4_variant
#               2. Run the function 5_4_variant.start()
#               3. The results will be generated in the console
###

### import modules
import timeit

### a function starting this script
def start():
    print("5_4_variant.py")

    start_time = timeit.default_timer()
    print("")
    print("Execution Time: ", timeit.default_timer() - start_time)


### a function to calculate minimum steps to advance to the last index
def minimum_step(A):

    return 0


start()
