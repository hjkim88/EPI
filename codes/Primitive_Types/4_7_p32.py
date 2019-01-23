###
#   File name  : 4_7_p32.py
#   Author     : Hyunjin Kim
#   Date       : Jan 23, 2018
#   Email      : firadazer@gmail.com
#   Purpose    : Write a program that takes a double x and an integer y
#                and returns x**y. You can ignore overflow and underflow.
#   Example    : 2**3 = 8, 5**0 = 1, 23**2 = 529
#
#   Instruction
#               1. import 4_7_p32
#               2. Run the function 4_7_p32.start()
#               3. The results will be generated in the console
###

### import modules
import timeit


### a function starting this script
def start():
    print("4_7_p32.py")

    start_time = timeit.default_timer()
    print("exponentiation(2, 3) = ", exponentiation(2, 3))
    print("exponentiation(5, 0) = ", exponentiation(5, 0))
    print("exponentiation(23, 2) = ", exponentiation(23, 2))
    print("exponentiation(2.7, 4) = ", exponentiation(2.7, 4))
    print("exponentiation(10.1, 5) = ", exponentiation(10.1, 5))
    for i in range(10000):
        exponentiation(1.5, 30)
    print("Execution Time: ", timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    print("exponentiation2(2, 3) = ", exponentiation2(2, 3))
    print("exponentiation2(5, 0) = ", exponentiation2(5, 0))
    print("exponentiation2(23, 2) = ", exponentiation2(23, 2))
    print("exponentiation2(2.7, 4) = ", exponentiation2(2.7, 4))
    print("exponentiation2(10.1, 5) = ", exponentiation2(10.1, 5))
    for i in range(10000):
        exponentiation2(1.5, 30)
    print("Execution Time: ", timeit.default_timer() - start_time)


### a brute-force function to calculate x**y without using **
def exponentiation(x, y):
    result = x
    while(y > 1):
        result *= x
        y -= 1

    if(y == 0):
        result = 1

    return result


### a more efficient function than the brute-force one
### the exponent can be transfomed as binary number
### it is like binary search
### x**27 = x**16 + x**8 + x**2 + x**1
### here, x**16 = x**8 x x**8 = x**4 x x**4 x x**4 x x**4
def exponentiation2(x, y):
    result = 1
    while(y):
        if(y & 1 == 1):
            result *= x
        x *= x
        y >>= 1

    return result


### hint: exploit mathematical properties of exponentiation
### this is what I used in my efficient approach

### the suggested approach in the book is exactly the same as mine


start()
