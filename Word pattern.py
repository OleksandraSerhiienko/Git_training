def wordPattern(pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s = s.split()
        if len(pattern) != len(s) or len(set(s)) != len(set(pattern)) :
            return False
        char_word = {}
        for char in range(len(pattern)):
            if pattern[char] not in char_word:
                char_word[pattern[char]] = s[char]
            elif char_word[pattern[char]] != s[char]:
                return False
        return True