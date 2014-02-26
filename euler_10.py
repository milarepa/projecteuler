#!/usr/bin/python3
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
Originally I thought this to mean "below 2Mil primes" and was getting an
answer 3193847394...(12 or 13 digits). When I realized that it was the
sum of the primes in a set of 2mil it was all to easy.
Thanks to DaniWeb for the "is_prime()" function that I use so often on
games like this...(my refusal to re-invent the wheel)
"""

def is_prime(n):
    n = abs(int(n))

    if n < 2:
        return False

    if n == 2:
        return True

    if not n & 1:
        return False

    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True


def prime_sum(n):

  psum = 0

  for i in range(n):
    if is_prime(i):
      psum += i

  return psum
