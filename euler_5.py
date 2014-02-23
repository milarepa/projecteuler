#! / usr/bin/python
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import functools as f

def gcd(a,b):

  while b:
    a, b = b, a % b

  return a

def lcm(a,b):
  return a * b // gcd(a,b)

def lcmm(*args):
  return f.reduce(lcm, args)

# usage - answer = lcmm(*range(1,20))

