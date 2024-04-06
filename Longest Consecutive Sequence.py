def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    nums_set = set(nums)
    max_len = 0 #initial lenght of longest consequtive sequence 
    for num in nums_set:
            if num - 1 not in nums_set:
                    real_num = num
                    len_seq = 1
                    
                    while real_num + 1 in nums_set:
                            real_num +=1
                            len_seq +=1
                    max_len = max(max_len, len_seq) #from 0 to len_seq
                    
            
                            
    return max_len