class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        A = [int(digit) for digit in str(x)]
        return A== A[::-1]