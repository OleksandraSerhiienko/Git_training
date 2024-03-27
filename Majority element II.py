def majorityElement(nums):
        n = len(nums)
        count = {}
        main_chs = []
        for numb in nums:
            if numb not in count:
                count[numb] = 1
            else:
                count[numb] +=1
            if count[numb] > n/3 and numb not in main_chs:
                main_chs.append(numb)
                continue
        return main_chs