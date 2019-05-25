###
#   File name  : 5_4_p44.py
#   Author     : Hyunjin Kim
#   Date       : May 25, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : Write a program which takes an array of n integers, where A[i] denotes the maximum you can
#                advance from index i, and returns whether it is possible to advance to the last index
#                starting from the beginning of the array.
#   Example    : if A = [3, 3, 1, 0, 2, 0, 1], return True
#                if A = [3, 2, 0, 0, 2, 0, 1], return False
#
#   Instruction
#               1. import 5_4_p44.py
#               2. Run the function 5_4_p44.start()
#               3. The results will be generated in the console
###

### import modules
import timeit

### a function starting this script
def start():
    print("5_4_p44.py")

    start_time = timeit.default_timer()
    print("isAdvancable([3, 3, 1, 0, 2, 0, 1]) = ", isAdvancable([3, 3, 1, 0, 2, 0, 1]))
    print("isAdvancable([3, 2, 0, 0, 2, 0, 1]) = ", isAdvancable([3, 2, 0, 0, 2, 0, 1]))
    print("isAdvancable([1, 1, 1, 1, 1, 1, 1]) = ", isAdvancable([1, 1, 1, 1, 1, 1, 1]))
    print("isAdvancable([0, 3, 1, 0, 2, 0, 1]) = ", isAdvancable([0, 3, 1, 0, 2, 0, 1]))
    print("isAdvancable([10, 3, 1, 0, 2, 0, 1]) = ", isAdvancable([10, 3, 1, 0, 2, 0, 1]))
    print("Execution Time: ", timeit.default_timer() - start_time)


### a function to tell whether the input array is advancable or not
### just one FOR loop. check every item until it reaches the end index or stuck in the middle
def isAdvancable(A):
    maxIdx = 0
    for i in range(len(A)):
        if i > maxIdx:
            break
        else:
            maxIdx = max(maxIdx, (i + A[i]))

    if maxIdx >= len(A):
        return True
    else:
        return False


start()
