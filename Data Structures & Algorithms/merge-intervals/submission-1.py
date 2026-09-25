class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intravels = sorted(intervals, key=lambda x: x[0])
        merged = [sorted_intravels[0]]
        for timing in sorted_intravels[1:]:
            last = merged.pop()
            if timing[0] <= last[1]:
                last[1] = max(last[1], timing[1])   
                merged.append(last)
            else:
                merged.append(last)
                merged.append(timing)
        return merged
        