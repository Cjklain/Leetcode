class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = []
        for i, num in enumerate(nums):
            if i == 0:
                temp = num
            else:
                temp = temp * num
            prefix.append(temp)
        postfix = [None] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                temp = nums[i]
            else:
                temp = temp * nums[i]
            postfix[i] = temp

        res = []
        for i, num in enumerate(nums):
            if i == 0:
                res.append(postfix[1])
            elif i == len(nums) - 1:
                res.append(prefix[i-1])
            else:
                res.append(prefix[i - 1] * postfix[i + 1])
        return res

test = Solution().productExceptSelf(nums = [4,3,2,1,2])
