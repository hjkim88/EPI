###
#   File name  : 5_1_p39.py
#   Author     : Hyunjin Kim
#   Date       : Apr 20, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : Write a program that takes an array A and an index i into A,
#                and rearranges the elements such that all elements less than
#                A[i](the "pivot") appear first, followed by elements equal to
#                the pivot, followed by elements greater than the pivot.
#                The space complexity should be O(1).
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
    print("dutch_flag_partition1([3, 2, 1, 3, 2, 3, 1, 1, 3], 4): ", dutch_flag_partition1([3, 2, 1, 3, 2, 3, 1, 1, 3], 4))
    print("dutch_flag_partition1([4, 1, 3, 7, 3, 2, 7, 4, 3], 1): ", dutch_flag_partition1([4, 1, 3, 7, 3, 2, 7, 4, 3], 1))
    print("dutch_flag_partition1([8, 5, 7, 2, 4, 4, 4, 7, 1], 7): ", dutch_flag_partition1([8, 5, 7, 2, 4, 4, 4, 7, 1], 7))
    print("dutch_flag_partition1([6, 6, 2, 7, 5, 3, 6, 1, 2], 5): ", dutch_flag_partition1([6, 6, 2, 7, 5, 3, 6, 1, 2], 5))
    print("dutch_flag_partition1([1, 9, 4, 0, 3, 5, 8, 3, 8], 0): ", dutch_flag_partition1([1, 9, 4, 0, 3, 5, 8, 3, 8], 0))
    print("dutch_flag_partition1([6, 4, 2, 7, 4, 4, 1, 6, 7], 8): ", dutch_flag_partition1([6, 4, 2, 7, 4, 4, 1, 6, 7], 8))
    print("Execution Time: ", timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    print("dutch_flag_partition2([3, 2, 1, 3, 2, 3, 1, 1, 3], 4): ", dutch_flag_partition2([3, 2, 1, 3, 2, 3, 1, 1, 3], 4))
    print("dutch_flag_partition2([4, 1, 3, 7, 3, 2, 7, 4, 3], 1): ", dutch_flag_partition2([4, 1, 3, 7, 3, 2, 7, 4, 3], 1))
    print("dutch_flag_partition2([8, 5, 7, 2, 4, 4, 4, 7, 1], 7): ", dutch_flag_partition2([8, 5, 7, 2, 4, 4, 4, 7, 1], 7))
    print("dutch_flag_partition2([6, 6, 2, 7, 5, 3, 6, 1, 2], 5): ", dutch_flag_partition2([6, 6, 2, 7, 5, 3, 6, 1, 2], 5))
    print("dutch_flag_partition2([1, 9, 4, 0, 3, 5, 8, 3, 8], 0): ", dutch_flag_partition2([1, 9, 4, 0, 3, 5, 8, 3, 8], 0))
    print("dutch_flag_partition2([6, 4, 2, 7, 4, 4, 1, 6, 7], 8): ", dutch_flag_partition2([6, 4, 2, 7, 4, 4, 1, 6, 7], 8))
    print("Execution Time: ", timeit.default_timer() - start_time)


### a function of Dutch flag problem
### space complexity: O(1), time complexity: O(n)
### same as the third function in the book
def rearrange(A, pivot_index):
    pivot, start_idx, end_idx, current_idx = A[pivot_index], 0, len(A)-1, 0

    while current_idx < end_idx:
        if A[current_idx] < pivot:
            A[start_idx], A[current_idx] = A[current_idx], A[start_idx]
            start_idx += 1
            current_idx += 1
        elif A[current_idx] > pivot:
            A[end_idx], A[current_idx] = A[current_idx], A[end_idx]
            end_idx -= 1
        else:
            current_idx += 1

    return A


### the first function introduced in the book
### Space complexity: O(1), time complexity: O(n**2)
def dutch_flag_partition1(A, pivot_index):
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


### the second function introduced in the book
### Space complexity: O(1), time complexity: O(n)
def dutch_flag_partition2(A, pivot_index):
    pivot = A[pivot_index]
    # First pass: group elements smaller than pivot
    small_idx = 0
    for i in range(len(A)):
        if A[i] < A[pivot_index]:
            A[small_idx], A[i] = A[i], A[small_idx]
            small_idx += 1

    # Scond pass: group elements larger than pivot
    large_idx = len(A)-1
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break

        if A[i] > pivot:
            A[large_idx], A[i] = A[i], A[large_idx]
            large_idx -= 1

    return A


start()
