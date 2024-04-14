def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = 0 #to keep track of the current position in changed list
        for i in nums:
            if n < 2 or i > nums[n-2]: #for i=1, n less than 2, so 1 placed at nums[0] and n=1; when i=1, same, nums[1]=1, n=2...
                nums[n] = i
                n+=1
        return n