def containsNearbyDuplicate(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        indices = {}
        for i, num in enumerate(nums):
            if num in indices:
                if i - indices[num] <=k:
                    return True
            indices[num] = i
        return False               