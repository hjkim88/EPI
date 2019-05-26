###
#   File name  : 5_4_variant.py
#   Author     : Hyunjin Kim
#   Date       : May 25, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : 1. Write a program to compute the minimum number of steps needed to advance
#                to the last location.
#
#   Background : This is related to the "5_4_p44.py".
#
#   Example    : if A = [3, 3, 1, 0, 2, 0, 1], return 4
#                if A = [3, 2, 0, 0, 2, 0, 1], return 0
#                if A = [10, 3, 1, 0, 2, 0, 1], return 2
#                if A = [1, 1, 1, 1, 1, 1, 1], return 7
#
#
#   Instruction
#               1. import 5_4_variant
#               2. Run the function 5_4_variant.start()
#               3. The results will be generated in the console
###

### import modules
import timeit

### a function starting this script
def start():
    print("5_4_variant.py")

    start_time = timeit.default_timer()
    print("minimum_step([3, 3, 1, 0, 2, 0, 1]) = ", minimum_step([3, 3, 1, 0, 2, 0, 1]))
    print("minimum_step([3, 2, 0, 0, 2, 0, 1]) = ", minimum_step([3, 2, 0, 0, 2, 0, 1]))
    print("minimum_step([10, 3, 1, 0, 2, 0, 1]) = ", minimum_step([10, 3, 1, 0, 2, 0, 1]))
    print("minimum_step([1, 1, 1, 1, 1, 1, 1]) = ", minimum_step([1, 1, 1, 1, 1, 1, 1]))
    print("minimum_step([0, 3, 1, 0, 2, 0, 1]) = ", minimum_step([0, 3, 1, 0, 2, 0, 1]))
    print("Execution Time: ", timeit.default_timer() - start_time)


### a function to calculate minimum steps to advance to the last index
def minimum_step(A):
    old_max_idx = 0
    max_idx = 0
    B = [0] * len(A)
    B[0] = 1

    for i in range(len(A)):
        if i > max_idx:
            break
        else:
            max_idx = max(max_idx, (i + A[i]))
            max_idx = min(max_idx, len(A)-1)
            B[(old_max_idx+1):max_idx+1] = [B[i] + 1] * (max_idx - old_max_idx)
            old_max_idx = max_idx

    return B[len(B)-1]


start()
