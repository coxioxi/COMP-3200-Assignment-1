# COMP 3200 - Fall 2025 - Programming Assignment 1

# Complete all of the following functions. Currently they all just
# 'pass' rather than explicitly return a value, which means that they
# implicitly return None. They all include doctests, which you can
# test by running this file as a script: python3 assign1.py

# Feel free to add your own doctests.


def tnp1(n):
    """
    The "three N plus 1" sequence starting from a positive integer n
    is defined as follows: if n is 1, stop; if n is odd, the next
    number is 3n+1; if n is even, the next number is n//2. For
    example, here's the sequence starting from 7:

        7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1

    The function tnp1 must return the total length of the sequence
    starting from n, so

    >>> tnp1(7)
    17
    >>> tnp1(5)
    6
    >>> tnp1(11)
    15

    Remember that // performs integer division in Python.
    """
    pass

    if(n == 1):
        return 1
    elif(n % 2 != 0):
        return 1 + tnp1(3*n+1)
    else:
        return 1 + tnp1(n//2)


def multRange(a, b):
    """
    Returns the product of the integers from a to b.
    This must work for *any* two integers a and b.
    If a is greater than b, the product is defined to be 1.

    >>> multRange(1, 5)
    120
    >>> multRange(3, 6)
    360
    >>> multRange(5, 2)
    1
    
    """
    pass

    if(a > b):
        return 1
    else:
        return a * multRange(a+1, b) 
    



def ascend(xs):
    """
    Returns a new sorted list from xs by working left-to-right and
    dropping any element that is less than any of its predecessors in
    the list. Can easily be done in linear time. For example,

    >>> ascend([])
    []
    >>> ascend(list('godfather'))
    ['g', 'o', 't']
    >>> ascend([1,3,2,6,5,6,9,0])
    [1, 3, 6, 6, 9]
    """
    pass


def closest_point(xys):
    """
    Given a list of ordered pairs representing points in the plane,
    return the point that is closest to the origin. If two or more
    points are equally close, return the one that appears earliest in
    the list. If the list is empty, return None. For example,

    >>> closest_point([(1,2),(4,-2),(-0.5,0),(3.14,2)])
    (-0.5, 0)
    """
    pass


def count_if(p, xs):
    """
    Returns the number of elements of list xs that satisfy predicate p.

    >>> count_if(lambda x: x > 5, [8,6,7,5,3,0,9])
    4
    >>> count_if(lambda c: c.isupper(), list('Heavy Rain'))
    2
    """
    pass


def find_last(p, xs):
    """
    Returns the last element in list xs that satisfies predicate p. If
    there is no element in xs that satisfies p, it returns None.

    >>> find_last(lambda x: x > 10, [7,3,5,9,9,1,5,3])
    >>> find_last(lambda x: x % 2 == 0, [7,2,5,4,4,1,6,3])
    6
    """
    pass


def fixed_point(f, x0, n=1000):
    """
    A fixed point of function f is a value x such that f(x) is x. Try
    to find a fixed point of f starting with x0: compute f(x0),
    f(f(x0)), f(f(f(x0))), ..., until two successive values are the
    same. If you find a fixed point in at most n steps, return it,
    otherwise return None.

    >>> fixed_point(lambda x: x + 1, 100)
    >>> fixed_point(lambda x: x//2 + 1, 37)
    2
    >>> fixed_point(lambda s: s[2]+s[1]+s[3:]+s[1], 'football')
    'oooooooo'

    Not all functions have fixed points, and not all fixed points can be
    found using this simple technique.
    """
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()