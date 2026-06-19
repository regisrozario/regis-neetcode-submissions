class Solution:
    def reorganizeString(self, s: str) -> str:
        count  = Counter(s)
        heap = [(-cnt, ch) for ch, cnt in count.items()]
        heapq.heapify(heap)
        if -heap[0][0] > (len(s)+1)//2:
            return ""

        result = []
        while heap:
            count, char = heapq.heappop(heap)
            if len(result) > 0: 
                if result[-1] != char:
                    result.append(char)
                    count = -count -1
                    if count > 0:
                        heapq.heappush(heap, (-count, char))
                else:
                    nextcount, nextchar = heapq.heappop(heap)
                    result.append(nextchar)
                    nextcount = -nextcount -1
                    if nextcount > 0:
                        heapq.heappush(heap, (-nextcount, nextchar))
                    heapq.heappush(heap, (count, char))
            else:
                result.append(char)
                count = -count -1
                if count > 0:
                    heapq.heappush(heap, (-count, char))
        print(result)
        return "".join(result)
        

        