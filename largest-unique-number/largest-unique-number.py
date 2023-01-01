from collections import defaultdict
class Solution: 
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        ones = set()

        for num, count in counts.items():
            if count == 1:
                ones.add(num)
        if len(ones) == 0:
            return -1
        else:
            return max(ones)


