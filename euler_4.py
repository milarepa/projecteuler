#! /usr/bin/python3
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def palindrome():

  pal = []

  for i in range(999,800,-1):
    for j in range(999,800,-1):
      print(str(i) + " " + str(j)),
      product = str(i * j)
      if product == product[::-1]:
        pal.append(product)
        print(product),
  return pal
