###
#   File name  : 4_10_p34.py
#   Author     : Hyunjin Kim
#   Date       : Jan 28, 2018
#   Email      : firadazer@gmail.com
#   Purpose    : How would you implement a random number generator that generates
#                a random integer i between a and b, inclusive, given a random
#                number generator that produces zero or one with equal probability?
#                All values in [a,b] should be equally likely.
#   Background : This problem is motivated by the following scenario.
#                Six friends have to select a designated driver using a single
#                unbiased coin. The process should be fair to everyone.
#
#   Instruction
#               1. import 4_10_p34
#               2. Run the function 4_10_p34.start()
#               3. The results will be generated in the console
###

### import modules
import timeit
import random


### a function starting this script
def start():
    print("4_10_p34.py")

    start_time = timeit.default_timer()
    print("generate_random_num(1, 6) = ", generate_random_num(1, 6))
    print("generate_random_num(25, 125) = ", generate_random_num(25, 125))
    print("generate_random_num(3, 3) = ", generate_random_num(3, 3))
    print("generate_random_num(9, 54) = ", generate_random_num(9, 54))
    print("generate_random_num(48, 2) = ", generate_random_num(48, 2))
    print("Execution Time: ", timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    print("generate_random_num2(1, 6) = ", generate_random_num2(1, 6))
    print("generate_random_num2(25, 125) = ", generate_random_num2(25, 125))
    print("generate_random_num2(3, 3) = ", generate_random_num2(3, 3))
    print("generate_random_num2(9, 54) = ", generate_random_num2(9, 54))
    print("generate_random_num2(48, 2) = ", generate_random_num2(48, 2))
    print("Execution Time: ", timeit.default_timer() - start_time)


### a brute-force approach to generate random number
### a tournament approach
def generate_random_num(a, b):
    if a > b:
        a, b = b, a
    x = list(range(a, b+1))
    while len(x) > 1:
        y = list()
        for i in range(len(x)):
            if random.randint(0,1):
                y.append(i)
        if len(y) > 0:
            x = list(x[i] for i in y)

    return x[0]


### a more efficient approach to generate random number
### this is improved than the above since the above determines 0/1 for one each,
### while this one can solve two by one 0/1
def generate_random_num2(a, b):
    if a > b:
        a, b = b, a
    x = list(range(a, b + 1))
    while len(x) > 1:
        y = list()
        for i in range(len(x)//2):
            if random.randint(0,1):
                y.append(i*2)
            else:
                y.append(i*2+1)
        if len(x) % 2 and random.randint(0,1):
            y.append(len(x)-1)
        x = list(x[i] for i in y)

    return(x[0])


### hint: how would you mimic a three-sided coin with a two-sided coin?


### a more efficient function to generate random number
### using binary numbers
def generate_random_num3(a, b):
    return(a)


start()
