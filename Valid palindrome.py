def isPalindrome( s):
    s = s.lower()
    split_s = s.split()
    join_s = "".join(split_s)
    join_s = ''.join(i for i in s if i.isalnum())
    if join_s[:] == join_s[::-1]:
        return True
    else:
        return False

    return join_s