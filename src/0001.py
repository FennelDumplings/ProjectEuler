
"""
https://projecteuler.net/problem=1

Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""

import sys


class Solution:
    def __init__(self, x, y, n):
        self.x = x
        self.y = y
        self.n = n

    def __call__(self):
        l1 = [i * self.x for i in range(1, (self.n - 1) // self.x + 1)]
        l2 = [i * self.y for i in range(1, (self.n - 1) // self.y + 1)]
        setting = set(l1)
        setting = setting.union(set(l2))
        return sum(setting)


if __name__ == "__main__":
    x, y, n = sys.argv[1:]
    solution = Solution(int(x), int(y), int(n))
    ans = solution()
    print(ans)
