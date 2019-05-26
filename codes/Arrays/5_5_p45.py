###
#   File name  : 5_5_p45.py
#   Author     : Hyunjin Kim
#   Date       : May 26, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : Write a program which takes as input a sorted array and updates it so that all duplicates
#                have been removd and the remaining elements have been shifted left to fill the emptied
#                indices. Return the number of valid elements. Many languages have library functions for
#                performing this operation - you cannot use thses functions.
#
#   Example    : For the array [2, 3, 5, 5, 7, 11, 11, 11, 13], then after deletion,
# #              the array is [2, 3, 5, 7, 11, 13, 0, 0, 0].
#
#   Instruction
#               1. import 5_5_p45.py
#               2. Run the function 5_5_p45.start()
#               3. The results will be generated in the console
###

### import modules
import timeit

### a function starting this script
def start():
    print("5_5_p45.py")

    start_time = timeit.default_timer()
    print("")
    print("Execution Time: ", timeit.default_timer() - start_time)


### a function to delete duplicates in an array
def delete_duplicates(A):

    return A


start()
