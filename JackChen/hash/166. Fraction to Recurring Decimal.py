"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".
Hint:

No scary math, just apply elementary math knowledge. Still remember how to perform a long division?
Try a long division on 4/9, the repeating part is obvious. Now try 4/333. Do you see a pattern?
Be wary of edge cases! List out as many test cases as you can think of and test your code thoroughly.
"""

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        n, d = numerator, denominator
        hash, result = {}, ''
        if n == 0:
            return '0'
        if n*d < 0:
            result = '-'
        n, d = abs(n), abs(d)
        result += str(n/d)
        if n % d == 0:
            return result
        result += '.'
        n = n % d
        while n:
            if n in hash.keys():
                result = result[0:hash[n]] + '(' + result[hash[n]:] + ')'
                break
            hash[n] = len(result)
            n *= 10
            result += str(n/d)
            n %= d
        return result
