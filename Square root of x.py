def mySqrt(x):
        """
        :type x: int
        :rtype: int
        """
        if x==0:
            return 0
        elif x ==1:
            return 1
        for i in range(1, x+1):
            if i *i >x:
                return i-1