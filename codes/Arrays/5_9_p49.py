###
#   File name  : 5_9_p49.py
#   Author     : Hyunjin Kim
#   Date       : Jun 12, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : A natural number is called a prime if it is bigger than 1 and has no divisors other than 1 and itself.
#                Write a program that takes an integer argument and returns all th primes between 1 and that integer.
#
#   Example    : input: 18, output: [2, 3, 5, 7, 11, 13, 17]
#
#   Instruction
#               1. import 5_9_p49.py
#               2. Run the function 5_9_p49.start()
#               3. The results will be generated in the console
###

### import modules
import timeit

### a function starting this script
def start():
    print("5_9_p49.py")

    start_time = timeit.default_timer()
    print("get_primes(18) = ", get_primes(18))
    print("get_primes(5) = ", get_primes(5))
    print("get_primes(24) = ", get_primes(24))
    print("get_primes(42) = ", get_primes(42))
    print("get_primes(99) = ", get_primes(99))
    print("Execution Time: ", timeit.default_timer() - start_time)


###
def get_primes(int_num):
    primes = []

    return primes


start()
