class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        r = 0
        # list -> for (indexing)
        # dict (map) -> key (element) -> value (index)
        d = {}  # hashing
        for i in range(len(nums)):
            r = target - nums[i]
            if r in d.keys():
                return [d[r], i]
            else:
                d[nums[i]] = i

        """
        1. element is inserted to map (element - index)
        2. when element is same as the required element,
            required element in dict.keys()
            return dict[element]

        """
