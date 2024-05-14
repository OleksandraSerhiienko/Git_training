def merge(intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        new = []
        new.append(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] <= new[-1][1]:
                el = new.pop(-1)
                new.append([el[0], max(intervals[i][1], el[1])])
                #print(new)
            else:
                new.append(intervals[i])
                #new.append(intervals[-1])
                #print(new)
        return new