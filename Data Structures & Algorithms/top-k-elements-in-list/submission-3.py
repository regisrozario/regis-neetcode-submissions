class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] +=1
        pq = []
        for key, val in freq.items():
            heapq.heappush(pq, (val,key))
            if len(pq) > k:
                heapq.heappop(pq)
        return [key for val,key in pq]


        
        

            
        