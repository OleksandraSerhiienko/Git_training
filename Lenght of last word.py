class Solution(object):
    def lengthOfLastWord(self, s):
        spl_str = s.split()
        for i in spl_str:
            l = len(spl_str[-1])
        return l