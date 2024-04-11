def isIsomorphic(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return len(set(s))==len(set(t))==len(set(zip(s,t)))