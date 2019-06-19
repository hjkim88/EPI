###
#   File name  : 5_10_variant.py
#   Author     : Hyunjin Kim
#   Date       : Jun 19, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : 1. Given an array A of integers representing a permutation, update A to represent
#                the inverse permutation using only constant additional storage.
#
#   Background : This is related to the "5_10_p50.py".
#
#   Example    : input: [3, 8, 5, 10, 9, 4, 6, 1, 7, 2, 0], output: [10, 7, 9, 0, 5, 2, 6, 8, 1, 4, 3]
#
#   Instruction
#               1. import 5_10_variant
#               2. Run the function 5_10_variant.start()
#               3. The results will be generated in the console
###

### import modules
import timeit

### a function starting this script
def start():
    print("5_10_variant.py")

    start_time = timeit.default_timer()
    print("")
    print("Execution Time: ", timeit.default_timer() - start_time)


start()
