###
#   File name  : 5_11_variant.py
#   Author     : Hyunjin Kim
#   Date       : Jun 20, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : 1. Compute the k-th permutation under dictionary ordering, starting from the identity permutation
#                (which is the first permutation in dictionary ordering).
#                2. Given a permutation P, return the permutation corresponding to the previous permutation of P
#                under dictionary ordering.
#
#   Background : This is related to the "5_11_p52.py".
#
#   Instruction
#               1. import 5_11_variant
#               2. Run the function 5_11_variant.start()
#               3. The results will be generated in the console
###

### import modules
import timeit

### a function starting this script
def start():
    print("5_11_variant.py")

    start_time = timeit.default_timer()
    print("")
    print("Execution Time: ", timeit.default_timer() - start_time)


start()
