###
#   File name  : 4_5_p29.py
#   Author     : Hyunjin Kim
#   Date       : Jan 20, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : Write a program that multiplies two nonnegative integers.
#                The only operators you are allowed to use are:
#                - assignment
#                - the bitwise operators >>, <<, |, &, ~, ^
#                - equality checks and boolean combinations thereof
#                You may use loops and functions that you write yourself.
#                These constraints imply, for example, that you cannot
#                use increment or decrement, or test if x < y.
#   Background : Sometimes the processors used in ultra low-power devices
#                such as hearing aids do not have dedicated hardware for
#                performing multiplication. A program that needs to perform
#                multiplication must do so explicitly using lower-level primitives.
#
#   Instruction
#               1. import 4_5_p29
#               2. Run the function 4_5_p29.start()
#               3. The results will be generated in the console
###

### import modules
import timeit


### a function starting this script
def start():
    print("4_5_p29.py")

    start_time = timeit.default_timer()
    print("multiply(2, 3) = ", multiply(2, 3))
    print("multiply(32, 75) = ", multiply(32, 75))
    print("multiply(1, 7) = ", multiply(1, 7))
    print("multiply(26, 0) = ", multiply(26, 0))
    print("multiply(4, 8) = ", multiply(4, 8))
    for i in range(100):
        multiply(3, 8)
        multiply(345, 874)
        multiply(2353, 534)
    print("Execution Time: ", timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    print("multiply2(2, 3) = ", multiply2(2, 3))
    print("multiply2(32, 75) = ", multiply2(32, 75))
    print("multiply2(1, 7) = ", multiply2(1, 7))
    print("multiply2(26, 0) = ", multiply2(26, 0))
    print("multiply2(4, 8) = ", multiply2(4, 8))
    for i in range(100):
        multiply2(3, 8)
        multiply2(345, 874)
        multiply2(2353, 534)
    print("Execution Time: ", timeit.default_timer() - start_time)


### a function to add two given integers only using bitwise operators
def add(x, y):
    ### x + y = (x ^ y) + ((x & y) << 1)
    ### if y == 0, then it means now two integers can be clearly added with no bit elevation
    while(y != 0):
        ### XOR of two integers means they are different in those positions, so they are added in there
        remaining = x ^ y

        ### AND of two integers means they are duplicates in those positions, so they should be doubled ( << 1)
        y = (x & y) << 1

        ### save remaining to the x
        x = remaining

    return x


### a function to multiply two given integers only using bitwise operators
### x << n means x * 2^n
### e.g.,     6      x      5      =    3 0
###       0 0 1 1 0  x  0 0 1 0 1  = 1 1 1 1 0
###                         2   0
###     = 0 0 1 1 0  <<  2  +  0 0 1 1 0  <<  0
###     = 1 1 0 0 0  +  0 0 1 1 0  = 1 1 1 1 0
def multiply(x, y):
    z = 0
    while(y != 0):
        if(y & 1 == 1):
            z = add(x, z)

        x = x << 1
        y = y >> 1

    return z


### hint: add using bitwise operations; multiply using shift-and-add
### this is what I used in my approach

### a brute-force approach would be to perform repeated addition.
### the time complexity is very high - as much as O(2^n)


### the function introduced in the book
### the embedded add function is different from mine
def multiply2(x, y):
    def add2(a,b):
        running_sum, carryin, k, temp_a, temp_b = 0, 0, 1, a, b
        while temp_a or temp_b:
            ak, bk = a & k, b & k
            carryout = (ak & bk) | (ak & carryin) | (bk & carryin)
            running_sum |= ak ^ bk ^ carryin
            carryin, k, temp_a, temp_b = (carryout << 1, k << 1, temp_a >> 1, temp_b >> 1)

        return  running_sum | carryin

    running_sum = 0
    while x:
        if x & 1:
            running_sum = add2(running_sum, y)
        x, y = x >> 1, y << 1
    return running_sum


### it seems like my approach is faster than the one in the book


start()
