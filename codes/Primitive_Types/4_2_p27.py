###
#   File name  : 4_2_p27.py
#   Author     : Hyunjin Kim
#   Date       : Jan 18, 2018
#   Email      : firadazer@gmail.com
#   Purpose    : Implement code that takes an input as 64-bit integer and swaps the bits at indices i and j.
#   Background : A 64-bit integer can be viewed as an array of 64 bits, with the bit at index 0
#                corresponding to the least significant bit (LSB), and the bit at index 63
#                corresponding to the most significant bit (MSB).
#                e.g., the 8-bit integer 73 can be viewed as array of bits, with the LSB being at index 0.
#                 0  1   0   0   1   0   0   1
#                MSB                        LSB
#
#   Instruction
#               1. import 4_2_p27
#               2. Run the function 4_2_p27.start()
#               3. The results will be generated in the console
###

### import modules
import timeit


### a function starting this script
def start():
    print("4_2_p27.py")

    start_time = timeit.default_timer()
    print("bit_swap(01011010, 1, 5) = ", bin(bit_swap(int('01011010', 2), 1, 5)))
    print("Execution Time: ", timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    print("bit_swap2(01011010, 1, 5) = ", bin(bit_swap2(int('01011010', 2), 1, 5)))
    print("Execution Time: ", timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    print("swap_bits(01011010, 1, 5) = ", bin(swap_bits(int('01011010', 2), 1, 5)))
    print("Execution Time: ", timeit.default_timer() - start_time)


### a brute-force function to swap bits in a 64-bit integer
def bit_swap(integer, i, j):
    a = integer & (2**i)
    b = integer & (2**j)

    if(a == 0):
        c = integer & (~(2**j))
    else:
        c = integer | (2**j)

    if(b == 0):
        c = c & (~(2**i))
    else:
        c = c | (2**i)

    return c


### hint: when is the swap necessary?


### a more efficient function to swap bits than the brute-force approach
def bit_swap2(integer, i, j):
    ### if the designated two bits are the same, no need to swap

    ### test the two bits are the same
    a = integer & (2**i + 2**j)

    ### if the two bits are all 0
    if(a == 0):
        return integer
    ### if the two bits are all 1
    elif(a == (2**i + 2**j)):
        return integer
    else:
        return (integer ^ (2**i + 2**j))


### the one introduced in the book
def swap_bits(x, i, j):
    if(x >> i) & 1 != (x >> j) & 1:
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask
    return x


start()
