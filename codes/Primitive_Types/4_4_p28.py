###
#   File name  : 4_4_p28.py
#   Author     : Hyunjin Kim
#   Date       : Jan 19, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : Write a program which takes as input a nonnegative integer x and returns a number y
#                which is not equal to x, but has the same weight as x and their difference,
#                |y-x|, is as small as possible. You can assume x is not 0, or all 1s.
#                You can assume the integer fits in 64 bits.
#   Example    : If x = 6, you should return 5.
#   Background : Define the weight of a nonnegative integer x to be the number of bits that are
#                set to 1 in its binary representation. For example, since 92 in base-2-equals
#                (1011100)2, the weight of 92 is 4.
#
#   Instruction
#               1. import 4_4_p28
#               2. Run the function 4_4_p28.start()
#               3. The results will be generated in the console
###

### import modules
import timeit


### a function starting this script
def start():
    print("4_4_p28.py")

    start_time = timeit.default_timer()
    print("getSameWeightVal(100100) = ", bin(getSameWeightVal(int("100100", 2))))
    print("getSameWeightVal(100101) = ", bin(getSameWeightVal(int("100101", 2))))
    print("getSameWeightVal(0101111) = ", bin(getSameWeightVal(int("0101111", 2))))
    print("getSameWeightVal(1101011) = ", bin(getSameWeightVal(int("1101011", 2))))
    print("Execution Time: ", timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    print("getSameWeightVal2(100100) = ", bin(getSameWeightVal2(int("100100", 2))))
    print("getSameWeightVal2(100101) = ", bin(getSameWeightVal2(int("100101", 2))))
    print("getSameWeightVal2(0101111) = ", bin(getSameWeightVal2(int("0101111", 2))))
    print("getSameWeightVal2(1101011) = ", bin(getSameWeightVal2(int("1101011", 2))))
    print("Execution Time: ", timeit.default_timer() - start_time)


### a brute-force function to get the closest, same-weight integer of the input
### from the LSB to MSB, if there are flipped bits in sequence (01 or 10), just swap them
def getSameWeightVal(x):
    for i in range(63):
        if(((x >> i) & 1) != ((x >> (i+1)) & 1)):
            x ^= (1 << i | 1 << (i+1))
            break

    return x


### a more efficient function to get the closest, same-weight integer of the input
### find the right-most 1, and then swap it with the 0 in the closest right side
### if there is no 0 in the right side of the right-most 1 (which means the 1 is the right-most bit), swap right-most 0 to its right next 1
def getSameWeightVal2(x):
    ONE_BIT_MASK = x & ~(x-1)

    if((ONE_BIT_MASK-1) == 0):
        ZERO_BIT_MASK = ~x & ~(~x - 1)
        x ^= (ZERO_BIT_MASK | (ZERO_BIT_MASK >> 1))
    else:
        x ^= (ONE_BIT_MASK | (ONE_BIT_MASK >> 1))

    return (x)


### hint: start with the least significant bit.
### hey... that is already used in my brute-force approach..
### the brute-force approach in the book is to try all integers x-1, x+1, x-2, x+2, ...,
### stopping as soon as they encounter one with the same weight - a real brute-force one..

### variant: solve the same problem in O(1) time and space
### that is my improved approach. I did it already.


start()
