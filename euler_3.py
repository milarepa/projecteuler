#! /usr/bin/python
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def prime(n,f):

  i = f

  while (n % i != 0 and i * i < n):
    i += 1

  if (i * i < n):
    return prime(n / i, 2)
  else:
    print ("The largerst prime factor is: ", n)


