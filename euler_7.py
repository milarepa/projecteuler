#! /usr/bin/python3
"""
Find the 10001th prime number (6th is 13).
Originally though to do this with list comprehensions
but the better implementation was with a slick verion of a prime
number generator from http://code.activestate.com/recipes/117119/
More power to ya, Sieve of Eratosthenes
"""
# prime number generator with comment!
def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}

    # The running integer that's checked for primeness
    q = 2

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1


def prime_list(max):

  gen = gen_primes()
  plist = []
  count = 0

  for i in gen:
    plist.append(i)
    count += 1
    if count >= max:
      break

  return plist


