###
#   File name  : 5_11_p52.py
#   Author     : Hyunjin Kim
#   Date       : Jun 19, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : Write a program that takes as input a permutation, and returns the next permutation
#                under dictionary ordering. If the permutation is the last permutation, return the empty array.
#
#   Example    : input: [1, 0, 3, 2], output: [1, 2, 0, 3]
#                input: [3, 2, 1, 0], output: []
#                input: [3, 1, 0, 2, 4], output: [3, 1, 0, 4, 2]
#                input: [2, 0, 1, 3, 4, 5], output: [2, 0, 1, 3, 5, 4]
#                input: [0, 4, 2, 1, 3, 7, 6, 5], output: [0, 4, 2, 1, 5, 3, 6, 7]
#                input: [1, 5, 4, 3, 2, 0], output: [2, 0, 1, 3, 4, 5]
#
#   Instruction
#               1. import 5_11_p52.py
#               2. Run the function 5_11_p52.start()
#               3. The results will be generated in the console
###

### import modules
import timeit

### a function starting this script
def start():
    print("5_11_p52.py")

    start_time = timeit.default_timer()
    print("next_perm([1, 0, 3, 2]) = ", next_perm([1, 0, 3, 2]))
    print("next_perm([3, 2, 1, 0]) = ", next_perm([3, 2, 1, 0]))
    print("next_perm([3, 1, 0, 2, 4]) = ", next_perm([3, 1, 0, 2, 4]))
    print("next_perm([2, 0, 1, 3, 4, 5]) = ", next_perm([2, 0, 1, 3, 4, 5]))
    print("next_perm([0, 4, 2, 1, 3, 7, 6, 5]) = ", next_perm([0, 4, 2, 1, 3, 7, 6, 5]))
    print("next_perm([1, 5, 4, 3, 2, 0]) = ", next_perm([1, 5, 4, 3, 2, 0]))
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


start()
