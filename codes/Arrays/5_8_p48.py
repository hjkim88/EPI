###
#   File name  : 5_8_p48.py
#   Author     : Hyunjin Kim
#   Date       : Jun 11, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : Write a program that takes an array A of n numbers, and rearranges A's elements to get a new array
#                B having the property that B[0] <= B[1] >= B[2] <= B[3] >= B[4] <= B[5] >= ...
#
#   Example    : input: [3, 4, 1, 54, 32, 42, 7, 5, 43] -> output: [3, 4, 1, 54, 32, 42, 5, 43, 7]
#
#   Instruction
#               1. import 5_8_p48.py
#               2. Run the function 5_8_p48.start()
#               3. The results will be generated in the console
###

### import modules
import timeit

### a function starting this script
def start():
    print("5_8_p48.py")

    start_time = timeit.default_timer()
    print("")
    print("Execution Time: ", timeit.default_timer() - start_time)


start()
