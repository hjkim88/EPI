###
#   File name  : 5_12_p54.py
#   Author     : Hyunjin Kim
#   Date       : Nov 12, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : Implement an algorithm that takes as input an array of distinct elements and a size, and returns
#                a subset of the given size of the array elements. All subsets should be equally likely.
#                Return the result in input array itself.
#
#   Instruction
#               1. import 5_12_p54.py
#               2. Run the function 5_12_p54.start()
#               3. The results will be generated in the console
###

### import modules
import timeit
import random

### a function starting this script
def start():
    print("5_12_p54.py")

    start_time = timeit.default_timer()
    print("random_subset([54, 5, 3, 67, 0], 3) = ", random_subset([54, 5, 3, 67, 0], 3))
    print("random_subset([54, 5, 3, 67, 0], 3) = ", random_subset([54, 5, 3, 67, 0], 3))
    print("random_subset([54, 5, 3, 67, 0], 4) = ", random_subset([54, 5, 3, 67, 0], 4))
    print("random_subset([54, 5, 3, 67, 0], 4) = ", random_subset([54, 5, 3, 67, 0], 4))
    print("Execution Time: ", timeit.default_timer() - start_time)


### a function to return random subset of a given array A with a size
def random_subset(A, size):
    idx = random.sample(range(len(A)), size)
    idx.sort()

    return [A[x] for x in idx]


start()
