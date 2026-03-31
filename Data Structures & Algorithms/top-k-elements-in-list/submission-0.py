class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] = freq.get(n,0)+1
        
        sorted_dict = sorted(freq.items(), key=lambda x:x[1]*-1)
        result = []
        for i in range(k):
            result.append(sorted_dict[i][0])
        return result


        
        

            
        