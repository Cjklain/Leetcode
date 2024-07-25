class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        set_nums = set(nums)
        print(set_nums)
        longest = 0
        for num in nums:
            print("asd")
            # detect first element of sequence
            if not num - 1 in set_nums:
                # print(num)
                temp = 0
                while num + temp in set_nums:
                    temp += 1
                    if temp > longest:
                        longest = temp
                    print(temp)
        return longest


test = Solution().longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
print(test)
