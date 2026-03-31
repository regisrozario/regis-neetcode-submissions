class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        
        heap: [tuple[int,int]] = []

        for num, count in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (count,num))
            else:
                heapq.heappushpop(heap, (count, num))
        return [num for _,num in heap]
        