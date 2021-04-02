# -*- coding: utf-8 -*-

"""
https://projecteuler.net/problem=2

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

"""
a[1], a[4], a[8], ... 是偶数
"""


def solution():
    a0 = 1
    a1 = 2
    ans = 0
    while a1 <= 4000000:
        if a1 % 2 == 0:
            ans += a1
        tmp = a0 + a1
        a0 = a1
        a1 = tmp
    print(ans)


if __name__ == "__main__":
    solution()
