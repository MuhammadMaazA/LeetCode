class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answer = [] 
        intervals.sort() # intervals.sort(key = lambda x:x[0])

        for interval in intervals:
            if not answer or answer[-1][1] < interval[0]:
                answer.append(interval)
            else:
                answer[-1][1] = max(answer[-1][1], interval[1])
        return answer
    
    # Time: O(nLogn) sort is log n and for loop is n
    # Space: O(1) if we ignore the space for the answer list else O(n)