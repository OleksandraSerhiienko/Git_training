def rotate(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if k>=len(nums): 
                k = k%len(nums)
        # Rotate the array using slicing
        nums[:] = nums[-k:] + nums[:-k] #extracts the range  from the last k element of the array till the end; then extracts all elements of the array except the last k elements and concatenates those two slices
        return nums