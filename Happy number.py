def isHappy(n):
        """
        :type n: int
        :rtype: bool
        """
        digits=[]
        while n !=1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in digits:
                return False
            digits.append(n)
            print(digits)
        return True