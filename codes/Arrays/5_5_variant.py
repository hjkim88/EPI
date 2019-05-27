###
#   File name  : 5_5_variant.py
#   Author     : Hyunjin Kim
#   Date       : May 27, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : 1. Implement a function which takes as input an array and a key, and updates the array
#                so that all occurrences of the input key have been removed and the remaining elements have been
#                shifted left to fill the emptied indices. Return the number of remaining elements. There are no
#                requirements as to the values stored beyond the last valid element.
#                2. Write a program which takes as input a sorted array A of integers and a positive integer m,
#                and updates A so that if x appears m times in A it appears exactly min(2,m) times in A.
#                The update to A should be performed in one pass, and no additional storage may be allocated.
#
#   Background : This is related to the "5_5_p45.py".
#
#   Instruction
#               1. import 5_5_variant
#               2. Run the function 5_5_variant.start()
#               3. The results will be generated in the console
###

### import modules
import timeit

### a function starting this script
def start():
    print("5_5_variant.py")

    start_time = timeit.default_timer()
    print("")
    print("Execution Time: ", timeit.default_timer() - start_time)


start()
