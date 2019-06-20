###
#   File name  : 5_10_variant.py
#   Author     : Hyunjin Kim
#   Date       : Jun 19, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : 1. Given an array A of integers representing a permutation, update A to represent
#                the inverse permutation using only constant additional storage.
#
#   Background : This is related to the "5_10_p50.py".
#
#   Example    : input: [3, 8, 5, 10, 9, 4, 6, 1, 7, 2, 0], output: [10, 7, 9, 0, 5, 2, 6, 8, 1, 4, 3]
#                input: [0, 1, 2, 3, 4], output: [0, 1, 2, 3, 4]
#                input: [2, 1, 4, 5, 0, 3], output: [4, 1, 0, 5, 2, 3]
#                input: [6, 5, 2, 1, 0, 3, 4], output: [4, 3, 2, 5, 6, 1, 0]
#                input: [3, 2, 1, 0], output: [3, 2, 1, 0]
#
#   Instruction
#               1. import 5_10_variant
#               2. Run the function 5_10_variant.start()
#               3. The results will be generated in the console
###

### import modules
import timeit

### a function starting this script
def start():
    print("5_10_variant.py")

    start_time = timeit.default_timer()
    print("inverse([3, 8, 5, 10, 9, 4, 6, 1, 7, 2, 0]) = ", inverse([3, 8, 5, 10, 9, 4, 6, 1, 7, 2, 0]))
    print("inverse([0, 1, 2, 3, 4]) = ", inverse([0, 1, 2, 3, 4]))
    print("inverse([2, 1, 4, 5, 0, 3]) = ", inverse([2, 1, 4, 5, 0, 3]))
    print("inverse([6, 5, 2, 1, 0, 3, 4]) = ", inverse([6, 5, 2, 1, 0, 3, 4]))
    print("inverse([3, 2, 1, 0]) = ", inverse([3, 2, 1, 0]))
    print("Execution Time: ", timeit.default_timer() - start_time)


### a function to inverse the input permutation
### time complexity: O(n), space complexity: O(1)
### in the 5_10_p50.py, there are two arrays A and P, so we could change P to mark cycles
### but here, there is only P array
### how to mark an index is already cycled?
def inverse(P):
    for i in range(len(P)):
        next_idx = i
        temp = -1
        if P[next_idx] >= 0:
            while P[next_idx] >= 0:
                P[next_idx], next_idx, temp = temp-len(P), P[next_idx], next_idx
            P[next_idx] = temp-len(P)

    for i in range(len(P)):
        P[i] += len(P)

    return P


start()
