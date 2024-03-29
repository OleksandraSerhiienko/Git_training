def isSubsequence(s, t):
    letters = iter(t)
    for i in s:
        if i not in letters:
            return False
    return True
   