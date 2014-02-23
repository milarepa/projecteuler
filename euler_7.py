#! /usr/bin/python3
"""
Find the 10001th prime number (6th is 13).
I think I can nail this with list comprehensions!
"""
def get_primes(n):

  # generate a list of non-primes for comparrison
  nonprimes = [j for i in range(2,n) for j in range(i*2,n,i)]

  # using non-primes we can find a list of primes to the nth number
  primes = [x for x in range(2,n) if x not in nonprimes]

  return primes

"""
Prime number tester
"""
def is_prime(n):

  # check for positive integer
  n = abs(int(n))

  # 0 and 1 are NOT prime
  if n < 2:
    return False
  # 2 is the only "even" prime
  if n == 2:
    return True
  # all other even numbers are not prime
  if not n & 1:
    return False
  # range begins with 3 and goes to square root of n for all odd numbers
  for x in range(3,int(n**0.5)+1,2):
    if n % x == 0:
      return False
  return True
