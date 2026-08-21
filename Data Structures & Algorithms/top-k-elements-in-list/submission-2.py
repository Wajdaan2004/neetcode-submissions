class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        order = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n,i in count.items():
            order[i].append(n)
        
        result = []
        for i in range(len(order)-1, 0, -1):
            for n in order[i]:
                result.append(n)
                if len(result) == k:
                    return result