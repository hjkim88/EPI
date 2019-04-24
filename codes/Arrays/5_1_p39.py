###
#   File name  : 5_1_p39.py
#   Author     : Hyunjin Kim
#   Date       : Apr 20, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : Write a program that takes an array A and an index i into A,
#                and rearranges the elements such that all elements less than
#                A[i](the "pivot") appear first, followed by elements equal to
#                the pivot, followed by elements greater than the pivot.
#   Example    : A = <0, 1, 2, 0, 2, 1, 1> and pivot index = 3,
#                a valid partitioning = <0, 0, 1, 2, 2, 1, 1>
#                if pivot index = 2, then <0, 1, 0, 1, 1, 2, 2>
#
#   Instruction
#               1. import 5_1_p39
#               2. Run the function 5_1_p39.start()
#               3. The results will be generated in the console
###

### import modules
import timeit

### a function starting this script
def start():
    print("5_1_p39.py")

    ### print the parity of the examples
    start_time = timeit.default_timer()
    print("rearrange([3, 2, 1, 3, 2, 3, 1, 1, 3], 4): ", rearrange([3, 2, 1, 3, 2, 3, 1, 1, 3], 4))
    print("rearrange([4, 1, 3, 7, 3, 2, 7, 4, 3], 1): ", rearrange([4, 1, 3, 7, 3, 2, 7, 4, 3], 1))
    print("rearrange([8, 5, 7, 2, 4, 4, 4, 7, 1], 7): ", rearrange([8, 5, 7, 2, 4, 4, 4, 7, 1], 7))
    print("rearrange([6, 6, 2, 7, 5, 3, 6, 1, 2], 5): ", rearrange([6, 6, 2, 7, 5, 3, 6, 1, 2], 5))
    print("rearrange([1, 9, 4, 0, 3, 5, 8, 3, 8], 0): ", rearrange([1, 9, 4, 0, 3, 5, 8, 3, 8], 0))
    print("rearrange([6, 4, 2, 7, 4, 4, 1, 6, 7], 8): ", rearrange([6, 4, 2, 7, 4, 4, 1, 6, 7], 8))
    print("Execution Time: ", timeit.default_timer() - start_time)


### a function of Dutch flag problem
### from the start, compare the start and the pivot
### if the start > pivot, swap it with the end value and endIdx--
### if the start < pivot, then startIdx++
### if the start == pivot, swap it with the value at (i+1), and i = i++
### repeat this until startIdx == endIdx
def rearrange(A, i):
    startIdx, endIdx = 0, len(A)-1

    while startIdx < endIdx:
        if(A[startIdx] > A[i]):
            temp = A[startIdx]
            A[startIdx] = A[endIdx]
            A[endIdx] = temp
            endIdx -= 1
        elif(A[startIdx] < A[i]):
            startIdx += 1
        else:
            A[startIdx] = A[i+1]
            A[i+1] = A[i]
            i += 1

    return A


start()
