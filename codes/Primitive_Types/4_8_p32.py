###
#   File name  : 4_8_p32.py
#   Author     : Hyunjin Kim
#   Date       : Jan 23, 2018
#   Email      : firadazer@gmail.com
#   Purpose    : Write a program which takes an integer and returns the integer
#                corresponding to the digits of the input written in reverse order.
#   Example    : The reverse of 42 is 24, and the reverse of -314 is -413.
#
#   Instruction
#               1. import 4_8_p32
#               2. Run the function 4_8_p32.start()
#               3. The results will be generated in the console
###

### import modules
import timeit


### a function starting this script
def start():
    print("4_8_p32.py")

    start_time = timeit.default_timer()
    print()
    print("Execution Time: ", timeit.default_timer() - start_time)


### a brute-force function to return reversed digit of a given integer
def reverseDigit(x):
    return(x)


start()
