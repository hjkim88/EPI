###
#   File name  : 5_9_p49.py
#   Author     : Hyunjin Kim
#   Date       : Jun 12, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : A natural number is called a prime if it is bigger than 1 and has no divisors other than 1 and itself.
#                Write a program that takes an integer argument and returns all the primes between 1 and that integer.
#
#   Example    : input: 18, output: [2, 3, 5, 7, 11, 13, 17]
#                input: 5, output: [2, 3, 5]
#                input: 24, output: [2, 3, 5, 7, 11, 13, 17, 19, 23]
#                input: 42, output: [2, 3, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
#                input: 99, output: [2, 3, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
#
#   Instruction
#               1. import 5_9_p49.py
#               2. Run the function 5_9_p49.start()
#               3. The results will be generated in the console
###

### import modules
import timeit
import math

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


### a brute-force approach would be one nested for loop that from 2 to the given number,
### check the current number has divisors. Time complexity would be O(n^2), space complexity: O(n).
### a more efficient approach would be using Sieve of Eratosthenes - time complexity: O(n^1.5), space complexity: O(n).
def get_primes(int_num):
    primes = [2] + [x for x in range(3, int_num+1, 2)]

    for i in range(3, math.floor(math.sqrt(int_num)+1)):
        for number in primes[2:]:
            if number % i is 0:
                primes.remove(number)

    if int_num is 1:
        return None
    else:
        return primes


start()
