"""
Problem #5 - Jane Street - CAR/CDR Pair - Hard

This problem was asked by Jane Street.

cons(a, b)constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.
"""

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(cons: callable) -> int:
    def return_first(a,b):
        return a
    return cons(return_first)

def cdr(cons: callable) -> int:
    def return_last(a,b):
        return b
    return cons(return_last)

if __name__ == '__main__':
    print("\nSample tests below:")
    print(f"car(cons(3, 4))  gives the output of {car(cons(3, 4))}")
    print(f"cdr(cons(3, 4))  gives the output of {cdr(cons(3, 4))}")