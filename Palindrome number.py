def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        x=str(x)
        if x == x[::-1]:
            return True
        else:
            return False