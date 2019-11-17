###
#   File name  : 5_13_p55.py
#   Author     : Hyunjin Kim
#   Date       : Nov 15, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : Design a program that takes as input a size k, and reads packets, continuously maintaining
#                a uniform random subset of size k of the read packets.
#
#   Instruction
#               1. import 5_13_p55.py
#               2. Run the function 5_13_p55.start()
#               3. The results will be generated in the console
###

### import modules
import timeit
import random

### a function starting this script
def start():
    print("5_13_p55.py")

    ### THE PACKETS ARE NOT ACTUALLY IN STREAMING HERE, SO RUNNING TIME MIGHT BE DIFFERENT TO OUR EXPECTATIONS.

    start_time = timeit.default_timer()
    print("packet_sniffer(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'], 5) = ",
          packet_sniffer(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'], 5))
    print("packet_sniffer(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'], 5) = ",
          packet_sniffer(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'], 5))
    print("packet_sniffer(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'], 5) = ",
          packet_sniffer(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'], 5))
    print("packet_sniffer(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'], 5) = ",
          packet_sniffer(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'], 5))
    print("packet_sniffer(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'], 5) = ",
          packet_sniffer(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'], 5))
    print("Execution Time: ", timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    print("packet_sniffer2(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'], 5) = ",
          packet_sniffer2(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'], 5))
    print("packet_sniffer2(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'], 5) = ",
          packet_sniffer2(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'], 5))
    print("packet_sniffer2(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'], 5) = ",
          packet_sniffer2(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'], 5))
    print("packet_sniffer2(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'], 5) = ",
          packet_sniffer2(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'], 5))
    print("packet_sniffer2(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'], 5) = ",
          packet_sniffer2(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'], 5))
    print("Execution Time: ", timeit.default_timer() - start_time)


### a packet sniffer
### a brute-force approach
### read packet set and select random k samples
def packet_sniffer(packet, k):
    idx = random.sample(range(len(packet)), k)
    idx.sort()

    return [packet[x] for x in idx]


### a packet sniffer2
### a more efficient approach
### read the first k packets and just replace one of the packets while reading remaining packets in the stream
### this can downsize the space complexity hugely and the time complexity
def packet_sniffer2(packet, k):
    result = packet[0:k]
    for x in range(k, len(packet)):
        idx = random.sample(range(x), 1)
        if idx[0] < k:
            result[idx[0]] = packet[x]

    return result


start()
