###
#   File name  : p24.py
#   Author     : Hyunjin Kim
#   Date       : Nov 29, 2018
#   Email      : firadazer@gmail.com
#   Purpose    : How would you compute the parity of a very large number of 64-bit words?
#   Background : The parity of a binary word is 1 if the number of 1s in the word is odd;
#                otherwise, it is 0. For example, the parity of 1011 is 1, and the parity of 10001000 is 0.
#                Parity checks are used to detect single bit errors in data storage and communication.
#                It is fairly straightforward to write code that computes the parity of a single 64-bit word.
#
#   Instruction
#               1. import p24
#               2. Run the function p24.start()
#               3. The results will be generated in the console
###

### import modules
import timeit

### a function starting this script
def start():
    print("p24.py")

    ### some example integers
    a = Random64BinGeneration(64, 1234)
    b = Random64BinGeneration(64, 4321)
    c = int('1011',2)
    d = int('10001000',2)

    ### print the parity of the examples
    start_time = timeit.default_timer()
    print("Input: ", bin(a), " Parity: ", parityCheck(a))
    print("Input: ", bin(b), " Parity: ", parityCheck(b))
    print("Input: ", bin(c), " Parity: ", parityCheck(c))
    print("Input: ", bin(d), " Parity: ", parityCheck(d))
    print("Execution Time: ", timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    print("Input: ", bin(a), " Parity: ", parity(a))
    print("Input: ", bin(b), " Parity: ", parity(b))
    print("Input: ", bin(c), " Parity: ", parity(c))
    print("Input: ", bin(d), " Parity: ", parity(d))
    print("Execution Time: ", timeit.default_timer() - start_time)

### a function to generate a random n-bit integer number
def Random64BinGeneration(n, seed):
    # print("Random64BinGeneration()")

    ### load library
    import random

    ### set a seed for random generation
    random.seed(seed)

    ### return random n bit integer
    return random.randint(0, 2**n-1)


### a function to check parity of a given integer number
def parityCheck(input_word):
    # print("parityCheck()")

    ### return only if a given number is positive
    if input_word >= 0:
        ### load library
        import math

        ### set initial count
        cnt = 0

        ### compute how many 1s in the number in binary form
        while math.floor(input_word / 2) != 0:
            if input_word % 2 == 1:
                cnt = cnt + 1
            input_word = math.floor(input_word / 2)
        if(input_word == 1):
            cnt = cnt + 1

        ### return the parity
        if(cnt % 2 == 1):
            return 1
        else:
            return 0
    else:
        print("ERROR: the given integer is negative. It should be equal or bigger than 0.")


### a brute-force algorithm described in the book
def parity(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result


start()
