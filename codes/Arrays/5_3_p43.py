###
#   File name  : 5_3_p43.py
#   Author     : Hyunjin Kim
#   Date       : May 13, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : Write a program that takes two arrays representing integers, and returns an integer
#                representing their product.
#   Example    : 193707721 x -761838257287 = -147573952589676412927. The inputs should be all in arrays.
#
#   Instruction
#               1. import 5_3_p43.py
#               2. Run the function 5_3_p43.start()
#               3. The results will be generated in the console
###

### import modules
import timeit

### a function starting this script
def start():
    print("5_3_p43.py")

    start_time = timeit.default_timer()
    print("array_product1([3, 2, 4, 3, 2], [7, 5, 4]) = ", array_product1([3, 2, 4, 3, 2], [7, 5, 4]))
    print("array_product1(['-', 6, 3, 8], [3, 4, 9]) = ", array_product1(['-', 6, 3, 8], [3, 4, 9]))
    print("array_product1([4, 3, 6, 3, 5, 1, 7], ['-', 3, 1, 3]) = ", array_product1([4, 3, 6, 3, 5, 1, 7], ['-', 3, 1, 3]))
    print("array_product1(['-', 3, 1, 5], ['-', 7, 7, 5, 3]) = ", array_product1(['-', 3, 1, 5], ['-', 7, 7, 5, 3]))
    print("array_product1([5, 6, 2, 3, 0], [5, 0, 1, 4]) = ", array_product1([5, 6, 2, 3, 0], [5, 0, 1, 4]))
    print("Execution Time: ", timeit.default_timer() - start_time)


### a function to return numeric value from the input array
def getNumeric(arr):
    minus = False
    if arr[0] is '-':
        minus = True
        arr.remove('-')

    result = 0
    for i in range(len(arr)):
        result += arr[i] * (10 **(len(arr)-i-1))

    if minus:
        return -result
    else:
        return result


### a function to multiply two arrays
### a brute-force approach would be convert them to numeric value
### get multiplied value and return it as an array
def array_product1(x, y):
    x = getNumeric(x)
    y = getNumeric(y)

    return x * y


### here, the product is calculated bit-by-bit from the LSB
def array_product2(x, y):
    minus = False
    if x[0] is '-':
        minus = not minus
        x.remove('-')
    if y[0] is '-':
        minus = not minus
        y.remove('-')

    result = 0
    for i in reversed(range(len(x))):
        for j in reversed(range(len(y))):
            result += x[i] * y[j]
            



    return 0


start()
