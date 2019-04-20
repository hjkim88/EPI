###
#   File name  : 4_3_p28.py
#   Author     : Hyunjin Kim
#   Date       : Jan 18, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : Write a program that takes a 64-bit word and returns the 64-bit word consisting of
#                the bits of the input word in reverse order.
#   Example    : If the input is (1110000000000001), the output should be (1000000000000111).
#
#   Instruction
#               1. import 4_3_p28
#               2. Run the function 4_3_p28.start()
#               3. The results will be generated in the console
###

### import modules
import timeit


### a function starting this script
def start():
    print("4_3_p28.py")

    start_time = timeit.default_timer()
    print("reverse_bit(01011010, 8) = ", bin(reverse_bit(int('01011010', 2), 8)))
    print("reverse_bit(1110000000000001, 16) = ", bin(reverse_bit(int('1110000000000001', 2), 16)))
    print("Execution Time: ", timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    print("reverse_bit2(01011010, 8) = ", bin(reverse_bit2(int('01011010', 2), 8)))
    print("reverse_bit2(1110000000000001, 16) = ", bin(reverse_bit2(int('1110000000000001', 2), 16)))
    print("Execution Time: ", timeit.default_timer() - start_time)


### a brute-force function to reverse the bits of the input (n-bit word)
### save n bits and remake one with the reversed order
def reverse_bit(x, n):
    y = 0

    for i in range(n):
        if((1 & (x >> i)) == 1):
            y |= 1 << (n-i-1)

    return y


### a function to reverse the bits of the input with bit swapping
### if the rightest and the leftest bits are the same, no need to change them
def reverse_bit2(x, n):
    for i in range(n//2):
        if(((x >> (n-i-1)) & 1) != ((x >> i) & 1)):
            bit_mask = (1 << (n-i-1)) | (1 << i)
            x ^= bit_mask

    return x


### hint: use a lookup table


### a more efficient function to reverse the bits of the input
### using a lookup table - 64bit-input only
# def reverse_bit3(x):
#     MASK_SIZE = 16
#     BIT_MASK = 0xFFFF
#     return (PRECOMPUTED_REVERSE[x >> (3 * MASK_SIZE)]   |
#              (PRECOMPUTED_REVERSE[(x >> (2 * MASK_SIZE)) & BIT_MASK] << MASK_SIZE) |
#              (PRECOMPUTED_REVERSE[(x >> MASK_SIZE) & BIT_MASK] << (2 * MASK_SIZE)) |
#              (PRECOMPUTED_REVERSE[x & BIT_MASK] << (3 * MASK_SIZE)))


start()
