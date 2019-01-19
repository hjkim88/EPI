###
#   File name  : 4_4_p28.py
#   Author     : Hyunjin Kim
#   Date       : Jan 19, 2018
#   Email      : firadazer@gmail.com
#   Purpose    : Write a program which takes as input a nonnegative integer x and returns a number y
#                which is not equal to x, but has the same weight as x and their difference,
#                |y-x|, is as small as possible. You can assume x is not 0, or all 1s.
#                You can assume the integer fits in 64 bits.
#   Example    : If x = 6, you should return 5.
#   Background : Define the weight of a nonnegative integer x to be the number of bits that are
#                set to 1 in its binary representation. For example, since 92 in base-2-equals
#                (1011100)2, the weight of 92 is 4.
#
#   Instruction
#               1. import 4_4_p28
#               2. Run the function 4_4_p28.start()
#               3. The results will be generated in the console
###

### import modules
import timeit


### a function starting this script
def start():
    print("4_4_p28.py")

    start_time = timeit.default_timer()
    print()
    print("Execution Time: ", timeit.default_timer() - start_time)


### a brute-force function to get the closest, same-weight integer of the input (n-bit word)
def getSameWeightVal(x, n):
    return x


start()
