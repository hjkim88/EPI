###
#   File name  : 4_5_p29.py
#   Author     : Hyunjin Kim
#   Date       : Jan 20, 2018
#   Email      : firadazer@gmail.com
#   Purpose    : Write a program that multiplies two nonnegative integers.
#                The only operators you are allowed to use are:
#                - assignment
#                - the bitwise operators >>, <<, |, &, ~, ^
#                - equality checks and boolean combinations thereof
#                You may use loops and functions that you write yourself.
#                These constraints imply, for example, that you cannot
#                use increment or decrement, or test if x < y.
#   Background : Sometimes the processors used in ultra low-power devices
#                such as hearing aids do not have dedicated hardware for
#                performing multiplication. A program that needs to perform
#                multiplication must do so explicitly using lower-level primitives.
#
#   Instruction
#               1. import 4_5_p29
#               2. Run the function 4_5_p29.start()
#               3. The results will be generated in the console
###

### import modules
import timeit


### a function starting this script
def start():
    print("4_5_p29.py")

    start_time = timeit.default_timer()
    print()
    print("Execution Time: ", timeit.default_timer() - start_time)


###
def multiply(x, y):
    return 0