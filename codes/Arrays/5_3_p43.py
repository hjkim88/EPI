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

    start_time = timeit.default_timer()
    print("array_product2([3, 2, 4, 3, 2], [7, 5, 4]) = ", array_product2([3, 2, 4, 3, 2], [7, 5, 4]))
    print("array_product2(['-', 6, 3, 8], [3, 4, 9]) = ", array_product2(['-', 6, 3, 8], [3, 4, 9]))
    print("array_product2([4, 3, 6, 3, 5, 1, 7], ['-', 3, 1, 3]) = ", array_product2([4, 3, 6, 3, 5, 1, 7], ['-', 3, 1, 3]))
    print("array_product2(['-', 3, 1, 5], ['-', 7, 7, 5, 3]) = ", array_product2(['-', 3, 1, 5], ['-', 7, 7, 5, 3]))
    print("array_product2([5, 6, 2, 3, 0], [5, 0, 1, 4]) = ", array_product2([5, 6, 2, 3, 0], [5, 0, 1, 4]))
    print("Execution Time: ", timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    print("multiply([3, 2, 4, 3, 2], [7, 5, 4]) = ", multiply([3, 2, 4, 3, 2], [7, 5, 4]))
    print("multiply([-6, 3, 8], [3, 4, 9]) = ", multiply([-6, 3, 8], [3, 4, 9]))
    print("multiply([4, 3, 6, 3, 5, 1, 7], [-3, 1, 3]) = ", multiply([4, 3, 6, 3, 5, 1, 7], [-3, 1, 3]))
    print("multiply([-3, 1, 5], [-7, 7, 5, 3]) = ", multiply([-3, 1, 5], [-7, 7, 5, 3]))
    print("multiply([5, 6, 2, 3, 0], [5, 0, 1, 4]) = ", multiply([5, 6, 2, 3, 0], [5, 0, 1, 4]))
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
            result += x[i] * (10 ** (len(x) - i - 1)) * y[j] * (10 ** (len(y) - j -1))

    if minus:
        return -result
    else:
        return result


### a function described in the book
def multiply(num1, num2):
    sign = -1 if(num1[0] < 0) ^ (num2[0] < 0) else 1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    result = [0] * (len(num1) + len(num2))
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i + j + 1] += num1[i] * num2[j]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10

    # Remove the leading zeros
    result = result[next((i for i, x in enumerate(result) if x != 0), len(result)):] or [0]

    return [sign * result[0]] + result[1:]


start()
