class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        result = []
        freq = [[] for i in range(len(nums) + 1)]

        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for n, c in count.items():
            freq[c].append(n)

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
