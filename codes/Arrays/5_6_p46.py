###
#   File name  : 5_6_p46.py
#   Author     : Hyunjin Kim
#   Date       : May 28, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : Write a program that takes an array denoting the daily stock price, and returns the maximum
#                profit that could be made by buying and then selling one share of that stock.
#
#   Example    : input: [310, 315, 275, 295, 260, 270, 290, 230, 255, 250] -> output: 30
#
#   Instruction
#               1. import 5_6_p46.py
#               2. Run the function 5_6_p46.start()
#               3. The results will be generated in the console
###

### import modules
import timeit

### a function starting this script
def start():
    print("5_6_p46.py")

    start_time = timeit.default_timer()
    print("maximum_profit([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]) = ", maximum_profit([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))
    print("maximum_profit([3, 2, 5, 1, 2, 3, 1, 4, 5, 6, 2, 3]) = ", maximum_profit([3, 2, 5, 1, 2, 3, 1, 4, 5, 6, 2, 3]))
    print("maximum_profit([100, 200, 300, 400, 500]) = ", maximum_profit([100, 200, 300, 400, 500]))
    print("maximum_profit([500, 400, 300, 200, 100]) = ", maximum_profit([500, 400, 300, 200, 100]))
    print("maximum_profit([100, 100, 100, 100, 100]) = ", maximum_profit([100, 100, 100, 100, 100]))
    print("maximum_profit([450, 200, 480, 235, 200, 695, 390, 560, 240, 585]) = ", maximum_profit([450, 200, 480, 235, 200, 695, 390, 560, 240, 585]))
    print("Execution Time: ", timeit.default_timer() - start_time)


### a function to return the highest profit in the given stock array
### one pass - get min values and take the highest current value - min
def maximum_profit(A):
    min_value = A[0]
    profit = 0
    for i in range(1, len(A)):
        profit = max(profit, A[i]-min_value)
        min_value = min(min_value, A[i])

    return profit


start()
