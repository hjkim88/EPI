###
#   File name  : 5_11_p52.py
#   Author     : Hyunjin Kim
#   Date       : Jun 19, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : Write a program that takes as input a permutation, and returns the next permutation
#                under dictionary ordering. If the permutation is the last permutation, return the empty array.
#
#   Example    : input: [1, 0, 3, 2], output: [1, 2, 0, 3]
#                input: [3, 2, 1, 0], output: []
#                input: [3, 1, 0, 2, 4], output: [3, 1, 0, 4, 2]
#                input: [2, 0, 1, 3, 4, 5], output: [2, 0, 1, 3, 5, 4]
#                input: [0, 4, 2, 1, 3, 7, 6, 5], output: [0, 4, 2, 1, 5, 3, 6, 7]
#
#   Instruction
#               1. import 5_11_p52.py
#               2. Run the function 5_11_p52.start()
#               3. The results will be generated in the console
###

### import modules
import timeit

### a function starting this script
def start():
    print("5_11_p52.py")

    start_time = timeit.default_timer()
    print("")
    print("Execution Time: ", timeit.default_timer() - start_time)


start()
