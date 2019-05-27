###
#   File name  : 5_5_p45.py
#   Author     : Hyunjin Kim
#   Date       : May 26, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : Write a program which takes as input a sorted array and updates it so that all duplicates
#                have been removed and the remaining elements have been shifted left to fill the emptied
#                indices. Return the number of valid elements. Many languages have library functions for
#                performing this operation - you cannot use these functions.
#
#   Example    : For the array [2, 3, 5, 5, 7, 11, 11, 11, 13], then after deletion,
# #              the array is [2, 3, 5, 7, 11, 13, 0, 0, 0].
#
#   Instruction
#               1. import 5_5_p45.py
#               2. Run the function 5_5_p45.start()
#               3. The results will be generated in the console
###

### import modules
import timeit

### a function starting this script
def start():
    print("5_5_p45.py")

    start_time = timeit.default_timer()
    print("delete_duplicates([2, 3, 5, 5, 7, 11, 11, 11, 13]) = ", delete_duplicates([2, 3, 5, 5, 7, 11, 11, 11, 13]))
    print("delete_duplicates([3, 3, 5, 5, 5, 6, 7, 7, 8]) = ", delete_duplicates([3, 3, 5, 5, 5, 6, 7, 7, 8]))
    print("delete_duplicates([1, 1, 1, 1, 1]) = ", delete_duplicates([1, 1, 1, 1, 1]))
    print("delete_duplicates([2, 23, 56, 78, 78]) = ", delete_duplicates([2, 23, 56, 78, 78]))
    print("delete_duplicates([4, 4, 5, 6, 6, 7, 8, 8, 9, 9, 9, 9]) = ", delete_duplicates([4, 4, 5, 6, 6, 7, 8, 8, 9, 9, 9, 9]))
    print("Execution Time: ", timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    print("delete_duplicates2([2, 3, 5, 5, 7, 11, 11, 11, 13]) = ", delete_duplicates2([2, 3, 5, 5, 7, 11, 11, 11, 13]))
    print("delete_duplicates2([3, 3, 5, 5, 5, 6, 7, 7, 8]) = ", delete_duplicates2([3, 3, 5, 5, 5, 6, 7, 7, 8]))
    print("delete_duplicates2([1, 1, 1, 1, 1]) = ", delete_duplicates2([1, 1, 1, 1, 1]))
    print("delete_duplicates2([2, 23, 56, 78, 78]) = ", delete_duplicates2([2, 23, 56, 78, 78]))
    print("delete_duplicates2([4, 4, 5, 6, 6, 7, 8, 8, 9, 9, 9, 9]) = ", delete_duplicates2([4, 4, 5, 6, 6, 7, 8, 8, 9, 9, 9, 9]))
    print("Execution Time: ", timeit.default_timer() - start_time)


### a function to delete duplicates in an array
### a brute-force approach would be checking sequencially
### since it uses remove(), the time complexity is O(n^2)
def delete_duplicates(A):
    i = 0
    j = len(A)-1
    while i < j:
        if A[i] is A[i+1]:
            A.remove(A[i])
            A.insert(len(A), 0)
            j -= 1
        else:
            i += 1

    return A


### a function to delete duplicates in an array
### without using remove()
### time complexity should be O(n) and space complexity should be O(1)
def delete_duplicates2(A):
    write_idx = 1
    for i in range(1,len(A)):
        if A[i] is not A[i-1]:
            A[write_idx] = A[i]
            write_idx += 1

    A[write_idx:] = [0] * (len(A)-write_idx)

    return A


start()
