###
#   File name  : 4_6_p31.py
#   Author     : Hyunjin Kim
#   Date       : Jan 23, 2018
#   Email      : firadazer@gmail.com
#   Purpose    : Given two positive integers, compute their quotient,
#                using only the addition, subtraction, and shifting operators.
#   Example    : 24 // 6 = 4, 16 // 3 = 5
#
#   Instruction
#               1. import 4_6_p31
#               2. Run the function 4_6_p31.start()
#               3. The results will be generated in the console
###

### import modules
import timeit


### a function starting this script
def start():
    print("4_6_p31.py")

    start_time = timeit.default_timer()
    print()
    print("Execution Time: ", timeit.default_timer() - start_time)


### a function that gives a quotient of two given positive integers as a return
def getQuotient(x, y):
    return(x // y)






