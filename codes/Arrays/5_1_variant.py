###
#   File name  : 5_1_variant.py
#   Author     : Hyunjin Kim
#   Date       : May 11, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : 1. Assuming that keys take one of three values, reorder the array
#                   so that all objects with the same key appear together.
#                   The ordr of the subarrays is not important. For example,
#                   both Figures 5.1(b) and 5.1(c) on Page 40 are valid answers for
#                   Figure 5.1(a) on Page 40. Use O(1) additional space and O(n) time.
#                2. Given an array A of n objects with keys that takes one of four values,
#                   reorder the array so that all objects that have the same key appear together.
#                   Use O(1) additional space and O(n) time.
#                3. Given an array A of n objects with Boolean-valued keys, reorder the array
#                   so that objects that have the key false appear first. Use O(1) additional
#                   space and O(n) time.
#                4. Given an array A of n objects with Boolean-valued keys, reorder the array
#                   so that objects that have the keay false appear first. The relative ordering
#                   of objects with key true should not change. Use O(1) additional space
#                   and O(n) time.
#
#   Background : This is related to the "5_1_p39.py".
#
#   Instruction
#               1. import 5_1_variant
#               2. Run the function 5_1_variant.start()
#               3. The results will be generated in the console
###

### import modules
import timeit

### a function starting this script
def start():
    print("5_1_variant.py")

    start_time = timeit.default_timer()
    print("")
    print("Execution Time: ", timeit.default_timer() - start_time)


### a function for the first task
def fun_one(A):
    return A


start()
