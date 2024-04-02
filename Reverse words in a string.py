def reverseWords(s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        words.reverse()
        words = " ".join(words)
        return words