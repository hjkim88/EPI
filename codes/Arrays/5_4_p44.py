###
#   File name  : 5_4_p44.py
#   Author     : Hyunjin Kim
#   Date       : May 25, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : Write a program which takes an array of n integers, where A[i] denotes the maximum you can
#                advance from index i, and returns whether it is possible to advance to the last index
#                starting from the beginning of the array.
#   Example    : if A = [3, 3, 1, 0, 2, 0, 1], return True
#                if A = [3, 2, 0, 0, 2, 0, 1], return False
#
#   Instruction
#               1. import 5_4_p44.py
#               2. Run the function 5_4_p44.start()
#               3. The results will be generated in the console
###

### import modules
import timeit

### a function starting this script
def start():
    print("5_4_p44.py")

    start_time = timeit.default_timer()
    print("")
    print("Execution Time: ", timeit.default_timer() - start_time)


### a function to tell whether the input array is advancable or not
def isAdvancable(A):
    
    return False


start()
