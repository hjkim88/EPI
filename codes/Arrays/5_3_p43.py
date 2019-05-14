###
#   File name  : 5_3_p43.py
#   Author     : Hyunjin Kim
#   Date       : May 13, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : Write a program that takes two arrays representing integers, and returns an integer
#                representing their product.
#   Example    : 193707721 x -761838257287 = -147573952589676412927. They should be all in arrays.
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
    print("")
    print("Execution Time: ", timeit.default_timer() - start_time)


### a function to multiply two arrays
### a brute-force approach would be convert them to numeric value
### get multiplied value and return it as an array
### here, the product is calculated bit-by-bit from the LSB
def array_product(x, y):
    minus = False
    if x[0] is '-':
        x_len = len(x)-1
        minus = not minus
    if y[0] is '-':
        y_len = len(y)-1
        minus = not minus




    return 0


start()
