###
#   File name  : 5_2_p43.py
#   Author     : Hyunjin Kim
#   Date       : May 11, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : Write a program which takes as input an array of digits encoding a decimal integer D
#                and updates the array to represent the integer D+1. Your algorithm should work
#                even if it is implemented in a language that has finite-precision arithmetic.
#   Example    : If the input is [1, 2, 9] then you should update the array to [1, 3, 0].
#
#   Instruction
#               1. import 5_2_p43.py
#               2. Run the function 5_2_p43.start()
#               3. The results will be generated in the console
###

### import modules
import timeit

### a function starting this script
def start():
    print("5_2_p43.py")

    start_time = timeit.default_timer()
    print("")
    print("Execution Time: ", timeit.default_timer() - start_time)


start()
