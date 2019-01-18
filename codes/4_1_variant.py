###
#   File name  : 4_1_variant.py
#   Author     : Hyunjin Kim
#   Date       : Jan 17, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : Write expressions that use bitwise operators, equality checks, and Boolean operators to do the following in O(1) time.
#   Background : 1. Right propagate the rightmost set bit in x, e.g., turns (01010000)2 to (01011111)2
#                2. Compute x mod a power of two, e.g., returns 13 for 77 mod 64
#                3. Test if x is a power of 2, i.e., evaluates to true for x = 1,2,4,8,...,false for all other values
#
#   Instruction
#               1. import 4_1_variant.py
#               2. Run the function 4_1_variant.start()
#               3. The results will be generated in the console
###

### import modules
import timeit


### a function starting this script
def start():
    print("4_1_variant.py")

    start_time = timeit.default_timer()
    print("fun_one(01010000) = ", bin(fun_one(int('01010000',2))))
    print("fun_one(11010010) = ", bin(fun_one(int('11010010', 2))))
    print("fun_one(01110111) = ", bin(fun_one(int('01110111', 2))))
    print("Execution Time: ", timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    print("77 mod 64 = ", fun_two(77, 64))
    print("83 mod 32 = ", fun_two(83, 32))
    print("30 mod 16 = ", fun_two(30, 16))
    print("Execution Time: ", timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    print("fun_three(5) = ", fun_three(5))
    print("fun_three(256) = ", fun_three(256))
    print("fun_three(1024) = ", fun_three(1024))
    print("fun_three(64) = ", fun_three(64))
    print("fun_three(345) = ", fun_three(345))
    print("fun_three(1) = ", fun_three(1))
    print("fun_three(0) = ", fun_three(0))
    print("Execution Time: ", timeit.default_timer() - start_time)


### 1. Right propagate the rightmost set bit in x, e.g., turns (01010000)2 to (01011111)2
def fun_one(x):
    if(x == 0):
        return 0
    else:
        return(x | (x-1))


### 2. Compute x mod a power of two, e.g., returns 13 for 77 mod 64
def fun_two(x, y):
    return(x & (y-1))


### 3. Test if x is a power of 2, i.e., evaluates to true for x = 1,2,4,8,...,false for all other values
def fun_three(x):
    if(x == 0):
        return False
    elif((x & (x-1)) == 0):
        return True
    else:
        return False


start()
