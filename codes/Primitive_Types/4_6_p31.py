###
#   File name  : 4_6_p31.py
#   Author     : Hyunjin Kim
#   Date       : Jan 23, 2018
#   Email      : firadazer@gmail.com
#   Purpose    : Given two positive integers, compute their quotient,
#                using only the addition, subtraction, and shifting operators.
#   Example    : 24 // 6 = 4, 16 // 3 = 5
#
#   Instruction
#               1. import 4_6_p31
#               2. Run the function 4_6_p31.start()
#               3. The results will be generated in the console
###

### import modules
import timeit


### a function starting this script
def start():
    print("4_6_p31.py")

    start_time = timeit.default_timer()
    print("getQuotient(24, 6) = ", getQuotient(24, 6))
    print("getQuotient(16, 3) = ", getQuotient(16, 3))
    print("getQuotient(2, 2) = ", getQuotient(2, 2))
    print("getQuotient(2344, 11) = ", getQuotient(2344, 11))
    print("getQuotient(18763, 74) = ", getQuotient(18763, 74))
    print("getQuotient(82652374, 457) = ", getQuotient(82652374, 457))
    ### takes too long
    ### print("getQuotient(3465983405203405, 45764) = ", getQuotient(3465983405203405, 45764))
    print("Execution Time: ", timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    print("getQuotient2(24, 6) = ", getQuotient2(24, 6))
    print("getQuotient2(16, 3) = ", getQuotient2(16, 3))
    print("getQuotient2(2, 2) = ", getQuotient2(2, 2))
    print("getQuotient2(2344, 11) = ", getQuotient2(2344, 11))
    print("getQuotient2(18763, 74) = ", getQuotient2(18763, 74))
    print("getQuotient2(82652374, 457) = ", getQuotient2(82652374, 457))
    for i in range(10000):
        getQuotient2(3465983405203405, 764)
    print("Execution Time: ", timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    print("getQuotient3(24, 6) = ", getQuotient3(24, 6))
    print("getQuotient3(16, 3) = ", getQuotient3(16, 3))
    print("getQuotient3(2, 2) = ", getQuotient3(2, 2))
    print("getQuotient3(2344, 11) = ", getQuotient3(2344, 11))
    print("getQuotient3(18763, 74) = ", getQuotient3(18763, 74))
    print("getQuotient3(82652374, 457) = ", getQuotient3(82652374, 457))
    for i in range(10000):
        getQuotient3(3465983405203405, 764)
    print("Execution Time: ", timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    print("getQuotient4(24, 6) = ", getQuotient4(24, 6))
    print("getQuotient4(16, 3) = ", getQuotient4(16, 3))
    print("getQuotient4(2, 2) = ", getQuotient4(2, 2))
    print("getQuotient4(2344, 11) = ", getQuotient4(2344, 11))
    print("getQuotient4(18763, 74) = ", getQuotient4(18763, 74))
    print("getQuotient4(82652374, 457) = ", getQuotient4(82652374, 457))
    for i in range(10000):
        getQuotient4(3465983405203405, 764)
    print("Execution Time: ", timeit.default_timer() - start_time)


### a brute-force function that gives a quotient of two given positive integers as a return
### repeat x = x - y until x becomes negative and count how many times the repeat occurred
def getQuotient(x, y):
    cnt = 0
    while(x > 0 and x >= y):
        x -= y
        cnt += 1

    return cnt


### a more efficient function that gives a quotient of two given positive integers as a return
### shift the divider to the left before it becomes bigger than the divisor
### divisor = divisor - divider * the number of the shifts
### repeat the process until the divisor becomes smaller than the divider
def getQuotient2(x, y):
    quotient = 0
    while(x >= y):
        cnt = 0
        while(x >= (y << cnt)):
            cnt += 1

        if(cnt > 0):
            quotient += (1 << (cnt-1))
            x -= (y << (cnt-1))

    return quotient


### hint: relate x/y to (x-y)/y
### this is the approach I already used in my function


### a function described in the book
def getQuotient3(x, y):
    result, power = 0, 32
    y_power = y << power
    while x >= y:
        while y_power > x:
            y_power >>= 1
            power -= 1

        result += 1 << power
        x -= y_power
    return result


### but why the power is 32 rather than 63?
### I think it's because there would be rare situations that
### we have to deal with bigger than 2**32
### anyway, it could be 0 - 63


### an improved function that gives a quotient of two given positive integers as a return
### because the cnt must be always smaller than the previous cnt,
### changed it as decreasing every iteration to make the whole process faster
def getQuotient4(x, y):
    quotient = 0
    cnt = 63
    while(x >= y):
        while(x < (y << cnt)):
            cnt -= 1

        quotient += (1 << cnt)
        x -= (y << cnt)

    return quotient


start()
