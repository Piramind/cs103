import random


def is_prime(num: int) -> bool:
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
def gcd(a: int, b: int) -> int:
    for i in range(a - 1, 1, -1):
        for j in range(b - 1, i - 1, -1):
            if i == j and a % i == 0 and b % i == 0:
                return i


