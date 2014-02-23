#! /usr/bin/python3
"""
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def s_sqrs():

  sqrs = [x**2 for x in range(1,101)]
  sum_of_squares = sum(sqrs)

  lst = [x+1 for x in range(0,100)]
  square_of_the_sum = sum(lst)**2

  diff = square_of_the_sum - sum_of_squares

  return diff
