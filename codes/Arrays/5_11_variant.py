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
#   Example1   : input: P = [1, 0, 3, 2] & k = 2, output: [1, 2, 0, 3]
#                input: P = [3, 2, 1, 0] & k = 4, output: []
#                input: P = [3, 1, 0, 2, 4] & k = 3, output: [3, 1, 2, 0, 4]
#                input: P = [2, 0, 1, 3, 4, 5] & k = 4, output: [2, 0, 1, 4, 5, 3]
#                input: P = [0, 4, 2, 1, 3, 7, 6, 5] & k = 3, output: [0, 4, 2, 1, 5, 3, 7, 6]
#                input: P = [1, 5, 4, 3, 2, 0] & k = 2, output: [2, 0, 1, 3, 5, 4]
#
#   Example2   : input: P = [1, 0, 3, 2], output: [1, 0, 2, 3]
#                input: P = [3, 2, 1, 0], output: [3, 2, 0, 1]
#                input: P = [3, 1, 0, 2, 4], output: [3, 0, 4, 2, 1]
#                input: P = [2, 0, 1, 3, 4, 5], output: [1, 5, 4, 3, 2, 0]
#                input: P = [0, 4, 2, 1, 3, 7, 6, 5], output: [0, 4, 2, 1, 3, 7, 5, 6]
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
    print("k_th_permut([1, 0, 3, 2], 2) = ", k_th_permut([1, 0, 3, 2], 2))
    print("k_th_permut([3, 2, 1, 0], 4) = ", k_th_permut([3, 2, 1, 0], 4))
    print("k_th_permut([3, 1, 0, 2, 4], 3) = ", k_th_permut([3, 1, 0, 2, 4], 3))
    print("k_th_permut([2, 0, 1, 3, 4, 5], 4) = ", k_th_permut([2, 0, 1, 3, 4, 5], 4))
    print("k_th_permut([0, 4, 2, 1, 3, 7, 6, 5], 3) = ", k_th_permut([0, 4, 2, 1, 3, 7, 6, 5], 3))
    print("k_th_permut([1, 5, 4, 3, 2, 0], 2) = ", k_th_permut([1, 5, 4, 3, 2, 0], 2))
    print("Execution Time: ", timeit.default_timer() - start_time)


### from the end, find the lower value than the end
### if found, swap it with the end and swap the next right with the swapped one again
### time complexity: O(n), space complexity: O(1)
def next_perm(P):
    stop_idx = -1
    for i in reversed(range(len(P)-1)):
        if P[i] < P[len(P)-1]:
            stop_idx = i
            break

    if stop_idx is -1:
        return []
    elif len(P) - stop_idx is 2:
        P[stop_idx], P[len(P) - 1] = P[len(P) - 1], P[stop_idx]
        return P
    else:
        P[stop_idx], P[stop_idx + 1], P[len(P) - 1] = P[len(P) - 1], P[stop_idx], P[stop_idx + 1]
        return P


### a function to return k-th permutation
### a brute-force approach that employs next_perm() k times
### time complexity: O(kn), space compexity: O(1)
def k_th_permut(P, k):
    for i in range(k-1):
        P = next_perm(P)

    return P


start()
