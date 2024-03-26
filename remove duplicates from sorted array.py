def removeDuplicates(nums):
        if not nums:
           return 0
        unique_elements = [nums[0]]
        for num in nums:
            if num != unique_elements[-1]:
                unique_elements.append(num)


        nums[:len(unique_elements)] = unique_elements

        return len(unique_elements)