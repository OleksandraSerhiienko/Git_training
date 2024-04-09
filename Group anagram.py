def groupAnagrams(strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict_anagrams={}
        for i in strs:
            word = ''.join(sorted(i)) #sorts characters in ascending order and joins them back in a word
            print(word)
            if word in dict_anagrams:
                dict_anagrams[word].append(i)
            else:
                dict_anagrams[word] = [i] # sorted word is a key and value is the list with current word
        return list(dict_anagrams.values())
            