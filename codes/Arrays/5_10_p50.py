###
#   File name  : 5_10_p50.py
#   Author     : Hyunjin Kim
#   Date       : Jun 16, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : Given an array A of n elements and a permutation P, apply P to A.
#
#   Example    : input: A = ['a', 'b', 'c', 'd'], P = [2, 0, 1, 3], output: ['b', 'c', 'a', 'd']
#                input: A = [1, 2, 3, 4], P = [3, 2, 1, 0], output: [4, 3, 2, 1]
#                input: A = [54, 3, 64, 2], P = [2, 3, 0, 1], output: [64, 2, 54, 3]
#                input: A = [7, 4, 5, 5], P = [1, 3, 0, 2], output: [5, 7, 5, 4]
#                input: A = ['e', 'e', 'e', 'e'], P = [3, 1, 2, 0], output: ['e', 'e', 'e', 'e']
#
#   Instruction
#               1. import 5_10_p50.py
#               2. Run the function 5_10_p50.start()
#               3. The results will be generated in the console
###

### import modules
import timeit

### a function starting this script
def start():
    print("5_10_p50.py")

    start_time = timeit.default_timer()
    print("applyPerm(['a', 'b', 'c', 'd'], [2, 0, 1, 3]) = ", applyPerm(['a', 'b', 'c', 'd'], [2, 0, 1, 3]))
    print("applyPerm([1, 2, 3, 4], [3, 2, 1, 0]) = ", applyPerm([1, 2, 3, 4], [3, 2, 1, 0]))
    print("applyPerm([54, 3, 64, 2], [2, 3, 0, 1]) = ", applyPerm([54, 3, 64, 2], [2, 3, 0, 1]))
    print("applyPerm([7, 4, 5, 5], [1, 3, 0, 2]) = ", applyPerm([7, 4, 5, 5], [1, 3, 0, 2]))
    print("applyPerm(['e', 'e', 'e', 'e'], [3, 1, 2, 0]) = ", applyPerm(['e', 'e', 'e', 'e'], [3, 1, 2, 0]))
    print("Execution Time: ", timeit.default_timer() - start_time)


### a brute-force approach would be from 0 to len(P) of P, B[P[i]] = A[i]
### time complexity: O(n), space complexity: O(n)
def applyPerm(A, P):
    B = [None] * len(A)
    for i in range(len(P)):
        B[P[i]] = A[i]

    return B


start()
