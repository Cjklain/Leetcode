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


# asd = Solution().productExceptSelf([1, 2, 4, 6])


class Solution2:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        before = [0 for _ in range(len(nums))]
        after = [0 for _ in range(len(nums))]
        result = [0 for _ in range(len(nums))]

        for i, num in enumerate(nums):
            if i == 0:
                after[i] = 1
            else:

                after[i] = after[i - 1] * nums[i - 1]

        for i in range(len(nums) - 1, -1, -1):

            if len(nums) == i + 1:
                before[i] = 1
            else:
                before[i] = before[i + 1] * nums[i + 1]

        for x in range(len(after)):
            result[x] = after[x] * before[x]

        return result


zxc = Solution2().productExceptSelf([1, 2, 4, 6])


class Solution3:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        post = []
        pre = [0 for _ in range(len(nums))]

        for i, num in enumerate(nums):
            if i == 0:
                post.append(1)
            else:
                post.append(post[i - 1] * nums[i - 1])

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                pre[i] = 1
            else:
                pre[i] = pre[i + 1] * nums[i + 1]

        res = []

        for i in range(len(post)):
            res.append(pre[i] * post[i])

        return res


zxc = Solution3().productExceptSelf([-1, 0, 1, 2, 3])
print(zxc)
