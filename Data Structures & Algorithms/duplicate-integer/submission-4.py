class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr = set()
        for i in nums:
            print(i)
            if i in arr:
                return True
            arr.add(i)
        return False