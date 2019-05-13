###
#   File name  : 5_1_variant.py
#   Author     : Hyunjin Kim
#   Date       : May 11, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : 1. Assuming that keys take one of three values, reorder the array
#                   so that all objects with the same key appear together.
#                   The ordr of the subarrays is not important. For example,
#                   both Figures 5.1(b) and 5.1(c) on Page 40 are valid answers for
#                   Figure 5.1(a) on Page 40. Use O(1) additional space and O(n) time.
#                2. Given an array A of n objects with keys that takes one of four values,
#                   reorder the array so that all objects that have the same key appear together.
#                   Use O(1) additional space and O(n) time.
#                3. Given an array A of n objects with Boolean-valued keys, reorder the array
#                   so that objects that have the key false appear first. Use O(1) additional
#                   space and O(n) time.
#                4. Given an array A of n objects with Boolean-valued keys, reorder the array
#                   so that objects that have the key false appear first. The relative ordering
#                   of objects with key true should not change. Use O(1) additional space
#                   and O(n) time.
#
#   Background : This is related to the "5_1_p39.py".
#
#   Instruction
#               1. import 5_1_variant
#               2. Run the function 5_1_variant.start()
#               3. The results will be generated in the console
###

### import modules
import timeit

### a function starting this script
def start():
    print("5_1_variant.py")

    start_time = timeit.default_timer()
    print("fun_one([0, 2, 1, 1, 0, 0, 1, 2, 0, 1] = )", fun_one([0, 2, 1, 1, 0, 0, 1, 2, 0, 1]))
    print("fun_one([1, 1, 0, 2, 0, 1, 0, 2, 1, 0] = )", fun_one([1, 1, 0, 2, 0, 1, 0, 2, 1, 0]))
    print("fun_one([2, 1, 1, 0, 0, 1, 0, 2, 0, 2] = )", fun_one([2, 1, 1, 0, 0, 1, 0, 2, 0, 2]))
    print("fun_one([0, 0, 0, 1, 0, 0, 2, 1, 2, 0] = )", fun_one([0, 0, 0, 1, 0, 0, 2, 1, 2, 0]))
    print("fun_one([1, 1, 0, 2, 0, 2, 0, 2, 1, 1] = )", fun_one([1, 1, 0, 2, 0, 2, 0, 2, 1, 1]))
    print("Execution Time: ", timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    print("fun_two([0, 2, 3, 1, 0, 3, 1, 2, 0, 1] = )", fun_two([0, 2, 3, 1, 0, 3, 1, 2, 0, 1]))
    print("fun_two([1, 3, 3, 2, 0, 1, 0, 2, 3, 0] = )", fun_two([1, 3, 3, 2, 0, 1, 0, 2, 3, 0]))
    print("fun_two([2, 1, 1, 0, 0, 1, 0, 2, 3, 3] = )", fun_two([2, 1, 1, 0, 0, 1, 0, 2, 3, 3]))
    print("fun_two([3, 0, 0, 1, 3, 0, 2, 1, 2, 3] = )", fun_two([3, 0, 0, 1, 3, 0, 2, 1, 2, 3]))
    print("fun_two([1, 3, 3, 3, 3, 2, 0, 2, 1, 1] = )", fun_two([1, 3, 3, 3, 3, 2, 0, 2, 1, 1]))
    print("Execution Time: ", timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    print("fun_three([False, False, True, False, False, True, True, False]) = ", fun_three([False, False, True, False, False, True, True, False]))
    print("fun_three([True, True, False, True, False, False, True, True]) = ", fun_three([True, True, False, True, False, False, True, True]))
    print("fun_three([True, False, False, True, False, True, False, True, False]) = ", fun_three([True, False, False, True, False, True, False, True, False]))
    print("fun_three([False, False, False, True, False, False, False, False]) = ", fun_three([False, False, False, True, False, False, False, False]))
    print("fun_three([True, False, False, False, True, False, True, False, True]) = ", fun_three([True, False, False, False, True, False, True, False, True]))
    print("Execution Time: ", timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    print("fun_three2([False, False, True, False, False, True, True, False]) = ", fun_three2([False, False, True, False, False, True, True, False]))
    print("fun_three2([True, True, False, True, False, False, True, True]) = ", fun_three2([True, True, False, True, False, False, True, True]))
    print("fun_three2([True, False, False, True, False, True, False, True, False]) = ", fun_three2([True, False, False, True, False, True, False, True, False]))
    print("fun_three2([False, False, False, True, False, False, False, False]) = ", fun_three2([False, False, False, True, False, False, False, False]))
    print("fun_three2([True, False, False, False, True, False, True, False, True]) = ", fun_three2([True, False, False, False, True, False, True, False, True]))
    print("Execution Time: ", timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    print("fun_four([False, False, True, False, False, True, True, False]) = ", fun_four([False, False, True, False, False, True, True, False]))
    print("fun_four([True, True, False, True, False, False, True, True]) = ", fun_four([True, True, False, True, False, False, True, True]))
    print("fun_four([True, False, False, True, False, True, False, True, False]) = ", fun_four([True, False, False, True, False, True, False, True, False]))
    print("fun_four([False, False, False, True, False, False, False, False]) = ", fun_four([False, False, False, True, False, False, False, False]))
    print("fun_four([True, False, False, False, True, False, True, False, True]) = ", fun_four([True, False, False, False, True, False, True, False, True]))
    print("Execution Time: ", timeit.default_timer() - start_time)


### a function for the first task
### suppose there are only 3 values, [0, 1, 2]
### set three indicies
### two indicies indicate two groups
### the third index indicates current position in a loop
### the third index starts from 0
### one index starts from 0 to len(A) the other starts from len(A)-1 to 0
### for one group, switch them all to the start
### for another one switch them all to the end
### for the last group, just count up the current index
### loop until the current position index meets the end index
x = [0, 1, 2]
def fun_one(A):
    start_idx, current_idx, end_idx = 0, 0, len(A)-1

    while current_idx <= end_idx:
        if A[current_idx] == x[0]:
            A[start_idx], A[current_idx] = A[current_idx], A[start_idx]
            start_idx += 1
            current_idx += 1
        elif A[current_idx] == x[1]:
            current_idx += 1
        else:
            A[end_idx], A[current_idx] = A[current_idx], A[end_idx]
            end_idx -= 1

    return A


### the fun_one should be done twice forward + backward
### in the forward pass, suppose there are only 3 groups - {0}, {1}, and {2,3}
### do not consider order in {2,3} - they will be ordered in the backward pass
### in the backward pass, suppose there are only 3 groups - {3}, {2}, {1,0}
### do not considr order in {1,0} - here they are already ordered in the forward pass
x = [0, 1, 2, 3]
def fun_two(A):
    start_idx, current_idx, end_idx = 0, 0, len(A)-1

    while current_idx <= end_idx:
        if A[current_idx] == x[0]:
            A[start_idx], A[current_idx] = A[current_idx], A[start_idx]
            start_idx += 1
            current_idx += 1
        elif A[current_idx] == x[1]:
            current_idx += 1
        else:
            A[end_idx], A[current_idx] = A[current_idx], A[end_idx]
            end_idx -= 1

    start_idx, current_idx = len(A)-1, len(A)-1

    while current_idx > end_idx:
        if A[current_idx] == x[3]:
            A[start_idx], A[current_idx] = A[current_idx], A[start_idx]
            start_idx -= 1
            current_idx -= 1
        elif A[current_idx] == x[2]:
            current_idx -= 1
        else:
            break

    return A


### a function to order a boolean array
### false - true
def fun_three(A):
    start_idx, end_idx = 0, len(A)-1

    while start_idx < end_idx:
        while not A[start_idx] and start_idx < end_idx:
            start_idx += 1
        while A[end_idx] and start_idx < end_idx:
            end_idx -= 1
        if start_idx < end_idx:
            A[start_idx], A[end_idx] = A[end_idx], A[start_idx]
            start_idx += 1
            end_idx -= 1

    return A


### a function to order a boolean array
### false - true
### it seems the above fun_three() is slow
### make a new one
def fun_three2(A):
    end_idx, i = len(A)-1, 0

    while i <= end_idx:
        if A[i]:
            A[i], A[end_idx] = A[end_idx], A[i]
            end_idx -= 1
        else:
            i += 1

    return A


### a function to order a boolean array
### false - true
### but relative order of true should not change
def fun_four(A):
    end_idx = len(A)-1

    for i in reversed(range(len(A))):
        if A[i]:
            A[i], A[end_idx] = A[end_idx], A[i]
            end_idx -= 1

    return A


start()
