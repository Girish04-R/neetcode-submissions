from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top2 = Counter(nums).most_common(k)
        result = [item[0] for item in top2]
        return result