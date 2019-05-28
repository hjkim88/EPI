###
#   File name  : 5_5_variant.py
#   Author     : Hyunjin Kim
#   Date       : May 27, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : 1. Implement a function which takes as input an array and a key, and updates the array
#                so that all occurrences of the input key have been removed and the remaining elements have been
#                shifted left to fill the emptied indices. Return the number of remaining elements. There are no
#                requirements as to the values stored beyond the last valid element.
#                2. Write a program which takes as input a sorted array A of integers and a positive integer m,
#                and updates A so that if x appears m times in A it appears exactly min(2,m) times in A.
#                The update to A should be performed in one pass, and no additional storage may be allocated.
#
#   Background : This is related to the "5_5_p45.py".
#
#   Instruction
#               1. import 5_5_variant
#               2. Run the function 5_5_variant.start()
#               3. The results will be generated in the console
###

### import modules
import timeit

### a function starting this script
def start():
    print("5_5_variant.py")

    start_time = timeit.default_timer()
    print("fun_one([4, 1, 3, 4, 6, 3, 4, 5, 1], 4) = ", fun_one([4, 1, 3, 4, 6, 3, 4, 5, 1], 4))
    print("fun_one([7, 4, 5, 4, 7, 2, 3, 4, 5], 1) = ", fun_one([7, 4, 5, 4, 7, 2, 3, 4, 5], 1))
    print("fun_one([5, 5, 5, 5, 5], 5) = ", fun_one([5, 5, 5, 5, 5], 5))
    print("fun_one([8, 2, 4, 3, 2, 4, 5, 2, 1, 4, 6, 3, 3], 2) = ", fun_one([8, 2, 4, 3, 2, 4, 5, 2, 1, 4, 6, 3, 3], 2))
    print("fun_one([8, 2, 5, 9, 3, 1, 7, 4, 3, 8, 5], 5) = ", fun_one([8, 2, 5, 9, 3, 1, 7, 4, 3, 8, 5], 5))
    print("Execution Time: ", timeit.default_timer() - start_time)


### a function to remove the given key in the given array and returns the remainings
def fun_one(A, k):
    write_idx = 0
    for i in range(len(A)):
        if A[i] is not k:
            A[write_idx] = A[i]
            write_idx += 1

    for i in range(write_idx, len(A)):
        A[i] = 0

    return A


### the second function described above
def fun_two(A, m):
    if m <= 2:
        return A
    else:
        i = 1
        while i < len(A):
            if A[i] is A[i-1]:
                A[i]
                

        return A


start()
