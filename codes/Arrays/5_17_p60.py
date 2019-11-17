###
#   File name  : 5_17_p60.py
#   Author     : Hyunjin Kim
#   Date       : Nov 17, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : Check whether a 9 x 9 2D array representing a partially completed Sudoku is valid.
#                Specifically, check that no row, column, or 3 x 3 2D sub-array contains duplicates.
#                A 0 value in the 2D array indicates that entry is blank; every other entry is in [1,9].
#
#   Input      : arr = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
#                       [6, 0, 0, 1, 9, 5, 0, 0, 0],
#                       [0, 9, 8, 0, 0, 0, 0, 6, 0],
#                       [8, 0, 0, 0, 6, 0, 0, 0, 3],
#                       [4, 0, 0, 8, 0, 3, 0, 0, 1],
#                       [7, 0, 0, 0, 2, 0, 0, 0, 6],
#                       [0, 6, 0, 0, 0, 0, 2, 8, 0],
#                       [0, 0, 0, 4, 1, 9, 0, 0, 5],
#                       [0, 0, 0, 0, 8, 0, 0, 7, 9]]
#
#   Instruction
#               1. import 5_17_p60.py
#               2. Run the function 5_17_p60.start()
#               3. The results will be generated in the console
###

### import modules
import timeit
import math

### a function starting this script
def start():
    print("5_17_p60.py")

    arr = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
           [6, 0, 0, 1, 9, 5, 0, 0, 0],
           [0, 9, 8, 0, 0, 0, 0, 6, 0],
           [8, 0, 0, 0, 6, 0, 0, 0, 3],
           [4, 0, 0, 8, 0, 3, 0, 0, 1],
           [7, 0, 0, 0, 2, 0, 0, 0, 6],
           [0, 6, 0, 0, 0, 0, 2, 8, 0],
           [0, 0, 0, 4, 1, 9, 0, 0, 5],
           [0, 0, 0, 0, 8, 0, 0, 7, 9]]

    start_time = timeit.default_timer()
    print("checkSudoku(arr) = ", checkSudoku(arr))
    print("Execution Time: ", timeit.default_timer() - start_time)


### check whether there are duplicates in a given array
### time complexity: O(n^2)
### space complexity: O(1)
def checkDups(a):
    r = False
    for x in range(len(a)-1):
        if a[x] != 0:
            for y in range(x+1, len(a)):
                if a[x] == a[y]:
                  r = True
                  break

    return r


### check validity of a Sudoku
### time complexity: O(n^3)
### space complexity: O(1)
def checkSudoku(A):
    r = True
    for i in range(len(A)):
        if checkDups(A[i]):
            r = False
            break
        if checkDups([A[x][i] for x in range(len(A[0]))]):
            r = False
            break

    n = int(math.sqrt(len(A)))

    for i in range(n):
        for j in range(n):
            if checkDups([A[x][y] for x in range(i*n, (i+1)*n) for y in range(j*n, (j+1)*n)]):
                r = False
                break

    return r


start()
