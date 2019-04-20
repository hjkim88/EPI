###
#   File name  : 5_1_p39.py
#   Author     : Hyunjin Kim
#   Date       : Apr 20, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : Write a program that takes an array A and an index i into A,
#                and rearranges the elements such that all elements less than
#                A[i](the "pivot") appear first, followed by elements equal to
#                the pivot, followed by elements greater than the pivot.
#   Example    : A = <0, 1, 2, 0, 2, 1, 1> and pivot index = 3,
#                a valid partitioning = <0, 0, 1, 2, 2, 1, 1>
#                if pivot index = 2, then <0, 1, 0, 1, 1, 2, 2>
#
#   Instruction
#               1. import 5_1_p39
#               2. Run the function 5_1_p39.start()
#               3. The results will be generated in the console
###

### import modules
import timeit

### a function starting this script
def start():
    print("5_1_p39.py")

    ### print the parity of the examples
    start_time = timeit.default_timer()
    print("Execution Time: ", timeit.default_timer() - start_time)

