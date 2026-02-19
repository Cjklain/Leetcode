# class Solution:
#     def productExceptSelf(self, nums: list[int]) -> list[int]:
#         prefix = []
#         for i, num in enumerate(nums):
#             if i == 0:
#                 temp = num
#             else:
#                 temp = temp * num
#             prefix.append(temp)
#         postfix = [None] * len(nums)
#         for i in range(len(nums) - 1, -1, -1):
#             if i == len(nums) - 1:
#                 temp = nums[i]
#             else:
#                 temp = temp * nums[i]
#             postfix[i] = temp

#         res = []
#         for i, num in enumerate(nums):
#             if i == 0:
#                 res.append(postfix[1])
#             elif i == len(nums) - 1:
#                 res.append(prefix[i-1])
#             else:
#                 res.append(prefix[i - 1] * postfix[i + 1])
#         return res

# test = Solution().productExceptSelf(nums = [4,3,2,1,2])


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)

        after = [1] * n
        before = [1] * n
        result = [1] * n

        for i, num in enumerate(nums):
            if i == 0:
                after[0] = 1
            else:
                after[i] = after[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            print(i)
            if i == n:
                before[n] = 1
            else:
                before[i] = nums[i + 1] * before[i + 1]

        # before or after in enumarete doesen't matter
        for i, num in enumerate(before):
            result[i] = before[i] * after[i]

        return result

        print(after)
        print(before)
        print(result)


asd = Solution().productExceptSelf([1, 2, 4, 6])
