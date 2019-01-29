###
#   File name  : 4_9_p33.py
#   Author     : Hyunjin Kim
#   Date       : Jan 28, 2018
#   Email      : firadazer@gmail.com
#   Purpose    : Write a program that takes an integer and determines if that
#                integer's representation as a decimal string is a palindrome
#   Background : A palindromic string is one which reads the same forwards and backwards,
#                e.g., "redivider".
#   Example    : Your program should return true for the inputs 0, 1, 7, 11, 121, 333,
#                and 2147447412, and false for the inputs -1, 12, 100, and 2147483647.
#
#   Instruction
#               1. import 4_9_p33
#               2. Run the function 4_9_p33.start()
#               3. The results will be generated in the console
###

### import modules
import timeit
import math


### a function starting this script
def start():
    print("4_9_p33.py")

    start_time = timeit.default_timer()
    print("is_palindrome(0) = ", is_palindrome(0))
    print("is_palindrome(1) = ", is_palindrome(1))
    print("is_palindrome(-1) = ", is_palindrome(-1))
    print("is_palindrome(12) = ", is_palindrome(12))
    print("is_palindrome(7) = ", is_palindrome(7))
    print("is_palindrome(11) = ", is_palindrome(11))
    print("is_palindrome(121) = ", is_palindrome(121))
    print("is_palindrome(100) = ", is_palindrome(100))
    print("is_palindrome(333) = ", is_palindrome(333))
    print("is_palindrome(2147483647) = ", is_palindrome(2147483647))
    print("is_palindrome(2147447412) = ", is_palindrome(2147447412))
    print("Execution Time: ", timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    print("is_palindrome2(0) = ", is_palindrome2(0))
    print("is_palindrome2(1) = ", is_palindrome2(1))
    print("is_palindrome2(-1) = ", is_palindrome2(-1))
    print("is_palindrome2(12) = ", is_palindrome2(12))
    print("is_palindrome2(7) = ", is_palindrome2(7))
    print("is_palindrome2(11) = ", is_palindrome2(11))
    print("is_palindrome2(121) = ", is_palindrome2(121))
    print("is_palindrome2(100) = ", is_palindrome2(100))
    print("is_palindrome2(333) = ", is_palindrome2(333))
    print("is_palindrome2(2147483647) = ", is_palindrome2(2147483647))
    print("is_palindrome2(2147447412) = ", is_palindrome2(2147447412))
    print("Execution Time: ", timeit.default_timer() - start_time)


### a function to check a given integer is palindrome
### change the integer to a string and reverse it and check equality: a typical approach
def is_palindrome(x):
    x = str(x)
    y = x[::-1]
    if x == y:
        return True
    else:
        return False


### hint: it's easy to come up with a simple expression that extracts the least significant digit.
### can you find a simple expression for the most significant digit?


### a function in the book
### the number of digits, n = floor(log10(x)) + 1
### the least significant digit is x mod 10
### the most significant digit is x // 10**(n-1)
def is_palindrome2(x):
    if x < 0:
        return False

    num_digits = math.floor(math.log10(x)) + 1
    msd_mask = 10**(num_digits -1)
    for i in range(num_digits // 2):
        if x // msd_mask != x % 10:
            return False
        x %= msd_mask
        x //= 10
        msd_mask //= 100
    return True


start()
