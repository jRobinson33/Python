
#6/18/2019

import math
import time


def is_prime_v1(n):
    """Return 'True if 'n' is a prime number. False otherwise."""

    if n==1:
        return False #1 is not a prime

    for d in range(2, n):
        if n % d == 0:
            return False
    return True

#===== Test Function =====
t0 = time.time()
for n in range(1, 100000):
    #print(n, is_prime_v1(n))
    is_prime_v1(n)
t1 = time.time()
print("Time required: ", t1 - t0)

def is_prime_v2(n):
    """Return 'True' if 'N' is a prime number. False otherwise."""

    if n == 1:
        return False # 1 is not prime

    max_divisor = math.floor(math.sqrt(n))
    for d in range(2, 1 + max_divisor):
        if n % d == 0:
            return False
    return True

# ===== Test Function =====
t3 = time.time()
for n in range(1, 100000):
    #print(n, is_prime_v2(n))
    is_prime_v2(n)
t4 = time.time()
print("Time required: ", t4 - t3)

def is_prime_v3(n):
    """Return 'True' if 'N' is a prime number. False otherwise."""

    if n == 1:
        return False # 1 is not prime
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False

    max_divisor = math.floor(math.sqrt(n))
    for d in range(3, 1 + max_divisor, 2):
        if n % d == 0:
            return False
    return True

# ===== Test Function =====
t5 = time.time()
for n in range(1, 100000):
    #print(n, is_prime_v2(n))
    is_prime_v3(n)
t6 = time.time()
print("Time required: ", t6 - t5)