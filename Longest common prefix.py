def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs:
        return " "
    shortest_word = min(strs, key=len)
    for i, char in enumerate(shortest_word):
        for other_words in strs:
            if other_words[i] != char:
                return shortest_word[:i]
    return shortest_word