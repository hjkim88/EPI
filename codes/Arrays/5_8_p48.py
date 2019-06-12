###
#   File name  : 5_8_p48.py
#   Author     : Hyunjin Kim
#   Date       : Jun 11, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : Write a program that takes an array A of n numbers, and rearranges A's elements to get a new array
#                B having the property that B[0] <= B[1] >= B[2] <= B[3] >= B[4] <= B[5] >= ...
#
#   Example    : input: [3, 4, 1, 54, 32, 42, 7, 5, 43] -> output: [3, 4, 1, 54, 32, 42, 5, 43, 7]
#                input: [34, 2, 54, 64, 23, 43, 25, 5] -> output: [2, 54, 32, 64, 23, 43, 5, 25]
#                input: [100, 43, 2, 53, 64, 54, 34, 6] -> output: [34, 100, 6, 53, 2, 64, 43, 54]
#                input: [53, 6, 34, 23, 64, 34, 64, 34] -> output: [6, 53, 34, 64, 23, 34, 34, 63]
#                input: [5, 5, 5, 5, 5, 5, 5, 5, 5, 5] -> output: [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
#
#   Instruction
#               1. import 5_8_p48.py
#               2. Run the function 5_8_p48.start()
#               3. The results will be generated in the console
###

### import modules
import timeit

### a function starting this script
def start():
    print("5_8_p48.py")

    start_time = timeit.default_timer()
    print("fluctuation([3, 4, 1, 54, 32, 42, 7, 5, 43]) = ", fluctuation([3, 4, 1, 54, 32, 42, 7, 5, 43]))
    print("fluctuation([34, 2, 54, 64, 23, 43, 25, 5]) = ", fluctuation([34, 2, 54, 64, 23, 43, 25, 5]))
    print("fluctuation([100, 43, 2, 53, 64, 54, 34, 6]) = ", fluctuation([100, 43, 2, 53, 64, 54, 34, 6]))
    print("fluctuation([53, 6, 34, 23, 64, 34, 64, 34]) = ", fluctuation([53, 6, 34, 23, 64, 34, 64, 34]))
    print("fluctuation([5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) = ", fluctuation([5, 5, 5, 5, 5, 5, 5, 5, 5, 5]))
    print("Execution Time: ", timeit.default_timer() - start_time)


### a bruce-force approach would be iteratively find bigger/smaller number than the previous one
### time complexity: O(n^2), space complexity: O(1)

### a more efficient one is to swap consecutive values sequentially
### time complexity: O(n), space complexity: O(1)
### only two for loops are needed
### for example, [5, 3, 6, 8], we do it with indicies of 0 and 2
### [5, 3, 6, 8] -> [3, 5, 6, 8]
### then we check indicies of 1 and 3,
### [3, 5, 6, 8] -> [3, 6, 5, 8]
### here, only two for loops are OK because we already know 3 < 5 and 6 < 8
### and if 5 < 6, then 6 is already bigger than 3, since "3 < 5" is already ordered in the first step loop
### likewise, 5 < 8 because we already know 5 < 6 < 8 and the "6 < 8" is already ordrered in the first step loop
def fluctuation(A):
    for i in range(0, len(A)-1, 2):
        if A[i] > A[i+1]:
            A[i], A[i+1] = A[i+1], A[i]
    for i in range(1, len(A)-1, 2):
        if A[i] < A[i+1]:
            A[i], A[i + 1] = A[i + 1], A[i]

    return A


start()
