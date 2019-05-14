###
#   File name  : 5_2_variant.py
#   Author     : Hyunjin Kim
#   Date       : May 13, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : 1. Write a program which takes as input two arrays s and t of bits
#                   encoding binary numbers Bs and Bt, respectively, and returns
#                   a new array of bits representing the number Bs + Bt.
#
#   Background : This is related to the "5_2_p43.py".
#
#   Instruction
#               1. import 5_2_variant
#               2. Run the function 5_2_variant.start()
#               3. The results will be generated in the console
###

### import modules
import timeit

### a function starting this script
def start():
    print("5_2_variant.py")

    start_time = timeit.default_timer()
    print("fun_one([1, 4, 0, 4, 5], [4, 2, 6, 7, 8]) = ", fun_one([1, 4, 0, 4, 5], [4, 2, 6, 7, 8]))
    print("fun_one([9, 9, 9, 9, 5, 3, 5, 6, 3], [6, 2, 6, 7, 8]) = ", fun_one([9, 9, 9, 9, 5, 3, 5, 6, 3], [6, 2, 6, 7, 8]))
    print("fun_one([5, 3, 4, 0, 5], [1, 3, 2, 0, 0]) = ", fun_one([5, 3, 4, 0, 5], [1, 3, 2, 0, 0]))
    print("fun_one([2, 5, 4, 3, 6], [2, 3, 4]) = ", fun_one([2, 5, 4, 3, 6], [2, 3, 4]))
    print("fun_one([4, 3, 5, 0, 0], [0, 0, 6, 7, 8]) = ", fun_one([4, 3, 5, 0, 0], [0, 0, 6, 7, 8]))
    print("Execution Time: ", timeit.default_timer() - start_time)


### a function to add two binary numbers in array format
### a brute-force approch would be convert them to numeric values
### and add them then convert back to a string array
### but I will add each bit from the LSB
### time complexity: O(n), space complexity: O(1)
def fun_one(Bs, Bt):
    residue = 0

    if len(Bs) > len(Bt):
        for i in range(len(Bt)):
            sum = Bs[len(Bs)-1-i] + Bt[len(Bt)-1-i] + residue
            if sum > 9:
                Bs[len(Bs)-1-i] = sum - 10
                residue = 1
            else:
                Bs[len(Bs)-1-i] = sum
                residue = 0
        for i in range(len(Bt), len(Bs)):
            sum = Bs[len(Bs)-1-i] + residue
            if sum > 9:
                Bs[len(Bs) - 1 - i] = sum - 10
                residue = 1
            else:
                Bs[len(Bs) - 1 - i] = sum
                residue = 0
        if residue == 1:
            Bs.insert(0, 1)
        return Bs
    else:
        for i in range(len(Bs)):
            sum = Bt[len(Bt)-1-i] + Bs[len(Bs)-1-i] + residue
            if sum > 9:
                Bt[len(Bt)-1-i] = sum - 10
                residue = 1
            else:
                Bt[len(Bt)-1-i] = sum
                residue = 0
        for i in range(len(Bs), len(Bt)):
            sum = Bt[len(Bt)-1-i] + residue
            if sum > 9:
                Bt[len(Bt) - 1 - i] = sum - 10
                residue = 1
            else:
                Bt[len(Bt) - 1 - i] = sum
                residue = 0
        if residue == 1:
            Bt.insert(0, 1)
        return Bt


start()
