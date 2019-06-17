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

    start_time = timeit.default_timer()
    print("generate_primes(18) = ", generate_primes(18))
    print("generate_primes(5) = ", generate_primes(5))
    print("generate_primes(24) = ", generate_primes(24))
    print("generate_primes(42) = ", generate_primes(42))
    print("generate_primes(99) = ", generate_primes(99))
    print("Execution Time: ", timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    print("generate_primes_from_1_to_n(18) = ", generate_primes_from_1_to_n(18))
    print("generate_primes_from_1_to_n(5) = ", generate_primes_from_1_to_n(5))
    print("generate_primes_from_1_to_n(24) = ", generate_primes_from_1_to_n(24))
    print("generate_primes_from_1_to_n(42) = ", generate_primes_from_1_to_n(42))
    print("generate_primes_from_1_to_n(99) = ", generate_primes_from_1_to_n(99))
    print("Execution Time: ", timeit.default_timer() - start_time)


### a brute-force approach would be one nested for loop that from 2 to the given number,
### check the current number has divisors. Time complexity would be O(n^2), space complexity: O(n).
### a more efficient approach would be using Sieve of Eratosthenes - time complexity: O(n^1.5), space complexity: O(n).
def get_primes(int_num):
    is_prime = [False, False] + [True] * (int_num-1)

    for i in range(2, math.floor(math.sqrt(int_num)+1)):
        prime = True
        for j in range(2, i):
            if i % j is 0:
                prime = False
                break

        if prime is True:
            for j in range(2*i, int_num+1, i):
                is_prime[j] = False

    primes = []
    for i in range(len(is_prime)):
        if is_prime[i]:
            primes.append(i)

    return primes


### a function described in the book
### but this makes an error when n = 5
### generate_primes(5) should be [2, 3, 5]
def generate_primes(n):
    primes = []
    # is_prime[p] represents if p is prime or not. Initially, set each to true,
    # expecting 0 and 1. Then use sieving to eliminate nonprimes.
    is_prime = [False, False] + [True] * (n-1)
    for p in range(2, n):
        if is_prime[p]:
            primes.append(p)
            # sieve p's multiples.
            for i in range(p, n+1, p):
                is_prime[i] = False

    return primes


### a more efficient function described in the book
### honestly, could not understand it
def generate_primes_from_1_to_n(n):
    size = (n - 3) // 2 + 1
    primes = [2] # stores the primes from 1 to n
    # is_prime[i] represents (2i + 3) is prime or not
    # initially set each to true. then use sieving to eliminate nonprimes
    is_prime = [True] * size
    for i in range(size):
        if is_prime[i]:
            p = i * 2 + 3
            primes.append(p)
            # sieving from p^2, where p^2 = (4i^2 + 12i + 9). The index in is_prime
            # is (2i^2 + 6i +3) because is_prime[i] represents 2i + 3
            # note that we need to use long for j because p^2 might overflow
            for j in range(2 * i**2 + 6 * i + 3, size, p):
                is_prime[j] = False

    return primes


start()
