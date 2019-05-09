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

    start_time = timeit.default_timer()
    print("rearrange([3, 2, 1, 3, 2, 3, 1, 1, 3], 4): ", rearrange([3, 2, 1, 3, 2, 3, 1, 1, 3], 4))
    print("rearrange([4, 1, 3, 7, 3, 2, 7, 4, 3], 1): ", rearrange([4, 1, 3, 7, 3, 2, 7, 4, 3], 1))
    print("rearrange([8, 5, 7, 2, 4, 4, 4, 7, 1], 7): ", rearrange([8, 5, 7, 2, 4, 4, 4, 7, 1], 7))
    print("rearrange([6, 6, 2, 7, 5, 3, 6, 1, 2], 5): ", rearrange([6, 6, 2, 7, 5, 3, 6, 1, 2], 5))
    print("rearrange([1, 9, 4, 0, 3, 5, 8, 3, 8], 0): ", rearrange([1, 9, 4, 0, 3, 5, 8, 3, 8], 0))
    print("rearrange([6, 4, 2, 7, 4, 4, 1, 6, 7], 8): ", rearrange([6, 4, 2, 7, 4, 4, 1, 6, 7], 8))
    print("Execution Time: ", timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    print("dutch_flag_partition([3, 2, 1, 3, 2, 3, 1, 1, 3], 4): ", dutch_flag_partition([3, 2, 1, 3, 2, 3, 1, 1, 3], 4))
    print("dutch_flag_partition([4, 1, 3, 7, 3, 2, 7, 4, 3], 1): ", dutch_flag_partition([4, 1, 3, 7, 3, 2, 7, 4, 3], 1))
    print("dutch_flag_partition([8, 5, 7, 2, 4, 4, 4, 7, 1], 7): ", dutch_flag_partition([8, 5, 7, 2, 4, 4, 4, 7, 1], 7))
    print("dutch_flag_partition([6, 6, 2, 7, 5, 3, 6, 1, 2], 5): ", dutch_flag_partition([6, 6, 2, 7, 5, 3, 6, 1, 2], 5))
    print("dutch_flag_partition([1, 9, 4, 0, 3, 5, 8, 3, 8], 0): ", dutch_flag_partition([1, 9, 4, 0, 3, 5, 8, 3, 8], 0))
    print("dutch_flag_partition([6, 4, 2, 7, 4, 4, 1, 6, 7], 8): ", dutch_flag_partition([6, 4, 2, 7, 4, 4, 1, 6, 7], 8))
    print("Execution Time: ", timeit.default_timer() - start_time)


### a function of Dutch flag problem
### from the start, compare the start and the pivot
### if the start > pivot, swap it with the end value and endIdx--
### if the start < pivot, then startIdx++
### if the start == pivot, swap it with the value at (i+1), and i = i++
### repeat this until startIdx == endIdx
def rearrange(A, i):
    start_idx, end_idx = 0, len(A)-1

    while end_idx - start_idx > 1:
        if A[start_idx] > A[i]:
            A[start_idx], A[end_idx] = A[end_idx], A[start_idx]
            end_idx -= 1
        elif A[start_idx] < A[i]:
            start_idx += 1
        else:
            A[start_idx], A[end_idx] = A[end_idx], A[start_idx]

    return A

### the function introduced in the book
RED, WHITE, BLUE = range(3)
def dutch_flag_partition(A, pivot_index):
    pivot = A[pivot_index]
    # First pass: group elements smaller than pivot
    for i in range(len(A)):
        # Look for a smaller element
        for j in range(i+1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                break
    # Scond pass: group elements larger than pivot
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        # Look for a larger element. Stop when we reach an element less than
        # pivot, since first pass has moved them to the start of A
        for j in reversed(range(i)):
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                break
    return A


start()
