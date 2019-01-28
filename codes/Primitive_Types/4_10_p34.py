###
#   File name  : 4_10_p34.py
#   Author     : Hyunjin Kim
#   Date       : Jan 28, 2018
#   Email      : firadazer@gmail.com
#   Purpose    : How would you implement a random number generator that generates
#                a  random integer i between a and b, inclusive, given a random
#                number generator that produces zero or one with equal probability?
#                All values in [a,b] should be equally likely.
#   Background : This problem is motivated by the following scenario.
#                Six friends have to select a designated driver using a single
#                unbiased coin. The process should be fair to everyone.
#
#   Instruction
#               1. import 4_10_p34
#               2. Run the function 4_10_p34.start()
#               3. The results will be generated in the console
###

### import modules
import timeit


### a function starting this script
def start():
    print("4_10_p34.py")

    start_time = timeit.default_timer()
    print("generate_random_num(1, 6) = ", generate_random_num(1, 6))
    print("generate_random_num(25, 125) = ", generate_random_num(25, 125))
    print("generate_random_num(3, 3) = ", generate_random_num(3, 3))
    print("generate_random_num(9, 54) = ", generate_random_num(9, 54))
    print("generate_random_num(48, 2) = ", generate_random_num(48, 2))
    print("Execution Time: ", timeit.default_timer() - start_time)


def generate_random_num(a, b):
    return(a)


start()
