###
#   File name  : 5_6_variant.py
#   Author     : Hyunjin Kim
#   Date       : May 28, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : 1. Write a program that takes an array of integers and finds the length of a longest subarray
#                all of whose entries are equal.
#
#   Background : This is related to the "5_6_p46.py".
#
#   Instruction
#               1. import 5_6_variant
#               2. Run the function 5_6_variant.start()
#               3. The results will be generated in the console
###

### import modules
import timeit

### a function starting this script
def start():
    print("5_6_variant.py")

    start_time = timeit.default_timer()
    print("fun_one([4, 2, 2, 2, 1, 1, 3, 4, 5, 2, 3, 4]) = ", fun_one([4, 2, 2, 2, 1, 1, 3, 4, 5, 2, 3, 4]))
    print("fun_one([3, 3, 3, 4, 4, 4, 4, 1, 2, 3]) = ", fun_one([3, 3, 3, 4, 4, 4, 4, 1, 2, 3]))
    print("fun_one([1, 1, 1, 1, 1]) = ", fun_one([1, 1, 1, 1, 1]))
    print("fun_one([2, 2, 2, 2, 1, 3, 2, 3, 4, 8]) = ", fun_one([2, 2, 2, 2, 1, 3, 2, 3, 4, 8]))
    print("fun_one([1, 2, 3, 4, 5]) = ", fun_one([1, 2, 3, 4, 5]))
    print("Execution Time: ", timeit.default_timer() - start_time)


### the first one described above
def fun_one(A):
    dup_num = 1
    max_num = 1
    for i in range(1, len(A)):
        if A[i] is A[i-1]:
            dup_num += 1
        else:
            max_num = max(max_num, dup_num)
            dup_num = 1

    max_num = max(max_num, dup_num)

    return max_num


start()
