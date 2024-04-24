def isUgly(n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False 
        for i in [2,3,5]:
            while n%i == 0:
                n = n//i  #can be written as n//=i; divide and change this number until n = 1
        return n == 1 