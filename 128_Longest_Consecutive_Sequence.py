class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        set_nums = set(nums)
        longest = 0
        for num in nums:
            # detect first element of sequence
            if not num - 1 in set_nums:
                temp = 0
                while num + temp in set_nums:
                    temp += 1
                    if temp > longest:
                        longest = temp
        return longest


# test = Solution().longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
# print(test)


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        set_nums = set(nums)
        longest = 0
        for num in nums:
            # detect first element of sequence
            if not num - 1 in set_nums:
                temp = 0
                while num + temp in set_nums:
                    temp += 1
                longest = max(temp, longest)
        return longest


from collections import defaultdict


class Solution2:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = set(nums)
        longest = 0
        for el in nums:
            temp = []
            if el - 1 not in nums:
                temp.append(el)
                i = 1
                while el + i in nums:
                    i += 1
                    temp.append(el + 1)
                if len(temp) > longest:
                    longest = len(temp)
        return longest


ads = Solution2().longestConsecutive([0, 3, 2, 5, 4, 6, 1, 1])
print(ads)
