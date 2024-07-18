# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:
#         if len(nums) > pow(10, 5):
#             return
#         for i in range(len(nums)):
#             print(nums[i], 'a')
#             # print(i, 'a')
#             for j in range(1, len(nums) - i):
#                 if nums[i] == nums[-j]:
#                     return True
#                 print(j , nums[-j], 'b')
#         return False
#             # for k 

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        record_list = {}
        if len(nums) > pow(10, 5):
            return
        for num in nums:
            if num in record_list:
                # print(num)
                return True
            record_list[num] = 1
        return False

test = Solution()

# print(test.containsDuplicate(nums = [2,14,18,22,22]))
# print(test.containsDuplicate(nums = [1,2,3,4]))


print(test.containsDuplicate(asd))