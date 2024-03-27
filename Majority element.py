def majorityElement(nums):
        n = len(nums)
        count = {}
        for numb in nums:
            if numb not in count:
                count[numb] = 1
            else:
                count[numb] +=1
            if count[numb]> n/2:
                print(count)
            return numb