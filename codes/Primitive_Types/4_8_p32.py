###
#   File name  : 4_8_p32.py
#   Author     : Hyunjin Kim
#   Date       : Jan 23, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : Write a program which takes an integer and returns the integer
#                corresponding to the digits of the input written in reverse order.
#   Example    : The reverse of 42 is 24, and the reverse of -314 is -413.
#
#   Instruction
#               1. import 4_8_p32
#               2. Run the function 4_8_p32.start()
#               3. The results will be generated in the console
###

### import modules
import timeit


### a function starting this script
def start():
    print("4_8_p32.py")

    start_time = timeit.default_timer()
    print("reverse_digit(42) = ", reverse_digit(42))
    print("reverse_digit(-314) = ", reverse_digit(-314))
    print("reverse_digit(5) = ", reverse_digit(5))
    print("reverse_digit(329573) = ", reverse_digit(329573))
    print("reverse_digit(-9837434) = ", reverse_digit(-9837434))
    print("Execution Time: ", timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    print("reverse_digit2(42) = ", reverse_digit2(42))
    print("reverse_digit2(-314) = ", reverse_digit2(-314))
    print("reverse_digit2(5) = ", reverse_digit2(5))
    print("reverse_digit2(329573) = ", reverse_digit2(329573))
    print("reverse_digit2(-9837434) = ", reverse_digit2(-9837434))
    print("Execution Time: ", timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    print("reverse_digit3(42) = ", reverse_digit3(42))
    print("reverse_digit3(-314) = ", reverse_digit3(-314))
    print("reverse_digit3(5) = ", reverse_digit3(5))
    print("reverse_digit3(329573) = ", reverse_digit3(329573))
    print("reverse_digit3(-9837434) = ", reverse_digit3(-9837434))
    print("Execution Time: ", timeit.default_timer() - start_time)


### a function to return reversed digit of a given integer
def reverse_digit(x):
    ispositive = True
    if x < 0:
        ispositive = False
        x = abs(x)

    n = 0
    while x > 10**n:
        n += 1

    y = 0
    for i in range((n-1), -1, -1):
        y += (x // (10**i)) * 10**(n-i-1)
        x = x % (10**i)

    if ispositive:
        return y
    else:
        return -y


### hint: how would you solve the same problem if the input is presented as a string?


### a function to change input integer to string and reverse it - based on the hint
def reverse_digit2(x):
    ispositive = True
    if x < 0:
        ispositive = False
        x = abs(x)

    x = str(x)

    if ispositive:
        return x[::-1]
    else:
        return "-" + x[::-1]


### an efficient function in the book
def reverse_digit3(x):
    result, x_remaining = 0, abs(x)
    while x_remaining:
        result = result * 10 + x_remaining % 10
        x_remaining //= 10
    return -result if x < 0 else result


start()
