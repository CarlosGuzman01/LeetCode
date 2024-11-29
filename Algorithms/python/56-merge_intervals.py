class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        res = [intervals[0]]

        for start, end in intervals[1:]:
            last = res[-1][1] 

            if last >= start:
                res[-1][1] = max(last, end)
            else:
                res.append([start, end])
        return res