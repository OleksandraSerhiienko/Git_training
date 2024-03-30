def isAnagram(s, t):
    if len(s) != len(t):
        return False
    s_list = []
    t_list = []
    for letter in s:
        s_list.append(letter)
    for letter in t:
        t_list.append(letter)
    s_list.sort()
    t_list.sort()
    
    if s_list == t_list:
        return(True)
    else:
        return(False)