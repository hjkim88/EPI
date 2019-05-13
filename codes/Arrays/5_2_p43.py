###
#   File name  : 5_2_p43.py
#   Author     : Hyunjin Kim
#   Date       : May 11, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : Write a program which takes as input an array of digits encoding a decimal integer D
#                and updates the array to represent the integer D+1. Your algorithm should work
#                even if it is implemented in a language that has finite-precision arithmetic.
#   Example    : If the input is [1, 2, 9] then you should update the array to [1, 3, 0].
#
#   Instruction
#               1. import 5_2_p43.py
#               2. Run the function 5_2_p43.start()
#               3. The results will be generated in the console
###

### import modules
import timeit

### a function starting this script
def start():
    print("5_2_p43.py")

    start_time = timeit.default_timer()
    print("plus_one([1, 2, 9]) = ", plus_one([1, 2, 9]))
    print("plus_one([4, 3, 2, 6, 4, 9, 9.00, 9]) = ", plus_one([4, 3, 2, 6, 4, 9, 9.00, 9]))
    print("plus_one([1, 5, 3, 2, 4, 5.0]) = ", plus_one([1, 5, 3, 2, 4, 5.0]))
    print("plus_one([9, 9, 9, 9, 9]) = ", plus_one([9, 9, 9, 9, 9]))
    print("plus_one([9, 3, 4, 2, 3]) = ", plus_one([9, 3, 4, 2, 3]))
    print("Execution Time: ", timeit.default_timer() - start_time)


### a function to return A+1, where the A indicates an input array that represents a integer
### a brute-force approach is start from the end index +1 there and if it excceds 9,
### propagate +1 to the left
### i think this is the fastest
def plus_one(A):
    for i in reversed(range(len(A))):
        if A[i] == 9:
            A[i] = 0
            if i == 0:
                A.insert(0, 1)
        else:
            A[i] = int(A[i]+1)
            break

    return A


start()
