###
#   File name  : 5_7_p47.py
#   Author     : Hyunjin Kim
#   Date       : May 29, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : Write a program that computes the maximum profit that can be made by buying and selling
#                a share at most twice. The second buy must be made on another date after the first sale.
#
#   Example    : input: [200, 500, 100, 200, 400, 300, 200, 150, 350, 300, 500] -> output: 700
#                input: [150, 100, 550, 450, 300, 600] -> output: 750
#                input: [200, 100, 200, 300, 300, 800] -> output: 700
#                input: [100, 100, 100, 100, 100, 100] -> output: 0
#                input: [300, 200, 100, 400, 500, 600] -> output: 500
#
#   Instruction
#               1. import 5_7_p47.py
#               2. Run the function 5_7_p47.start()
#               3. The results will be generated in the console
###

### import modules
import timeit

### a function starting this script
def start():
    print("5_7_p47.py")

    start_time = timeit.default_timer()
    print("maximum_profit_twice([200, 500, 100, 200, 400, 300, 200, 150, 350, 300, 500]) = ", maximum_profit_twice([200, 500, 100, 200, 400, 300, 200, 150, 350, 300, 500]))
    print("maximum_profit_twice([150, 100, 550, 450, 300, 600]) = ", maximum_profit_twice([150, 100, 550, 450, 300, 600]))
    print("maximum_profit_twice([200, 100, 200, 300, 300, 800]) = ", maximum_profit_twice([200, 100, 200, 300, 300, 800]))
    print("maximum_profit_twice([100, 100, 100, 100, 100, 100]) = ", maximum_profit_twice([100, 100, 100, 100, 100, 100]))
    print("maximum_profit_twice([300, 200, 100, 400, 500, 600]) = ", maximum_profit_twice([300, 200, 100, 400, 500, 600]))
    print("Execution Time: ", timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    print("maximum_profit_twice2([200, 500, 100, 200, 400, 300, 200, 150, 350, 300, 500]) = ", maximum_profit_twice2([200, 500, 100, 200, 400, 300, 200, 150, 350, 300, 500]))
    print("maximum_profit_twice2([150, 100, 550, 450, 300, 600]) = ", maximum_profit_twice2([150, 100, 550, 450, 300, 600]))
    print("maximum_profit_twice2([200, 100, 200, 300, 300, 800]) = ", maximum_profit_twice2([200, 100, 200, 300, 300, 800]))
    print("maximum_profit_twice2([100, 100, 100, 100, 100, 100]) = ", maximum_profit_twice2([100, 100, 100, 100, 100, 100]))
    print("maximum_profit_twice2([300, 200, 100, 400, 500, 600]) = ", maximum_profit_twice2([300, 200, 100, 400, 500, 600]))
    print("Execution Time: ", timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    print("maximum_profit_twice3([200, 500, 100, 200, 400, 300, 200, 150, 350, 300, 500]) = ", maximum_profit_twice3([200, 500, 100, 200, 400, 300, 200, 150, 350, 300, 500]))
    print("maximum_profit_twice3([150, 100, 550, 450, 300, 600]) = ", maximum_profit_twice3([150, 100, 550, 450, 300, 600]))
    print("maximum_profit_twice3([200, 100, 200, 300, 300, 800]) = ", maximum_profit_twice3([200, 100, 200, 300, 300, 800]))
    print("maximum_profit_twice3([100, 100, 100, 100, 100, 100]) = ", maximum_profit_twice3([100, 100, 100, 100, 100, 100]))
    print("maximum_profit_twice3([300, 200, 100, 400, 500, 600]) = ", maximum_profit_twice3([300, 200, 100, 400, 500, 600]))
    print("Execution Time: ", timeit.default_timer() - start_time)


### a function to return the maximum profit (buy & sell at most twice)
### a brute-force approach would be for every item i (0:len(A)), regard that i is the separation between the first
### buy-sell period and the second buy-sell period. And get the maximum profit.
### time complexity: O(n^2)
def maximum_profit_once(A):
    min_value = A[0]
    max_profit = 0
    for i in range(1, len(A)):
        max_profit = max(max_profit, (A[i]-min_value))
        min_value = min(min_value, A[i])

    return max_profit

def maximum_profit_twice(A):
    max_profit = maximum_profit_once(A)
    for i in range(2, len(A)-1):
        max_profit = max(max_profit, (maximum_profit_once(A[i:]) + maximum_profit_once(A[:i])))

    return max_profit


### HINT: what do you need to know about the first i elements when processing the (i+1)th element?

### do it in O(n) time complexity
### space complexity: O(n)
def maximum_profit_twice2(A):
    min_value = A[0]
    max_profit1 = [0] * len(A)
    for i in range(1, len(A)):
        max_profit1[i] = max(max_profit1[i-1], A[i] - min_value)
        min_value = min(min_value, A[i])

    max_value = A[len(A)-1]
    max_profit2 = [0] * len(A)
    for i in reversed(range(len(A)-1)):
        max_profit2[i] = max(max_profit2[i+1], max_value - A[i])
        max_value = max(max_value, A[i])

    max_profit = 0
    for i in range(len(A)):
        max_profit = max(max_profit, max_profit1[i] + max_profit2[i])

    return max_profit


### do it in O(n) time complexity and O(1) space complexity
### get hint from online solution
### for every A[i] determine which is bigger: the max_profit_twice so far VS the max_profit_once + A[i] - second_min
### because the max_profit_once + new profit can be bigger than the previous one
### determining the second_min is important
### it should appear after the first_min, and the smallest after the first_min
### if new max_profit_once appeared, it should start from the A[i]
### if new first_min is set, then probably, the max_profit_once will be reset and this will also affect the second_min
### because second_min will be also set as the A[i] that makes the max_profit_once,
### and then it will find the second_min from that value
def maximum_profit_twice3(A):
    min_value = A[0]
    max_profit_once = 0
    second_min = A[0]
    max_profit_overall = 0

    for i in range(1, len(A)):
        max_profit_overall = max(max_profit_overall, max_profit_once + A[i] - second_min)
        if max_profit_once < A[i] - min_value:
            max_profit_once = A[i] - min_value
            second_min = A[i]
        else:
            second_min = min(second_min, A[i])

        min_value = min(min_value, A[i])

    return max_profit_overall


start()
